"""
Panel de Administracion
======================
CRUD de contenido, gestion de usuarios y resultados de estudiantes.
"""

import json
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user
from app.extensions import db
from app.decorators import admin_required
from app.models import (
    User, UserProgress, UserQuizSubmission, UserWritingSubmission,
    UserReadingSubmission, StudyExerciseResult, UserStreak,
    StudyTopicContent, GrammarTopicContent, SentencePatternContent,
    WritingErrorPattern, WritingTipContent, ConceptSynonym,
    ErrorTipContent, AchievementMilestone,
    Quiz, QuizQuestion, Unit
)
from sqlalchemy import func, desc

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')


# ===========================
# MIDDLEWARE
# ===========================

@admin_bp.before_request
@login_required
def before_request():
    if not current_user.is_admin:
        flash('Acceso denegado.', 'danger')
        return redirect(url_for('main.index'))


# ===========================
# DASHBOARD
# ===========================

@admin_bp.route('/')
def dashboard():
    total_users = User.query.count()
    active_users = User.query.filter(User.last_login_date.isnot(None)).count()
    premium_users = User.query.filter(User.subscription_type != 'free').count()
    admin_users = User.query.filter_by(is_admin=True).count()

    total_quizzes = UserQuizSubmission.query.count()
    total_writings = UserWritingSubmission.query.count()
    total_readings = UserReadingSubmission.query.count()
    total_study = StudyExerciseResult.query.count()

    recent_users = User.query.order_by(desc(User.created_at)).limit(10).all()

    content_stats = {
        'study_topics': StudyTopicContent.query.count(),
        'grammar_topics': GrammarTopicContent.query.count(),
        'sentence_patterns': SentencePatternContent.query.count(),
        'writing_patterns': WritingErrorPattern.query.count(),
        'writing_tips': WritingTipContent.query.count(),
        'concept_synonyms': ConceptSynonym.query.count(),
        'error_tips': ErrorTipContent.query.count(),
        'milestones': AchievementMilestone.query.count(),
    }

    return render_template('admin/dashboard.html',
        total_users=total_users,
        active_users=active_users,
        premium_users=premium_users,
        admin_users=admin_users,
        total_quizzes=total_quizzes,
        total_writings=total_writings,
        total_readings=total_readings,
        total_study=total_study,
        recent_users=recent_users,
        content_stats=content_stats,
    )


# ===========================
# STUDY TOPICS
# ===========================

@admin_bp.route('/study')
def study_list():
    topics = StudyTopicContent.query.order_by(StudyTopicContent.id).all()
    return render_template('admin/content_list.html',
        title='Temas de Estudio',
        items=topics,
        create_url=url_for('admin.study_create'),
        edit_url_func=lambda t: url_for('admin.study_edit', id=t.id),
        delete_url_func=lambda t: url_for('admin.study_delete', id=t.id),
        fields=['slug', 'title', 'icon', 'difficulty', 'estimated_time'],
        model_name='StudyTopicContent',
    )


@admin_bp.route('/study/new', methods=['GET', 'POST'])
def study_create():
    if request.method == 'POST':
        topic = StudyTopicContent(
            slug=request.form['slug'].strip(),
            title=request.form['title'].strip(),
            icon=request.form.get('icon', '').strip() or None,
            difficulty=request.form.get('difficulty', '').strip() or None,
            estimated_time=request.form.get('estimated_time', '').strip() or None,
            description=request.form.get('description', '').strip() or None,
        )
        for field in ('theory', 'common_mistakes', 'tips', 'exercises'):
            raw = request.form.get(field, '').strip()
            if raw:
                try:
                    setattr(topic, field, json.loads(raw))
                except json.JSONDecodeError:
                    flash(f'JSON invalido en {field}', 'warning')
        db.session.add(topic)
        db.session.commit()
        flash('Tema de estudio creado.', 'success')
        return redirect(url_for('admin.study_list'))
    return render_template('admin/content_form.html',
        title='Nuevo Tema de Estudio',
        action=url_for('admin.study_create'),
    )


@admin_bp.route('/study/<int:id>/edit', methods=['GET', 'POST'])
def study_edit(id):
    topic = StudyTopicContent.query.get_or_404(id)
    if request.method == 'POST':
        topic.slug = request.form['slug'].strip()
        topic.title = request.form['title'].strip()
        topic.icon = request.form.get('icon', '').strip() or None
        topic.difficulty = request.form.get('difficulty', '').strip() or None
        topic.estimated_time = request.form.get('estimated_time', '').strip() or None
        topic.description = request.form.get('description', '').strip() or None
        for field in ('theory', 'common_mistakes', 'tips', 'exercises'):
            raw = request.form.get(field, '').strip()
            if raw:
                try:
                    setattr(topic, field, json.loads(raw))
                except json.JSONDecodeError:
                    flash(f'JSON invalido en {field}', 'warning')
            else:
                setattr(topic, field, None)
        db.session.commit()
        flash('Tema de estudio actualizado.', 'success')
        return redirect(url_for('admin.study_list'))
    return render_template('admin/content_form.html',
        title='Editar Tema de Estudio',
        action=url_for('admin.study_edit', id=id),
        item=topic,
    )


@admin_bp.route('/study/<int:id>/delete', methods=['POST'])
def study_delete(id):
    topic = StudyTopicContent.query.get_or_404(id)
    db.session.delete(topic)
    db.session.commit()
    flash('Tema de estudio eliminado.', 'success')
    return redirect(url_for('admin.study_list'))


# ===========================
# GRAMMAR TOPICS
# ===========================

@admin_bp.route('/grammar')
def grammar_list():
    topics = GrammarTopicContent.query.order_by(GrammarTopicContent.id).all()
    return render_template('admin/content_list.html',
        title='Temas de Gramatica',
        items=topics,
        create_url=url_for('admin.grammar_create'),
        edit_url_func=lambda t: url_for('admin.grammar_edit', id=t.id),
        delete_url_func=lambda t: url_for('admin.grammar_delete', id=t.id),
        fields=['slug', 'title', 'level', 'category', 'icon'],
        model_name='GrammarTopicContent',
    )


@admin_bp.route('/grammar/new', methods=['GET', 'POST'])
def grammar_create():
    if request.method == 'POST':
        topic = GrammarTopicContent(
            slug=request.form['slug'].strip(),
            title=request.form['title'].strip(),
            subtitle=request.form.get('subtitle', '').strip() or None,
            icon=request.form.get('icon', '').strip() or None,
            level=request.form.get('level', '').strip() or None,
            category=request.form.get('category', '').strip() or None,
            description=request.form.get('description', '').strip() or None,
            estimated_time=request.form.get('estimated_time', '').strip() or None,
        )
        for field in ('sections', 'tips', 'common_mistakes'):
            raw = request.form.get(field, '').strip()
            if raw:
                try:
                    setattr(topic, field, json.loads(raw))
                except json.JSONDecodeError:
                    flash(f'JSON invalido en {field}', 'warning')
        db.session.add(topic)
        db.session.commit()
        flash('Tema de gramatica creado.', 'success')
        return redirect(url_for('admin.grammar_list'))
    return render_template('admin/content_form.html',
        title='Nuevo Tema de Gramatica',
        action=url_for('admin.grammar_create'),
    )


@admin_bp.route('/grammar/<int:id>/edit', methods=['GET', 'POST'])
def grammar_edit(id):
    topic = GrammarTopicContent.query.get_or_404(id)
    if request.method == 'POST':
        topic.slug = request.form['slug'].strip()
        topic.title = request.form['title'].strip()
        topic.subtitle = request.form.get('subtitle', '').strip() or None
        topic.icon = request.form.get('icon', '').strip() or None
        topic.level = request.form.get('level', '').strip() or None
        topic.category = request.form.get('category', '').strip() or None
        topic.description = request.form.get('description', '').strip() or None
        topic.estimated_time = request.form.get('estimated_time', '').strip() or None
        for field in ('sections', 'tips', 'common_mistakes'):
            raw = request.form.get(field, '').strip()
            if raw:
                try:
                    setattr(topic, field, json.loads(raw))
                except json.JSONDecodeError:
                    flash(f'JSON invalido en {field}', 'warning')
            else:
                setattr(topic, field, None)
        db.session.commit()
        flash('Tema de gramatica actualizado.', 'success')
        return redirect(url_for('admin.grammar_list'))
    return render_template('admin/content_form.html',
        title='Editar Tema de Gramatica',
        action=url_for('admin.grammar_edit', id=id),
        item=topic,
    )


@admin_bp.route('/grammar/<int:id>/delete', methods=['POST'])
def grammar_delete(id):
    topic = GrammarTopicContent.query.get_or_404(id)
    db.session.delete(topic)
    db.session.commit()
    flash('Tema de gramatica eliminado.', 'success')
    return redirect(url_for('admin.grammar_list'))


# ===========================
# WRITING ERROR PATTERNS
# ===========================

@admin_bp.route('/writing-patterns')
def writing_patterns_list():
    patterns = WritingErrorPattern.query.order_by(WritingErrorPattern.pattern_type).all()
    return render_template('admin/content_list.html',
        title='Patrones de Errores de Escritura',
        items=patterns,
        create_url=url_for('admin.writing_pattern_create'),
        edit_url_func=lambda p: url_for('admin.writing_pattern_edit', id=p.id),
        delete_url_func=lambda p: url_for('admin.writing_pattern_delete', id=p.id),
        fields=['pattern_type', 'pattern', 'message', 'level'],
        model_name='WritingErrorPattern',
    )


@admin_bp.route('/writing-patterns/new', methods=['GET', 'POST'])
def writing_pattern_create():
    if request.method == 'POST':
        pattern = WritingErrorPattern(
            pattern_type=request.form['pattern_type'].strip(),
            pattern=request.form['pattern'].strip(),
            message=request.form.get('message', '').strip() or None,
            level=request.form.get('level', '').strip() or None,
            is_active='is_active' in request.form,
        )
        raw_replacements = request.form.get('replacements', '').strip()
        if raw_replacements:
            try:
                pattern.replacements = json.loads(raw_replacements)
            except json.JSONDecodeError:
                flash('JSON invalido en replacements', 'warning')
        db.session.add(pattern)
        db.session.commit()
        flash('Patron de escritura creado.', 'success')
        return redirect(url_for('admin.writing_patterns_list'))
    return render_template('admin/content_form.html',
        title='Nuevo Patron de Escritura',
        action=url_for('admin.writing_pattern_create'),
    )


@admin_bp.route('/writing-patterns/<int:id>/edit', methods=['GET', 'POST'])
def writing_pattern_edit(id):
    pattern = WritingErrorPattern.query.get_or_404(id)
    if request.method == 'POST':
        pattern.pattern_type = request.form['pattern_type'].strip()
        pattern.pattern = request.form['pattern'].strip()
        pattern.message = request.form.get('message', '').strip() or None
        pattern.level = request.form.get('level', '').strip() or None
        pattern.is_active = 'is_active' in request.form
        raw_replacements = request.form.get('replacements', '').strip()
        if raw_replacements:
            try:
                pattern.replacements = json.loads(raw_replacements)
            except json.JSONDecodeError:
                flash('JSON invalido en replacements', 'warning')
        else:
            pattern.replacements = None
        db.session.commit()
        flash('Patron de escritura actualizado.', 'success')
        return redirect(url_for('admin.writing_patterns_list'))
    return render_template('admin/content_form.html',
        title='Editar Patron de Escritura',
        action=url_for('admin.writing_pattern_edit', id=id),
        item=pattern,
    )


@admin_bp.route('/writing-patterns/<int:id>/delete', methods=['POST'])
def writing_pattern_delete(id):
    pattern = WritingErrorPattern.query.get_or_404(id)
    db.session.delete(pattern)
    db.session.commit()
    flash('Patron de escritura eliminado.', 'success')
    return redirect(url_for('admin.writing_patterns_list'))


# ===========================
# WRITING TIPS
# ===========================

@admin_bp.route('/writing-tips')
def writing_tips_list():
    tips = WritingTipContent.query.order_by(WritingTipContent.error_type).all()
    return render_template('admin/content_list.html',
        title='Tips de Escritura',
        items=tips,
        create_url=url_for('admin.writing_tip_create'),
        edit_url_func=lambda t: url_for('admin.writing_tip_edit', id=t.id),
        delete_url_func=lambda t: url_for('admin.writing_tip_delete', id=t.id),
        fields=['error_type', 'title', 'description'],
        model_name='WritingTipContent',
    )


@admin_bp.route('/writing-tips/new', methods=['GET', 'POST'])
def writing_tip_create():
    if request.method == 'POST':
        tip = WritingTipContent(
            error_type=request.form['error_type'].strip(),
            title=request.form['title'].strip(),
            description=request.form.get('description', '').strip() or None,
        )
        for field in ('tips', 'examples'):
            raw = request.form.get(field, '').strip()
            if raw:
                try:
                    setattr(tip, field, json.loads(raw))
                except json.JSONDecodeError:
                    flash(f'JSON invalido en {field}', 'warning')
        db.session.add(tip)
        db.session.commit()
        flash('Tip de escritura creado.', 'success')
        return redirect(url_for('admin.writing_tips_list'))
    return render_template('admin/content_form.html',
        title='Nuevo Tip de Escritura',
        action=url_for('admin.writing_tip_create'),
    )


@admin_bp.route('/writing-tips/<int:id>/edit', methods=['GET', 'POST'])
def writing_tip_edit(id):
    tip = WritingTipContent.query.get_or_404(id)
    if request.method == 'POST':
        tip.error_type = request.form['error_type'].strip()
        tip.title = request.form['title'].strip()
        tip.description = request.form.get('description', '').strip() or None
        for field in ('tips', 'examples'):
            raw = request.form.get(field, '').strip()
            if raw:
                try:
                    setattr(tip, field, json.loads(raw))
                except json.JSONDecodeError:
                    flash(f'JSON invalido en {field}', 'warning')
            else:
                setattr(tip, field, None)
        db.session.commit()
        flash('Tip de escritura actualizado.', 'success')
        return redirect(url_for('admin.writing_tips_list'))
    return render_template('admin/content_form.html',
        title='Editar Tip de Escritura',
        action=url_for('admin.writing_tip_edit', id=id),
        item=tip,
    )


@admin_bp.route('/writing-tips/<int:id>/delete', methods=['POST'])
def writing_tip_delete(id):
    tip = WritingTipContent.query.get_or_404(id)
    db.session.delete(tip)
    db.session.commit()
    flash('Tip de escritura eliminado.', 'success')
    return redirect(url_for('admin.writing_tips_list'))


# ===========================
# SENTENCE PATTERNS
# ===========================

@admin_bp.route('/sentence-patterns')
def sentence_patterns_list():
    items = SentencePatternContent.query.order_by(SentencePatternContent.topic_name).all()
    return render_template('admin/content_list.html',
        title='Patrones de Oraciones',
        items=items,
        create_url=url_for('admin.sentence_pattern_create'),
        edit_url_func=lambda i: url_for('admin.sentence_pattern_edit', id=i.id),
        delete_url_func=lambda i: url_for('admin.sentence_pattern_delete', id=i.id),
        fields=['topic_name'],
        model_name='SentencePatternContent',
    )


@admin_bp.route('/sentence-patterns/new', methods=['GET', 'POST'])
def sentence_pattern_create():
    if request.method == 'POST':
        item = SentencePatternContent(
            topic_name=request.form['topic_name'].strip(),
        )
        raw = request.form.get('patterns', '').strip()
        if raw:
            try:
                item.patterns = json.loads(raw)
            except json.JSONDecodeError:
                flash('JSON invalido en patterns', 'warning')
        db.session.add(item)
        db.session.commit()
        flash('Patron de oraciones creado.', 'success')
        return redirect(url_for('admin.sentence_patterns_list'))
    return render_template('admin/content_form.html',
        title='Nuevo Patron de Oraciones',
        action=url_for('admin.sentence_pattern_create'),
    )


@admin_bp.route('/sentence-patterns/<int:id>/edit', methods=['GET', 'POST'])
def sentence_pattern_edit(id):
    item = SentencePatternContent.query.get_or_404(id)
    if request.method == 'POST':
        item.topic_name = request.form['topic_name'].strip()
        raw = request.form.get('patterns', '').strip()
        if raw:
            try:
                item.patterns = json.loads(raw)
            except json.JSONDecodeError:
                flash('JSON invalido en patterns', 'warning')
        db.session.commit()
        flash('Patron de oraciones actualizado.', 'success')
        return redirect(url_for('admin.sentence_patterns_list'))
    return render_template('admin/content_form.html',
        title='Editar Patron de Oraciones',
        action=url_for('admin.sentence_pattern_edit', id=id),
        item=item,
    )


@admin_bp.route('/sentence-patterns/<int:id>/delete', methods=['POST'])
def sentence_pattern_delete(id):
    item = SentencePatternContent.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    flash('Patron de oraciones eliminado.', 'success')
    return redirect(url_for('admin.sentence_patterns_list'))


# ===========================
# CONCEPT SYNONYMS
# ===========================

@admin_bp.route('/concept-synonyms')
def concept_synonyms_list():
    items = ConceptSynonym.query.order_by(ConceptSynonym.concept_key).all()
    return render_template('admin/content_list.html',
        title='Sinonimos de Conceptos',
        items=items,
        create_url=url_for('admin.concept_synonym_create'),
        edit_url_func=lambda i: url_for('admin.concept_synonym_edit', id=i.id),
        delete_url_func=lambda i: url_for('admin.concept_synonym_delete', id=i.id),
        fields=['concept_key', 'synonyms'],
        model_name='ConceptSynonym',
    )


@admin_bp.route('/concept-synonyms/new', methods=['GET', 'POST'])
def concept_synonym_create():
    if request.method == 'POST':
        item = ConceptSynonym(
            concept_key=request.form['concept_key'].strip(),
        )
        raw = request.form.get('synonyms', '').strip()
        if raw:
            try:
                item.synonyms = json.loads(raw)
            except json.JSONDecodeError:
                flash('JSON invalido en synonyms', 'warning')
        db.session.add(item)
        db.session.commit()
        flash('Sinonimo creado.', 'success')
        return redirect(url_for('admin.concept_synonyms_list'))
    return render_template('admin/content_form.html',
        title='Nuevo Sinonimo de Concepto',
        action=url_for('admin.concept_synonym_create'),
    )


@admin_bp.route('/concept-synonyms/<int:id>/edit', methods=['GET', 'POST'])
def concept_synonym_edit(id):
    item = ConceptSynonym.query.get_or_404(id)
    if request.method == 'POST':
        item.concept_key = request.form['concept_key'].strip()
        raw = request.form.get('synonyms', '').strip()
        if raw:
            try:
                item.synonyms = json.loads(raw)
            except json.JSONDecodeError:
                flash('JSON invalido en synonyms', 'warning')
        db.session.commit()
        flash('Sinonimo actualizado.', 'success')
        return redirect(url_for('admin.concept_synonyms_list'))
    return render_template('admin/content_form.html',
        title='Editar Sinonimo de Concepto',
        action=url_for('admin.concept_synonym_edit', id=id),
        item=item,
    )


@admin_bp.route('/concept-synonyms/<int:id>/delete', methods=['POST'])
def concept_synonym_delete(id):
    item = ConceptSynonym.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    flash('Sinonimo eliminado.', 'success')
    return redirect(url_for('admin.concept_synonyms_list'))


# ===========================
# ERROR TIPS
# ===========================

@admin_bp.route('/error-tips')
def error_tips_list():
    items = ErrorTipContent.query.order_by(ErrorTipContent.category).all()
    return render_template('admin/content_list.html',
        title='Tips por Error',
        items=items,
        create_url=url_for('admin.error_tip_create'),
        edit_url_func=lambda i: url_for('admin.error_tip_edit', id=i.id),
        delete_url_func=lambda i: url_for('admin.error_tip_delete', id=i.id),
        fields=['category', 'error_type'],
        model_name='ErrorTipContent',
    )


@admin_bp.route('/error-tips/new', methods=['GET', 'POST'])
def error_tip_create():
    if request.method == 'POST':
        item = ErrorTipContent(
            category=request.form['category'].strip(),
            error_type=request.form['error_type'].strip(),
        )
        raw = request.form.get('tips', '').strip()
        if raw:
            try:
                item.tips = json.loads(raw)
            except json.JSONDecodeError:
                flash('JSON invalido en tips', 'warning')
        db.session.add(item)
        db.session.commit()
        flash('Tip de error creado.', 'success')
        return redirect(url_for('admin.error_tips_list'))
    return render_template('admin/content_form.html',
        title='Nuevo Tip de Error',
        action=url_for('admin.error_tip_create'),
    )


@admin_bp.route('/error-tips/<int:id>/edit', methods=['GET', 'POST'])
def error_tip_edit(id):
    item = ErrorTipContent.query.get_or_404(id)
    if request.method == 'POST':
        item.category = request.form['category'].strip()
        item.error_type = request.form['error_type'].strip()
        raw = request.form.get('tips', '').strip()
        if raw:
            try:
                item.tips = json.loads(raw)
            except json.JSONDecodeError:
                flash('JSON invalido en tips', 'warning')
        db.session.commit()
        flash('Tip de error actualizado.', 'success')
        return redirect(url_for('admin.error_tips_list'))
    return render_template('admin/content_form.html',
        title='Editar Tip de Error',
        action=url_for('admin.error_tip_edit', id=id),
        item=item,
    )


@admin_bp.route('/error-tips/<int:id>/delete', methods=['POST'])
def error_tip_delete(id):
    item = ErrorTipContent.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    flash('Tip de error eliminado.', 'success')
    return redirect(url_for('admin.error_tips_list'))


# ===========================
# ACHIEVEMENT MILESTONES
# ===========================

@admin_bp.route('/milestones')
def milestones_list():
    items = AchievementMilestone.query.order_by(AchievementMilestone.threshold).all()
    return render_template('admin/content_list.html',
        title='Hitos de Logros',
        items=items,
        create_url=url_for('admin.milestone_create'),
        edit_url_func=lambda i: url_for('admin.milestone_edit', id=i.id),
        delete_url_func=lambda i: url_for('admin.milestone_delete', id=i.id),
        fields=['name', 'milestone_type', 'threshold', 'icon'],
        model_name='AchievementMilestone',
    )


@admin_bp.route('/milestones/new', methods=['GET', 'POST'])
def milestone_create():
    if request.method == 'POST':
        item = AchievementMilestone(
            name=request.form['name'].strip(),
            milestone_type=request.form['milestone_type'].strip(),
            threshold=int(request.form['threshold']),
            description=request.form.get('description', '').strip() or None,
            icon=request.form.get('icon', '').strip() or None,
            is_active='is_active' in request.form,
        )
        db.session.add(item)
        db.session.commit()
        flash('Hito creado.', 'success')
        return redirect(url_for('admin.milestones_list'))
    return render_template('admin/content_form.html',
        title='Nuevo Hito de Logro',
        action=url_for('admin.milestone_create'),
    )


@admin_bp.route('/milestones/<int:id>/edit', methods=['GET', 'POST'])
def milestone_edit(id):
    item = AchievementMilestone.query.get_or_404(id)
    if request.method == 'POST':
        item.name = request.form['name'].strip()
        item.milestone_type = request.form['milestone_type'].strip()
        item.threshold = int(request.form['threshold'])
        item.description = request.form.get('description', '').strip() or None
        item.icon = request.form.get('icon', '').strip() or None
        item.is_active = 'is_active' in request.form
        db.session.commit()
        flash('Hito actualizado.', 'success')
        return redirect(url_for('admin.milestones_list'))
    return render_template('admin/content_form.html',
        title='Editar Hito de Logro',
        action=url_for('admin.milestone_edit', id=id),
        item=item,
    )


@admin_bp.route('/milestones/<int:id>/delete', methods=['POST'])
def milestone_delete(id):
    item = AchievementMilestone.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    flash('Hito eliminado.', 'success')
    return redirect(url_for('admin.milestones_list'))


# ===========================
# USER MANAGEMENT
# ===========================

@admin_bp.route('/users')
def users_list():
    search = request.args.get('q', '').strip()
    query = User.query
    if search:
        like = f'%{search}%'
        query = query.filter(
            db.or_(
                User.username.ilike(like),
                User.email.ilike(like),
                User.full_name.ilike(like),
            )
        )
    users = query.order_by(User.created_at.desc()).all()
    return render_template('admin/users_list.html', users=users, search=search)


@admin_bp.route('/users/<int:id>')
def user_detail(id):
    user = User.query.get_or_404(id)
    progress = user.progress.all()
    quiz_subs = UserQuizSubmission.query.filter_by(user_id=id).order_by(desc(UserQuizSubmission.id)).limit(20).all()
    writing_subs = UserWritingSubmission.query.filter_by(user_id=id).order_by(desc(UserWritingSubmission.id)).limit(20).all()
    study_results = StudyExerciseResult.query.filter_by(user_id=id).order_by(desc(StudyExerciseResult.id)).limit(20).all()
    streak = UserStreak.query.filter_by(user_id=id).first()
    return render_template('admin/user_detail.html',
        user=user,
        progress=progress,
        quiz_subs=quiz_subs,
        writing_subs=writing_subs,
        study_results=study_results,
        streak=streak,
    )


@admin_bp.route('/users/<int:id>/toggle-admin', methods=['POST'])
def user_toggle_admin(id):
    user = User.query.get_or_404(id)
    if user.id == current_user.id:
        flash('No puedes cambiarte el rol a ti mismo.', 'warning')
        return redirect(url_for('admin.user_detail', id=id))
    user.is_admin = not user.is_admin
    db.session.commit()
    state = 'ahora es administrador' if user.is_admin else 'ya no es administrador'
    flash(f'{user.username} {state}.', 'success')
    return redirect(url_for('admin.user_detail', id=id))


@admin_bp.route('/users/<int:id>/toggle-active', methods=['POST'])
def user_toggle_active(id):
    user = User.query.get_or_404(id)
    user.is_active = not user.is_active
    db.session.commit()
    state = 'activado' if user.is_active else 'desactivado'
    flash(f'{user.username} {state}.', 'success')
    return redirect(url_for('admin.user_detail', id=id))


@admin_bp.route('/users/<int:id>/set-subscription', methods=['POST'])
def user_set_subscription(id):
    user = User.query.get_or_404(id)
    sub = request.form.get('subscription_type', 'free')
    user.subscription_type = sub
    db.session.commit()
    flash(f'Suscripcion de {user.username} cambiada a {sub}.', 'success')
    return redirect(url_for('admin.user_detail', id=id))


# ===========================
# STUDENT RESULTS
# ===========================

@admin_bp.route('/results')
def results_overview():
    recent_quizzes = UserQuizSubmission.query.order_by(desc(UserQuizSubmission.id)).limit(30).all()
    recent_writings = UserWritingSubmission.query.order_by(desc(UserWritingSubmission.id)).limit(30).all()
    recent_study = StudyExerciseResult.query.order_by(desc(StudyExerciseResult.id)).limit(30).all()

    quiz_avg = db.session.query(func.avg(UserQuizSubmission.score)).scalar() or 0
    quiz_count = UserQuizSubmission.query.count()
    writing_count = UserWritingSubmission.query.count()
    study_count = StudyExerciseResult.query.count()

    return render_template('admin/results.html',
        recent_quizzes=recent_quizzes,
        recent_writings=recent_writings,
        recent_study=recent_study,
        quiz_avg=quiz_avg,
        quiz_count=quiz_count,
        writing_count=writing_count,
        study_count=study_count,
    )
