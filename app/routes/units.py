from flask import Blueprint, render_template, redirect, url_for, flash, abort
from flask_login import login_required, current_user
from app.extensions import db
from app.models import Unit, UserProgress, GrammarRule, VocabularyCategory, WritingPractice, UnitExtra
from app.services.unit_unlock import UnitUnlockSystem

units_bp = Blueprint('units', __name__, url_prefix='/units')


def check_unit_unlocked(unit_id):
    """Helper para verificar si la unidad está desbloqueada para el usuario actual"""
    unlock_system = UnitUnlockSystem(current_user.id)
    is_unlocked = unlock_system.is_unit_unlocked(unit_id)
    if not is_unlocked:
        return False, "Debes completar la unidad anterior primero."
    return True, None


@units_bp.route('/<int:unit_id>')
@login_required
def view_unit(unit_id):
    """Ver detalles de una unidad"""
    unit = Unit.query.get_or_404(unit_id)
    
    # Verificar si la unidad está desbloqueada
    unlock_system = UnitUnlockSystem(current_user.id)
    is_unlocked = unlock_system.is_unit_unlocked(unit_id)
    
    if not is_unlocked:
        flash('🔒 Debes completar la unidad anterior primero.', 'warning')
        return redirect(url_for('unit_challenge.units_overview'))
    
    # Obtener o crear progreso del usuario
    progress = UserProgress.query.filter_by(
        user_id=current_user.id,
        unit_id=unit_id
    ).first()
    
    if not progress:
        progress = UserProgress(user_id=current_user.id, unit_id=unit_id)
        db.session.add(progress)
        db.session.commit()
    
    # Obtener info de desbloqueo para la siguiente unidad
    unit_status = unlock_system.get_unit_requirements(unit_id)
    
    # Extra JSON activities/tips
    extra = UnitExtra.query.filter_by(unit_id=unit_id).first()
    activities = extra.data if extra and extra.data else {}

    return render_template('unit_detail.html',
                           unit=unit,
                           progress=progress,
                           activities=activities,
                           unit_status=unit_status)


@units_bp.route('/<int:unit_id>/grammar')
@login_required
def view_grammar(unit_id):
    """Ver reglas gramaticales de una unidad"""
    # Verificar si la unidad está desbloqueada
    is_unlocked, message = check_unit_unlocked(unit_id)
    if not is_unlocked:
        flash(f'🔒 {message}', 'warning')
        return redirect(url_for('unit_challenge.units_overview'))
    
    unit = Unit.query.get_or_404(unit_id)
    grammar_rules = GrammarRule.query.filter_by(unit_id=unit_id).order_by(GrammarRule.order).all()
    
    # Marcar gramática como completada
    unlock_system = UnitUnlockSystem(current_user.id)
    unlock_system.mark_section_complete(unit_id, 'grammar')
    
    return render_template('grammar_view.html',
                           unit=unit,
                           grammar_rules=grammar_rules)


@units_bp.route('/<int:unit_id>/vocabulary')
@login_required
def view_vocabulary(unit_id):
    """Ver vocabulario de una unidad"""
    # Verificar si la unidad está desbloqueada
    is_unlocked, message = check_unit_unlocked(unit_id)
    if not is_unlocked:
        flash(f'🔒 {message}', 'warning')
        return redirect(url_for('unit_challenge.units_overview'))
    
    unit = Unit.query.get_or_404(unit_id)
    vocab_categories = VocabularyCategory.query.filter_by(unit_id=unit_id).order_by(VocabularyCategory.order).all()
    
    # Marcar vocabulario como completado
    unlock_system = UnitUnlockSystem(current_user.id)
    unlock_system.mark_section_complete(unit_id, 'vocabulary')
    
    return render_template('vocabulary_view.html',
                           unit=unit,
                           vocab_categories=vocab_categories)


@units_bp.route('/<int:unit_id>/writing')
@login_required
def view_writing_practices(unit_id):
    """Ver ejercicios de escritura de una unidad"""
    # Verificar si la unidad está desbloqueada
    is_unlocked, message = check_unit_unlocked(unit_id)
    if not is_unlocked:
        flash(f'🔒 {message}', 'warning')
        return redirect(url_for('unit_challenge.units_overview'))
    
    unit = Unit.query.get_or_404(unit_id)
    writing_practices = WritingPractice.query.filter_by(unit_id=unit_id).order_by(WritingPractice.order).all()
    
    # Marcar ejercicios como completados
    unlock_system = UnitUnlockSystem(current_user.id)
    unlock_system.mark_section_complete(unit_id, 'exercises')
    
    return render_template('writing_practice.html',
                           unit=unit,
                           writing_practices=writing_practices)


@units_bp.route('/<int:unit_id>/sentence-structures')
@login_required
def view_sentence_structures(unit_id):
    """Ver estructuras de oraciones basadas en gramática de la unidad"""
    # Verificar si la unidad está desbloqueada
    is_unlocked, message = check_unit_unlocked(unit_id)
    if not is_unlocked:
        flash(f'🔒 {message}', 'warning')
        return redirect(url_for('unit_challenge.units_overview'))
    
    unit = Unit.query.get_or_404(unit_id)
    grammar_rules = GrammarRule.query.filter_by(unit_id=unit_id).order_by(GrammarRule.order).all()
    
    # Definir estructuras de oraciones por tema gramatical
    sentence_patterns = {
        'Articles': {
            'patterns': [
                {'structure': 'I go to [the] school', 'meaning': '[the] = edificio específico | sin artículo = como estudiante'},
                {'structure': 'Use [the] for specific things', 'meaning': 'Ej: The cat is black (gato específico)'},
                {'structure': 'Use [a/an] for general things', 'meaning': 'Ej: A cat is an animal (categoría general)'}
            ]
        },
        'Used to': {
            'patterns': [
                {'structure': 'Subject + used to + verb', 'meaning': 'Ej: I used to play soccer'},
                {'structure': 'I used to wake up early', 'meaning': 'Acción habitual en el pasado (ya no ocurre)'},
                {'structure': 'Did you use to...? / He used to...', 'meaning': 'Preguntas y respuestas negativas'}
            ]
        },
        'Reflexive Pronouns': {
            'patterns': [
                {'structure': 'Subject + verb + reflexive pronoun', 'meaning': 'Ej: I hurt myself'},
                {'structure': 'myself, yourself, himself, herself, itself, ourselves, yourselves, themselves', 'meaning': 'Cuando el sujeto y objeto son el mismo'},
                {'structure': 'She taught herself to code', 'meaning': 'Ella misma se enseñó (por su propia acción)'}
            ]
        },
        'Infinitive of Purpose': {
            'patterns': [
                {'structure': 'Subject + verb + to + infinitive', 'meaning': 'Ej: I went to the store to buy milk'},
                {'structure': '[action] + TO + [reason/purpose]', 'meaning': 'Ej: He exercises to stay healthy'},
                {'structure': 'I came to help you', 'meaning': 'Viniste CON EL PROPÓSITO DE ayudar'}
            ]
        },
        'First Conditional': {
            'patterns': [
                {'structure': 'If + Present + will + verb', 'meaning': 'Situación real/posible'},
                {'structure': 'If it rains, I will stay home', 'meaning': 'Si llueve (probable), me quedaré en casa'},
                {'structure': 'If you study, you will pass the exam', 'meaning': 'Resultado natural y lógico'}
            ]
        },
        'Second Conditional': {
            'patterns': [
                {'structure': 'If + Past + would + verb', 'meaning': 'Situación imaginaria/hipotética'},
                {'structure': 'If I had money, I would travel', 'meaning': 'Si tuviera dinero (no tengo), viajaría'},
                {'structure': 'If she were a bird, she would fly', 'meaning': 'Imaginario, no es real'}
            ]
        },
        'Gerunds': {
            'patterns': [
                {'structure': 'Verb + -ing (actuando como sustantivo)', 'meaning': 'Ej: Swimming is fun'},
                {'structure': 'Subject + verb + gerund', 'meaning': 'Ej: I enjoy reading books'},
                {'structure': 'Spending money is easy', 'meaning': 'El acto/acción como sustantivo'}
            ]
        },
        'Comparatives': {
            'patterns': [
                {'structure': 'Subject + verb + adjective + than + object', 'meaning': 'Ej: My house is bigger than yours'},
                {'structure': 'More + adjective + than', 'meaning': 'Para adjetivos largos: more expensive than'},
                {'structure': 'Adjective + -er + than', 'meaning': 'Para adjetivos cortos: faster than, taller than'}
            ]
        },
        'Superlatives': {
            'patterns': [
                {'structure': 'The + adjective + -est', 'meaning': 'Ej: the tallest, the fastest'},
                {'structure': 'The most + adjective', 'meaning': 'Para adjetivos largos: the most beautiful'},
                {'structure': 'Subject + verb + the + superlative', 'meaning': 'Ej: She is the smartest student'}
            ]
        },
        'Passive Voice': {
            'patterns': [
                {'structure': 'Object + be + past participle + by + subject', 'meaning': 'Ej: The car was washed by John'},
                {'structure': 'Plastic is found everywhere', 'meaning': 'La acción es más importante que quien la hace'},
                {'structure': 'The book was written by the author', 'meaning': 'Se enfoca en lo que pasó, no en quién lo hizo'}
            ]
        }
    }
    
    return render_template('sentence_structures.html',
                           unit=unit,
                           grammar_rules=grammar_rules,
                           sentence_patterns=sentence_patterns)


@units_bp.route('/<int:unit_id>/mark-complete', methods=['POST'])
@login_required
def mark_complete(unit_id):
    """Marcar unidad como completada - ahora requiere pasar el desafío"""
    unit = Unit.query.get_or_404(unit_id)
    
    progress = UserProgress.query.filter_by(
        user_id=current_user.id,
        unit_id=unit_id
    ).first_or_404()
    
    # Verificar si se completó el desafío
    if not progress.challenge_passed:
        flash('⚠️ Debes pasar el desafío de la unidad para completarla.', 'warning')
        return redirect(url_for('unit_challenge.unit_requirements', unit_id=unit_id))
    
    progress.completed = True
    progress.progress_percentage = 100.0
    db.session.commit()
    
    flash(f'🎉 ¡Unidad {unit.unit_number} completada! La siguiente unidad ha sido desbloqueada.', 'success')
    return redirect(url_for('unit_challenge.units_overview'))
