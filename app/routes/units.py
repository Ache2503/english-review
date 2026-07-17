from flask import Blueprint, render_template, redirect, url_for, flash, abort
from flask_login import login_required, current_user
from app.extensions import db
from app.models import Unit, UserProgress, GrammarRule, VocabularyCategory, WritingPractice, UnitExtra, Topic, TopicExplanation, SentencePatternContent
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
    
    return render_template('grammar/grammar_view.html',
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
    
    return render_template('vocabulary/vocabulary_view.html',
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
    
    return render_template('writing/writing_practice.html',
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
    
    sentence_patterns = {}
    for sp in SentencePatternContent.query.all():
        sentence_patterns[sp.topic_name] = {'patterns': sp.patterns}
    
    return render_template('sentences/sentence_structures.html',
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

@units_bp.route('/topic/<int:topic_id>')
@login_required
def topic_detail(topic_id):
    """Ver detalles de un tema específico dentro de una unidad"""
    # 1. Obtener el tópico
    topic = Topic.query.get_or_404(topic_id)
    
    # 2. Verificar si la unidad a la que pertenece está desbloqueada
    unlock_system = UnitUnlockSystem(current_user.id)
    if not unlock_system.is_unit_unlocked(topic.unit_id):
        flash('🔒 Debes desbloquear esta unidad primero.', 'warning')
        return redirect(url_for('unit_challenge.units_overview'))

    # 3. Obtener explicaciones extra si existen
    explanations = topic.explanations.order_by(TopicExplanation.order).all()
    
    # 4. Buscar reglas gramaticales relacionadas por coincidencia de nombre
    # (Buscamos reglas que pertenezcan a la misma unidad y tengan el mismo título de tópico)
    grammar_rules = GrammarRule.query.filter_by(
        unit_id=topic.unit_id, 
        topic=topic.title 
    ).all()

    return render_template('units/topic_detail.html', 
                           topic=topic, 
                           explanations=explanations,
                           grammar_rules=grammar_rules)