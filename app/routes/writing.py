"""
Rutas para el Sistema de Análisis de Escritura.

Este módulo proporciona endpoints para:
- Análisis en tiempo real de escritura
- Feedback detallado de errores
- Historial de análisis
- Sugerencias de mejora
"""

from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user
from datetime import datetime

from app.services.writing_analysis import (
    WritingAnalyzer,
    quick_analyze,
    get_writing_feedback_html
)
from app.extensions import db
from app.models import ErrorLog

writing_bp = Blueprint('writing', __name__, url_prefix='/writing')


@writing_bp.route('/analyze')
@login_required
def analyze_page():
    """Página principal del analizador de escritura."""
    return render_template('writing/analyze.html')


@writing_bp.route('/analyze', methods=['POST'])
@login_required
def analyze_text():
    """
    Analiza un texto y devuelve feedback detallado.
    
    Acepta JSON o form data con:
    - text: El texto a analizar
    - unit_number: (opcional) Número de unidad para contexto
    - format: 'json' o 'html' (default: json)
    """
    if request.is_json:
        data = request.get_json()
        text = data.get('text', '')
        unit_number = data.get('unit_number')
        output_format = data.get('format', 'json')
    else:
        text = request.form.get('text', '')
        unit_number = request.form.get('unit_number')
        output_format = request.form.get('format', 'json')
    
    if not text or not text.strip():
        if output_format == 'html':
            return '<div class="alert alert-warning">Por favor escribe algo para analizar.</div>'
        return jsonify({'error': 'No text provided'}), 400
    
    # Convertir unit_number si existe
    if unit_number:
        try:
            unit_number = int(unit_number)
        except ValueError:
            unit_number = None
    
    # Analizar el texto
    if output_format == 'html':
        html_feedback = get_writing_feedback_html(text, unit_number)
        return html_feedback
    
    # Análisis completo para JSON
    analyzer = WritingAnalyzer()
    feedback = analyzer.analyze(text, {'unit_number': unit_number} if unit_number else None)
    
    # Guardar errores significativos en el log y en WritingAnalysisLog
    if current_user.is_authenticated:
        # Guardar en ErrorLog (errores individuales)
        for error in feedback.errors[:5]:
            if error.severity in ['high', 'medium']:
                error_log = ErrorLog(
                    user_id=current_user.id,
                    unit_id=unit_number,
                    source='writing_analyzer',
                    message=error.message,
                    context=error.context[:200] if error.context else None,
                    rule=error.rule_id
                )
                db.session.add(error_log)
        
        # Guardar análisis completo en WritingAnalysisLog
        from app.models import WritingAnalysisLog
        grammar_errors = sum(1 for e in feedback.errors if e.error_type.value == 'grammar')
        spelling_errors = sum(1 for e in feedback.errors if e.error_type.value == 'spelling')
        style_errors = sum(1 for e in feedback.errors if e.error_type.value == 'style')
        
        analysis_log = WritingAnalysisLog(
            user_id=current_user.id,
            unit_id=unit_number,
            original_text=text[:2000],  # Limitar tamaño
            word_count=feedback.summary.get('word_count', 0),
            sentence_count=feedback.summary.get('sentence_count', 0),
            score=feedback.score,
            grade=feedback.grade,
            grammar_errors=grammar_errors,
            spelling_errors=spelling_errors,
            style_errors=style_errors,
            errors_detail=[{
                'type': e.error_type.value,
                'message': e.message,
                'rule': e.rule_id
            } for e in feedback.errors[:10]],
            strengths=feedback.strengths,
            improvements=feedback.improvements
        )
        db.session.add(analysis_log)
        
        try:
            db.session.commit()
        except Exception:
            db.session.rollback()
    
    # Serializar respuesta
    return jsonify({
        'score': feedback.score,
        'grade': feedback.grade,
        'summary': feedback.summary,
        'errors': [
            {
                'type': error.error_type.value,
                'message': error.message,
                'context': error.context,
                'suggestions': error.suggestions,
                'severity': error.severity,
                'original': error.original_text
            }
            for error in feedback.errors
        ],
        'strengths': feedback.strengths,
        'improvements': feedback.improvements,
        'statistics': feedback.statistics
    })


@writing_bp.route('/quick-check', methods=['POST'])
@login_required
def quick_check():
    """
    Análisis rápido para retroalimentación en tiempo real.
    Optimizado para ser llamado mientras el usuario escribe.
    """
    data = request.get_json()
    text = data.get('text', '')
    
    if not text or len(text) < 10:
        return jsonify({
            'score': 0,
            'error_count': 0,
            'message': 'Escribe más para obtener feedback'
        })
    
    result = quick_analyze(text)
    
    return jsonify(result)


@writing_bp.route('/suggest-improvements', methods=['POST'])
@login_required
def suggest_improvements():
    """
    Sugiere mejoras específicas para el texto.
    """
    data = request.get_json()
    text = data.get('text', '')
    focus_area = data.get('focus_area', 'all')  # grammar, vocabulary, style, all
    
    if not text:
        return jsonify({'error': 'No text provided'}), 400
    
    analyzer = WritingAnalyzer()
    feedback = analyzer.analyze(text)
    
    suggestions = []
    
    if focus_area in ['all', 'grammar']:
        grammar_errors = [e for e in feedback.errors if e.error_type.value == 'grammar']
        for error in grammar_errors[:5]:
            suggestions.append({
                'type': 'grammar',
                'original': error.original_text,
                'message': error.message,
                'fix': error.suggestions[0] if error.suggestions else None
            })
    
    if focus_area in ['all', 'style']:
        style_errors = [e for e in feedback.errors if e.error_type.value == 'style']
        for error in style_errors[:5]:
            suggestions.append({
                'type': 'style',
                'original': error.original_text,
                'message': error.message,
                'alternatives': error.suggestions
            })
    
    if focus_area in ['all', 'vocabulary']:
        # Sugerencias de vocabulario basadas en el texto
        vocab_suggestions = []
        
        # Detectar palabras repetidas
        words = text.lower().split()
        word_counts = {}
        for word in words:
            if len(word) > 3:
                word_counts[word] = word_counts.get(word, 0) + 1
        
        repeated_words = {w: c for w, c in word_counts.items() if c > 2}
        for word, count in list(repeated_words.items())[:3]:
            vocab_suggestions.append({
                'type': 'vocabulary',
                'message': f"La palabra '{word}' aparece {count} veces. Considera usar sinónimos.",
                'original': word
            })
        
        suggestions.extend(vocab_suggestions)
    
    return jsonify({
        'suggestions': suggestions,
        'total_issues': len(feedback.errors),
        'score': feedback.score
    })


@writing_bp.route('/history')
@login_required
def history():
    """Muestra el historial de análisis del usuario."""
    from app.models import WritingAnalysisLog
    from sqlalchemy import func
    from datetime import timedelta
    
    # Obtener errores recientes del usuario
    recent_errors = ErrorLog.query.filter(
        ErrorLog.user_id == current_user.id,
        ErrorLog.source == 'writing_analyzer'
    ).order_by(ErrorLog.created_at.desc()).limit(50).all()
    
    # Agrupar por regla/tipo de error
    error_summary = {}
    for error in recent_errors:
        rule = error.rule or 'other'
        if rule not in error_summary:
            error_summary[rule] = {
                'count': 0,
                'examples': [],
                'last_seen': None
            }
        error_summary[rule]['count'] += 1
        if len(error_summary[rule]['examples']) < 3:
            error_summary[rule]['examples'].append(error.message)
        if error_summary[rule]['last_seen'] is None:
            error_summary[rule]['last_seen'] = error.created_at
    
    # Ordenar por frecuencia
    sorted_errors = sorted(error_summary.items(), key=lambda x: x[1]['count'], reverse=True)
    
    # Convertir a formato para template
    error_patterns = []
    for rule, data in sorted_errors[:10]:
        severity = 'high' if data['count'] > 5 else 'medium' if data['count'] > 2 else 'low'
        error_patterns.append({
            'error_type': rule.replace('_', ' ').title(),
            'count': data['count'],
            'severity': severity,
            'description': data['examples'][0] if data['examples'] else 'Error detectado',
            'example': data['examples'][1] if len(data['examples']) > 1 else ''
        })
    
    # Obtener análisis desde WritingAnalysisLog
    analyses = WritingAnalysisLog.query.filter(
        WritingAnalysisLog.user_id == current_user.id
    ).order_by(WritingAnalysisLog.analyzed_at.desc()).all()
    
    # Estadísticas generales desde la DB
    if analyses:
        total_words = sum(a.word_count or 0 for a in analyses)
        avg_score = sum(a.score or 0 for a in analyses) / len(analyses) if analyses else 0
    else:
        total_words = 0
        avg_score = 0
    
    stats = {
        'total_analyses': len(analyses),
        'total_errors': len(recent_errors),
        'avg_score': round(avg_score, 1) if avg_score else '--',
        'words_written': total_words
    }
    
    # Textos recientes desde WritingAnalysisLog
    recent_texts = []
    for analysis in analyses[:10]:
        recent_texts.append({
            'date': analysis.analyzed_at,
            'score': analysis.score or 0,
            'word_count': analysis.word_count or 0,
            'preview': analysis.original_text[:150] if analysis.original_text else '',
            'grammar_errors': analysis.grammar_errors or 0,
            'spelling_errors': analysis.spelling_errors or 0,
            'style_errors': analysis.style_errors or 0
        })
    
    # Calcular datos por semana para el gráfico
    now = datetime.utcnow()
    week_labels = []
    week_scores = []
    week_errors = []
    
    for i in range(4):
        week_end = now - timedelta(days=i*7)
        week_start = week_end - timedelta(days=7)
        week_labels.insert(0, f'Sem {4-i}')
        
        week_analyses = [a for a in analyses if week_start <= a.analyzed_at <= week_end]
        if week_analyses:
            week_scores.insert(0, round(sum(a.score or 0 for a in week_analyses) / len(week_analyses), 1))
            week_errors.insert(0, round(sum((a.grammar_errors or 0) + (a.spelling_errors or 0) for a in week_analyses) / len(week_analyses), 1))
        else:
            week_scores.insert(0, 0)
            week_errors.insert(0, 0)
    
    return render_template('writing/history.html',
                          error_patterns=error_patterns,
                          stats=stats,
                          recent_texts=recent_texts,
                          week_labels=week_labels,
                          week_scores=week_scores,
                          week_errors=week_errors)


@writing_bp.route('/tips/<error_type>')
@login_required
def get_tips(error_type):
    """Obtiene consejos específicos para un tipo de error."""
    
    # Base de conocimiento de consejos
    tips_database = {
        'SPANISH_SPEAKER_ERROR': {
            'title': 'Errores comunes de hispanohablantes',
            'description': 'Estos errores son típicos al traducir directamente del español.',
            'tips': [
                "Evita traducciones literales del español",
                "Recuerda que 'people' es plural en inglés",
                "Algunos sustantivos son incontables: information, advice, news",
                "'Actually' significa 'en realidad', no 'actualmente'",
                "Usa 'for' con duraciones y 'since' con puntos en el tiempo"
            ],
            'examples': [
                {'wrong': 'I am agree', 'correct': 'I agree'},
                {'wrong': 'The people is happy', 'correct': 'The people are happy'},
                {'wrong': 'I have 25 years', 'correct': 'I am 25 years old'}
            ]
        },
        'STYLE_IMPROVEMENT': {
            'title': 'Mejoras de estilo',
            'description': 'Usa palabras más precisas para un inglés más natural.',
            'tips': [
                "Evita 'very + adjective', usa adjetivos más fuertes",
                "Varía las estructuras de tus oraciones",
                "Usa conectores para mejorar la fluidez",
                "Evita repetir las mismas palabras"
            ],
            'examples': [
                {'wrong': 'very happy', 'correct': 'delighted, thrilled, ecstatic'},
                {'wrong': 'very big', 'correct': 'huge, enormous, massive'},
                {'wrong': 'very good', 'correct': 'excellent, outstanding, superb'}
            ]
        },
        'SENTENCE_CASE': {
            'title': 'Uso de mayúsculas',
            'description': 'Las reglas de capitalización en inglés.',
            'tips': [
                "Siempre inicia las oraciones con mayúscula",
                "Los nombres propios llevan mayúscula",
                "Los días de la semana y meses van con mayúscula",
                "'I' siempre va en mayúscula"
            ],
            'examples': [
                {'wrong': 'i went to london on monday', 'correct': 'I went to London on Monday'},
            ]
        },
        'default': {
            'title': 'Consejos generales de escritura',
            'description': 'Mejora tu escritura en inglés con estos consejos.',
            'tips': [
                "Lee en voz alta para detectar errores",
                "Revisa la concordancia sujeto-verbo",
                "Verifica los tiempos verbales",
                "Usa puntuación correctamente",
                "Practica escribiendo regularmente"
            ],
            'examples': []
        }
    }
    
    tips = tips_database.get(error_type, tips_database['default'])
    
    return jsonify(tips)


@writing_bp.route('/practice')
@login_required
def practice():
    """Página de práctica de escritura guiada."""
    # Obtener temas de práctica
    prompts = [
        {
            'id': 1,
            'title': 'Describe tu día',
            'description': 'Escribe sobre un día típico en tu vida.',
            'min_words': 50,
            'grammar_focus': ['Present Simple', 'Adverbs of Frequency'],
            'level': 'A2'
        },
        {
            'id': 2,
            'title': 'Un recuerdo especial',
            'description': 'Describe un recuerdo importante de tu pasado.',
            'min_words': 80,
            'grammar_focus': ['Past Simple', 'Used to', 'Past Perfect'],
            'level': 'B1'
        },
        {
            'id': 3,
            'title': 'Si pudiera viajar...',
            'description': 'Escribe sobre un viaje imaginario.',
            'min_words': 100,
            'grammar_focus': ['Second Conditional', 'Would'],
            'level': 'B1'
        },
        {
            'id': 4,
            'title': 'Opinión sobre tecnología',
            'description': 'Comparte tu opinión sobre el impacto de la tecnología.',
            'min_words': 120,
            'grammar_focus': ['Present Perfect', 'Passive Voice', 'Opinion phrases'],
            'level': 'B2'
        },
        {
            'id': 5,
            'title': 'Carta formal',
            'description': 'Escribe una carta formal de solicitud de empleo.',
            'min_words': 150,
            'grammar_focus': ['Formal language', 'Passive Voice', 'Modal verbs'],
            'level': 'B2'
        }
    ]
    
    return render_template('writing/practice.html', prompts=prompts)
