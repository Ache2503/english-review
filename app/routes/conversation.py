from flask import Blueprint, render_template, abort, request, session, redirect, url_for
from flask_login import login_required, current_user
import Levenshtein
from app.extensions import db
from app.models import Conversation, ConversationLine, ConversationPractice, AlternativeResponse, ResponsePattern
from datetime import datetime

conversation_bp = Blueprint('conversation', __name__, url_prefix='/conversation')


def load_conversation(scenario):
    """Cargar una conversación desde la BD en el formato del dict anterior"""
    conv = Conversation.query.filter_by(scenario=scenario).first()
    if not conv:
        return None
    
    meta = conv.extra_data or {}
    lines = ConversationLine.query.filter_by(
        conversation_id=conv.id
    ).order_by(ConversationLine.order).all()
    
    dialogue = []
    for line in lines:
        entry = {'speaker': line.speaker}
        if line.speaker == 'user':
            entry['expected'] = line.expected
            entry['options'] = line.options or [line.expected]
        else:
            entry['text'] = line.text
            if line.expected:
                entry['expected'] = line.expected
                entry['options'] = line.options or [line.expected]
        dialogue.append(entry)
    
    return {
        'title': conv.title,
        'description': conv.description,
        'user_role': meta.get('user_role', 'User'),
        'system_role': meta.get('system_role', 'System'),
        'icon': meta.get('icon', '💬'),
        'difficulty': meta.get('difficulty', 'Beginner'),
        'dialogue': dialogue
    }


def load_all_conversations():
    """Cargar todas las conversaciones desde la BD"""
    conversations = Conversation.query.order_by(Conversation.title).all()
    result = {}
    for conv in conversations:
        meta = conv.extra_data or {}
        result[conv.scenario] = {
            'title': conv.title,
            'description': conv.description,
            'user_role': meta.get('user_role', 'User'),
            'system_role': meta.get('system_role', 'System'),
            'icon': meta.get('icon', '💬'),
            'difficulty': meta.get('difficulty', 'Beginner'),
        }
    return result

def calculate_score(similarity):
    """Calcular puntaje basado en similitud"""
    if similarity > 0.85:
        return 100
    elif similarity > 0.7:
        return 80
    elif similarity > 0.5:
        return 60
    elif similarity > 0.3:
        return 40
    else:
        return 20

def get_feedback(similarity, expected, alternative_match=None):
    """Generar retroalimentación basada en similitud"""
    if alternative_match:
        return {
            'type': 'success', 
            'message': '¡Excelente! Tu respuesta es válida y natural.', 
            'suggestion': f'También podrías decir: "{expected}"',
            'learned': True
        }
    if similarity > 0.85:
        return {'type': 'success', 'message': '¡Excelente! Tu respuesta es muy natural.', 'suggestion': None}
    elif similarity > 0.7:
        return {'type': 'good', 'message': '¡Muy bien! Casi perfecto.', 'suggestion': f'Una forma ideal sería: "{expected}"'}
    elif similarity > 0.5:
        return {'type': 'ok', 'message': 'Bien, pero se puede mejorar.', 'suggestion': f'Intenta algo como: "{expected}"'}
    else:
        return {'type': 'needs_work', 'message': 'Sigue practicando.', 'suggestion': f'La respuesta esperada era: "{expected}"'}


def detect_pattern_type(text):
    """Detectar el tipo de patrón de una respuesta"""
    text_lower = text.lower()
    if any(word in text_lower for word in ['hello', 'hi', 'good morning', 'good afternoon', 'good evening']):
        return 'greeting'
    elif any(word in text_lower for word in ['thank', 'thanks', 'appreciate']):
        return 'thanks'
    elif any(word in text_lower for word in ['goodbye', 'bye', 'see you', 'take care']):
        return 'farewell'
    elif any(word in text_lower for word in ['please', 'could you', 'would you', 'can you']):
        return 'request'
    elif '?' in text:
        return 'question'
    elif any(word in text_lower for word in ['sorry', 'excuse me', 'pardon']):
        return 'apology'
    elif any(word in text_lower for word in ['yes', 'sure', 'of course', 'certainly']):
        return 'affirmation'
    elif any(word in text_lower for word in ['no', 'not', "don't", "can't"]):
        return 'negation'
    return 'general'


def find_alternative_match(user_input, scenario, step):
    """Buscar coincidencias con respuestas alternativas guardadas"""
    alternatives = AlternativeResponse.query.filter_by(
        scenario=scenario, 
        step=step
    ).filter(
        AlternativeResponse.times_used >= 2  # Solo usar alternativas usadas más de una vez
    ).all()
    
    for alt in alternatives:
        similarity = Levenshtein.ratio(user_input.lower(), alt.alternative_text.lower())
        if similarity > 0.85:
            return alt
    return None


def find_cross_scenario_match(user_input):
    """Buscar si la respuesta coincide con patrones de otros escenarios"""
    # Buscar patrones similares en la base de datos
    patterns = ResponsePattern.query.all()
    
    for pattern in patterns:
        similarity = Levenshtein.ratio(user_input.lower(), pattern.pattern_text.lower())
        if similarity > 0.8:
            return {
                'pattern': pattern,
                'similarity': similarity,
                'applicable_scenarios': pattern.applicable_scenarios or []
            }
    return None


def save_alternative_response(user_input, scenario, step, expected, similarity, user_id=None):
    """Guardar una respuesta alternativa válida del usuario"""
    # Verificar si ya existe esta alternativa
    existing = AlternativeResponse.query.filter_by(
        scenario=scenario,
        step=step,
        alternative_text=user_input
    ).first()
    
    if existing:
        # Incrementar el contador de uso
        existing.times_used += 1
        db.session.commit()
        return existing
    
    # Crear nueva alternativa si la similitud es razonable (entre 0.4 y 0.85)
    if 0.4 <= similarity <= 0.85:
        new_alt = AlternativeResponse(
            scenario=scenario,
            step=step,
            original_expected=expected,
            alternative_text=user_input,
            similarity_score=similarity,
            created_by_user_id=user_id
        )
        db.session.add(new_alt)
        db.session.commit()
        return new_alt
    return None


def save_or_update_pattern(text, pattern_type, scenario):
    """Guardar o actualizar un patrón de respuesta"""
    # Buscar patrón similar existente
    existing_patterns = ResponsePattern.query.filter_by(pattern_type=pattern_type).all()
    
    for pattern in existing_patterns:
        similarity = Levenshtein.ratio(text.lower(), pattern.pattern_text.lower())
        if similarity > 0.85:
            # Actualizar patrón existente
            pattern.usage_count += 1
            if pattern.applicable_scenarios:
                if scenario not in pattern.applicable_scenarios:
                    pattern.applicable_scenarios = pattern.applicable_scenarios + [scenario]
            else:
                pattern.applicable_scenarios = [scenario]
            db.session.commit()
            return pattern
    
    # Crear nuevo patrón
    new_pattern = ResponsePattern(
        pattern_text=text,
        pattern_type=pattern_type,
        applicable_scenarios=[scenario]
    )
    db.session.add(new_pattern)
    db.session.commit()
    return new_pattern


def get_learned_options(scenario, step):
    """Obtener opciones aprendidas de la base de datos"""
    alternatives = AlternativeResponse.query.filter_by(
        scenario=scenario,
        step=step
    ).filter(
        AlternativeResponse.times_used >= 3  # Solo mostrar alternativas populares
    ).order_by(
        AlternativeResponse.times_used.desc()
    ).limit(2).all()
    
    return [alt.alternative_text for alt in alternatives]


@conversation_bp.route('/')
def list():
    conversations = load_all_conversations()
    return render_template(
        'conversation/conversation_list.html',
        conversations=conversations
    )


@conversation_bp.route('/<scenario>', methods=['GET', 'POST'])
def detail(scenario):
    conversation = load_conversation(scenario)
    if not conversation:
        abort(404)

    # Inicializar sesión para este escenario
    session_key = f'conversation_{scenario}'
    if session_key not in session or request.args.get('restart'):
        session[session_key] = {
            'step': 0,
            'history': [],
            'scores': [],
            'completed': False
        }

    conv_state = session[session_key]
    dialogue = conversation['dialogue']
    current_step = conv_state['step']
    
    # Variables para la plantilla
    system_message = None
    user_prompt = None
    is_completed = conv_state['completed']
    final_score = None
    
    if request.method == 'POST' and not is_completed:
        user_sentence = request.form.get('user_sentence', '').strip()
        
        # Encontrar la respuesta esperada del usuario
        expected = None
        step_index = None
        for i, line in enumerate(dialogue):
            if i == current_step and line['speaker'] == 'user':
                expected = line['expected']
                step_index = i
                break
        
        if expected:
            # Calcular similitud con la respuesta esperada
            similarity = Levenshtein.ratio(user_sentence.lower(), expected.lower())
            
            # Buscar coincidencia con respuestas alternativas aprendidas
            alternative_match = find_alternative_match(user_sentence, scenario, current_step)
            
            # Buscar coincidencia con patrones de otros escenarios
            cross_match = find_cross_scenario_match(user_sentence)
            
            # Determinar el puntaje y feedback
            if alternative_match:
                # La respuesta coincide con una alternativa aprendida
                score = 90
                feedback = get_feedback(similarity, expected, alternative_match=alternative_match)
                # Incrementar uso de la alternativa
                alternative_match.times_used += 1
                db.session.commit()
            else:
                score = calculate_score(similarity)
                feedback = get_feedback(similarity, expected)
            
            # Si la respuesta es razonable pero diferente, guardarla como alternativa
            user_id = current_user.id if current_user.is_authenticated else None
            if 0.4 <= similarity <= 0.85 and len(user_sentence) > 5:
                save_alternative_response(user_sentence, scenario, current_step, expected, similarity, user_id)
                
                # Detectar y guardar el patrón
                pattern_type = detect_pattern_type(user_sentence)
                save_or_update_pattern(user_sentence, pattern_type, scenario)
            
            # Agregar info de cross-match al feedback si aplica
            if cross_match and not alternative_match:
                feedback['cross_scenario'] = {
                    'message': f'Tu respuesta también funcionaría en: {", ".join(cross_match["applicable_scenarios"][:3])}',
                    'pattern_type': cross_match['pattern']['pattern_type']
                }
            
            # Obtener el mensaje del sistema que precedía este turno del usuario
            system_msg_for_history = None
            for k in range(current_step - 1, -1, -1):
                if dialogue[k]['speaker'] == 'system':
                    system_msg_for_history = dialogue[k]['text']
                    break
            
            # Guardar en historial
            conv_state['history'].append({
                'step': current_step,
                'system_msg': system_msg_for_history,
                'user_input': user_sentence,
                'expected': expected,
                'similarity': round(similarity * 100, 1),
                'score': score,
                'feedback': feedback,
                'learned_match': alternative_match is not None,
                'cross_match': cross_match is not None
            })
            conv_state['scores'].append(score)
            
            # Avanzar al siguiente paso
            conv_state['step'] = current_step + 1
            current_step = conv_state['step']
        
        # Verificar si la conversación ha terminado
        if current_step >= len(dialogue):
            conv_state['completed'] = True
            is_completed = True
    
    # Obtener el mensaje actual del sistema
    if not is_completed:
        for i, line in enumerate(dialogue):
            if i >= current_step:
                if line['speaker'] == 'system':
                    system_message = line['text']
                    # Buscar el siguiente turno del usuario
                    for j in range(i + 1, len(dialogue)):
                        if dialogue[j]['speaker'] == 'user':
                            user_prompt = dialogue[j].get('expected', '')
                            conv_state['step'] = j
                            break
                    break
                elif line['speaker'] == 'user' and i == current_step:
                    # Buscar el mensaje del sistema anterior
                    for k in range(i - 1, -1, -1):
                        if dialogue[k]['speaker'] == 'system':
                            system_message = dialogue[k]['text']
                            break
                    user_prompt = line.get('expected', '')
                    break
    
    # Calcular puntaje final y guardar si está completado
    if is_completed and conv_state['scores']:
        final_score = round(sum(conv_state['scores']) / len(conv_state['scores']), 1)
        
        # Guardar en la base de datos si el usuario está autenticado y no se ha guardado aún
        if current_user.is_authenticated and not conv_state.get('saved'):
            practice = ConversationPractice(
                user_id=current_user.id,
                scenario=scenario,
                final_score=final_score,
                total_responses=len(conv_state['history']),
                practice_data=conv_state['history']
            )
            db.session.add(practice)
            db.session.commit()
            conv_state['saved'] = True
    
    # Obtener opciones de respuesta para el paso actual
    response_options = []
    learned_options = []
    if not is_completed:
        for i, line in enumerate(dialogue):
            if i == current_step and line['speaker'] == 'user':
                response_options = line.get('options', [])
                # Obtener opciones aprendidas de la base de datos
                learned_options = get_learned_options(scenario, current_step)
                break
    
    session[session_key] = conv_state
    
    return render_template(
        'conversation/conversation_detail.html',
        conversation=conversation,
        scenario=scenario,
        system_message=system_message,
        history=conv_state['history'],
        is_completed=is_completed,
        final_score=final_score,
        current_step=current_step,
        total_steps=len([d for d in dialogue if d['speaker'] == 'user']),
        response_options=response_options,
        learned_options=learned_options
    )
