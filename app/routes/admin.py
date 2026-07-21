"""
Panel de Administracion
======================
CRUD de contenido, gestion de usuarios y resultados de estudiantes.
"""

import json
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app.extensions import db
from app.models import (
    User, UserProgress, UserQuizSubmission, UserWritingSubmission,
    UserReadingSubmission, StudyExerciseResult, UserStreak,
    StudyTopicContent, GrammarTopicContent, SentencePatternContent,
    WritingErrorPattern, WritingTipContent, ConceptSynonym,
    ErrorTipContent, AchievementMilestone,
    Unit, Topic, Quiz, QuizQuestion, QuizOption,
    GrammarRule, WritingPractice, Reading, Flashcard,
    MiniGame, MiniGameContent, QuickQuiz,
    ReadingComprehension, ReadingQuestion, SpeedTyping,
    UserGameScore, UserQuizScore, UserReadingScore, UserTypingScore,
    VocabularyCategory, VocabularyItem,
    UnitChallenge, ChallengeQuestion, UnitExplanation, TopicExplanation,
    ThematicScenario, ScenarioVocabulary, ScenarioPhrase,
)
from sqlalchemy import func, desc

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')


@admin_bp.before_request
def before_request():
    if not current_user.is_authenticated:
        return redirect(url_for('auth.login'))
    if not current_user.is_admin:
        flash('Acceso denegado.', 'danger')
        return redirect(url_for('main.index'))


def _parse_json(field_name, default=None):
    raw = request.form.get(field_name, '').strip()
    if not raw:
        return default
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        flash(f'JSON invalido en {field_name}', 'warning')
        return default


def _paginate_and_search(query, search_fields=None, per_page=10):
    """Apply search filtering and pagination to a query."""
    q = request.args.get('q', '').strip()
    if q and search_fields:
        filters = []
        for field_name in search_fields:
            field = getattr(query.column_descriptions[0]['type'], field_name, None)
            if field is not None:
                filters.append(field.ilike(f'%{q}%'))
        if filters:
            from sqlalchemy import or_
            query = query.filter(or_(*filters))
    
    # Preserve existing filters (unit_id, game_type, etc.)
    for key in ['unit_id', 'game_type']:
        val = request.args.get(key)
        if val:
            col = getattr(query.column_descriptions[0]['type'], key, None)
            if col is not None:
                query = query.filter(col == val)
    
    page = request.args.get('page', 1, type=int)
    return query.paginate(page=page, per_page=per_page, error_out=False)


# Model map for bulk actions
_MODEL_MAP = {
    'Unit': Unit, 'Topic': Topic, 'Quiz': Quiz, 'GrammarRule': GrammarRule,
    'VocabularyCategory': VocabularyCategory, 'VocabularyItem': VocabularyItem,
    'WritingPractice': WritingPractice, 'Reading': Reading,
    'UnitChallenge': UnitChallenge, 'ChallengeQuestion': ChallengeQuestion,
    'MiniGame': MiniGame, 'MiniGameContent': MiniGameContent,
    'QuickQuiz': QuickQuiz, 'ReadingComprehension': ReadingComprehension,
    'ReadingQuestion': ReadingQuestion, 'SpeedTyping': SpeedTyping,
    'StudyTopicContent': StudyTopicContent, 'GrammarTopicContent': GrammarTopicContent,
    'WritingErrorPattern': WritingErrorPattern, 'WritingTipContent': WritingTipContent,
    'SentencePatternContent': SentencePatternContent, 'ConceptSynonym': ConceptSynonym,
    'ErrorTipContent': ErrorTipContent, 'AchievementMilestone': AchievementMilestone,
    'ThematicScenario': ThematicScenario,
}


@admin_bp.route('/bulk-action', methods=['POST'])
def bulk_action():
    model_name = request.form.get('model', '')
    action = request.form.get('action', '')
    ids = request.form.getlist('ids')
    redirect_url = request.form.get('redirect', url_for('admin.dashboard'))
    
    if not ids or not action or model_name not in _MODEL_MAP:
        flash('Selecciona registros y una accion.', 'warning')
        return redirect(redirect_url)
    
    model = _MODEL_MAP[model_name]
    items = model.query.filter(model.id.in_([int(i) for i in ids])).all()
    count = len(items)
    
    if action == 'delete':
        for item in items:
            db.session.delete(item)
        db.session.commit()
        flash(f'{count} registro(s) eliminado(s).', 'success')
    elif action == 'activate':
        for item in items:
            if hasattr(item, 'is_active'):
                item.is_active = True
        db.session.commit()
        flash(f'{count} registro(s) activado(s).', 'success')
    elif action == 'deactivate':
        for item in items:
            if hasattr(item, 'is_active'):
                item.is_active = False
        db.session.commit()
        flash(f'{count} registro(s) desactivado(s).', 'success')
    
    return redirect(redirect_url)


# ===========================
# DASHBOARD
# ===========================

@admin_bp.route('/')
def dashboard():
    content_stats = {
        'units': Unit.query.count(),
        'topics': Topic.query.count(),
        'quizzes': Quiz.query.count(),
        'grammar_rules': GrammarRule.query.count(),
        'writing_practices': WritingPractice.query.count(),
        'readings': Reading.query.count(),
        'flashcards': Flashcard.query.count(),
        'study_topics': StudyTopicContent.query.count(),
        'grammar_topics': GrammarTopicContent.query.count(),
        'sentence_patterns': SentencePatternContent.query.count(),
        'writing_patterns': WritingErrorPattern.query.count(),
        'writing_tips': WritingTipContent.query.count(),
        'concept_synonyms': ConceptSynonym.query.count(),
        'error_tips': ErrorTipContent.query.count(),
        'milestones': AchievementMilestone.query.count(),
        'scenarios': ThematicScenario.query.count(),
    }
    return render_template('admin/dashboard.html',
        total_users=User.query.count(),
        active_users=User.query.filter(User.last_login_date.isnot(None)).count(),
        premium_users=User.query.filter(User.subscription_type != 'free').count(),
        admin_users=User.query.filter_by(is_admin=True).count(),
        total_quizzes=UserQuizSubmission.query.count(),
        total_writings=UserWritingSubmission.query.count(),
        total_readings=UserReadingSubmission.query.count(),
        total_study=StudyExerciseResult.query.count(),
        recent_users=User.query.order_by(desc(User.created_at)).limit(10).all(),
        content_stats=content_stats,
    )


# ===========================
# UNITS
# ===========================

@admin_bp.route('/units')
def units_list():
    query = Unit.query.order_by(Unit.unit_number)
    items = _paginate_and_search(query, search_fields=['title', 'description'])
    return render_template('admin/content_list.html',
        title='Unidades', items=items,
        create_url=url_for('admin.unit_create'),
        edit_url_func=lambda i: url_for('admin.unit_detail', id=i.id),
        delete_url_func=lambda i: url_for('admin.unit_delete', id=i.id),
        fields=['unit_number', 'title', 'description'], model_name='Unit')


@admin_bp.route('/units/new', methods=['GET', 'POST'])
def unit_create():
    if request.method == 'POST':
        item = Unit(
            unit_number=int(request.form['unit_number']),
            title=request.form['title'].strip(),
            description=request.form.get('description', '').strip() or None,
            detailed_explanation=request.form.get('detailed_explanation', '').strip() or None,
            overview=request.form.get('overview', '').strip() or None,
            learning_objectives=_parse_json('learning_objectives'),
            created_by=current_user.id,
        )
        db.session.add(item)
        db.session.commit()
        flash('Unidad creada.', 'success')
        return redirect(url_for('admin.units_list'))
    return render_template('admin/content_form.html',
        title='Nueva Unidad', action=url_for('admin.unit_create'), model_name='Unit')


@admin_bp.route('/units/<int:id>/edit', methods=['GET', 'POST'])
def unit_edit(id):
    item = Unit.query.get_or_404(id)
    if request.method == 'POST':
        item.unit_number = int(request.form['unit_number'])
        item.title = request.form['title'].strip()
        item.description = request.form.get('description', '').strip() or None
        item.detailed_explanation = request.form.get('detailed_explanation', '').strip() or None
        item.overview = request.form.get('overview', '').strip() or None
        item.learning_objectives = _parse_json('learning_objectives')
        item.updated_by = current_user.id
        db.session.commit()
        flash('Unidad actualizada.', 'success')
        return redirect(url_for('admin.units_list'))
    return render_template('admin/content_form.html',
        title='Editar Unidad', action=url_for('admin.unit_edit', id=id), item=item)


@admin_bp.route('/units/<int:id>/delete', methods=['POST'])
def unit_delete(id):
    item = Unit.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    flash('Unidad eliminada.', 'success')
    return redirect(url_for('admin.units_list'))


@admin_bp.route('/units/<int:id>')
def unit_detail(id):
    unit = Unit.query.get_or_404(id)
    return render_template('admin/unit_detail.html', unit=unit,
        topics=unit.topics.all(),
        grammar_rules=unit.grammar_rules.all(),
        vocab_categories=unit.vocabulary_categories.all(),
        writing_practices=unit.writing_practices.all(),
        readings=unit.readings,
        explanations=unit.explanations.all(),
        quizzes=unit.quizzes,
        challenges=UnitChallenge.query.filter_by(unit_id=id).all(),
    )


# ===========================
# VOCABULARY CATEGORIES + ITEMS
# ===========================

@admin_bp.route('/vocab-categories')
def vocab_categories_list():
    query = VocabularyCategory.query.order_by(VocabularyCategory.unit_id, VocabularyCategory.order)
    items = _paginate_and_search(query, search_fields=['category_name', 'description'])
    return render_template('admin/content_list.html',
        title='Categorias de Vocabulario', items=items,
        create_url=url_for('admin.vocab_category_create'),
        edit_url_func=lambda i: url_for('admin.vocab_category_edit', id=i.id),
        delete_url_func=lambda i: url_for('admin.vocab_category_delete', id=i.id),
        fields=['category_name', 'unit_id', 'order'],
        filter_options={'unit_id': Unit.query.order_by(Unit.unit_number).all()},
        model_name='VocabularyCategory')


@admin_bp.route('/vocab-categories/new', methods=['GET', 'POST'])
def vocab_category_create():
    if request.method == 'POST':
        item = VocabularyCategory(
            unit_id=int(request.form['unit_id']),
            category_name=request.form['category_name'].strip(),
            description=request.form.get('description', '').strip() or None,
            order=int(request.form.get('order', 0)),
            created_by=current_user.id,
        )
        db.session.add(item)
        db.session.commit()
        flash('Categoria creada.', 'success')
        return redirect(url_for('admin.vocab_categories_list'))
    units = Unit.query.order_by(Unit.unit_number).all()
    return render_template('admin/content_form.html',
        title='Nueva Categoria de Vocabulario', action=url_for('admin.vocab_category_create'), units=units, model_name='VocabularyCategory')


@admin_bp.route('/vocab-categories/<int:id>/edit', methods=['GET', 'POST'])
def vocab_category_edit(id):
    item = VocabularyCategory.query.get_or_404(id)
    if request.method == 'POST':
        item.unit_id = int(request.form['unit_id'])
        item.category_name = request.form['category_name'].strip()
        item.description = request.form.get('description', '').strip() or None
        item.order = int(request.form.get('order', 0))
        item.updated_by = current_user.id
        db.session.commit()
        flash('Categoria actualizada.', 'success')
        return redirect(url_for('admin.vocab_categories_list'))
    units = Unit.query.order_by(Unit.unit_number).all()
    return render_template('admin/content_form.html',
        title='Editar Categoria', action=url_for('admin.vocab_category_edit', id=id), item=item, units=units)


@admin_bp.route('/vocab-categories/<int:id>/delete', methods=['POST'])
def vocab_category_delete(id):
    item = VocabularyCategory.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    flash('Categoria eliminada.', 'success')
    return redirect(url_for('admin.vocab_categories_list'))


@admin_bp.route('/vocab-categories/<int:cat_id>/items')
def vocab_items_list(cat_id):
    cat = VocabularyCategory.query.get_or_404(cat_id)
    query = VocabularyItem.query.filter_by(category_id=cat_id)
    items = _paginate_and_search(query, search_fields=['word', 'definition'])
    return render_template('admin/content_list.html',
        title=f'Vocabulario: {cat.category_name}', items=items,
        create_url=url_for('admin.vocab_item_create', cat_id=cat_id),
        edit_url_func=lambda i: url_for('admin.vocab_item_edit', cat_id=cat_id, id=i.id),
        delete_url_func=lambda i: url_for('admin.vocab_item_delete', cat_id=cat_id, id=i.id),
        fields=['word', 'definition', 'example', 'pronunciation', 'order'],
        back_url=url_for('admin.vocab_categories_list'),
        model_name='VocabularyItem')


@admin_bp.route('/vocab-categories/<int:cat_id>/items/new', methods=['GET', 'POST'])
def vocab_item_create(cat_id):
    cat = VocabularyCategory.query.get_or_404(cat_id)
    if request.method == 'POST':
        item = VocabularyItem(
            category_id=cat_id,
            word=request.form['word'].strip(),
            definition=request.form['definition'].strip(),
            example=request.form.get('example', '').strip() or None,
            pronunciation=request.form.get('pronunciation', '').strip() or None,
            order=int(request.form.get('order', 0)),
        )
        db.session.add(item)
        db.session.commit()
        flash('Palabra creada.', 'success')
        return redirect(url_for('admin.vocab_items_list', cat_id=cat_id))
    return render_template('admin/content_form.html',
        title=f'Nueva Palabra - {cat.category_name}', action=url_for('admin.vocab_item_create', cat_id=cat_id), model_name='VocabularyItem')


@admin_bp.route('/vocab-categories/<int:cat_id>/items/<int:id>/edit', methods=['GET', 'POST'])
def vocab_item_edit(cat_id, id):
    item = VocabularyItem.query.get_or_404(id)
    if request.method == 'POST':
        item.word = request.form['word'].strip()
        item.definition = request.form['definition'].strip()
        item.example = request.form.get('example', '').strip() or None
        item.pronunciation = request.form.get('pronunciation', '').strip() or None
        item.order = int(request.form.get('order', 0))
        db.session.commit()
        flash('Palabra actualizada.', 'success')
        return redirect(url_for('admin.vocab_items_list', cat_id=cat_id))
    return render_template('admin/content_form.html',
        title='Editar Palabra', action=url_for('admin.vocab_item_edit', cat_id=cat_id, id=id), item=item)


@admin_bp.route('/vocab-categories/<int:cat_id>/items/<int:id>/delete', methods=['POST'])
def vocab_item_delete(cat_id, id):
    item = VocabularyItem.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    flash('Palabra eliminada.', 'success')
    return redirect(url_for('admin.vocab_items_list', cat_id=cat_id))


# ===========================
# WRITING PRACTICES (per unit)
# ===========================

@admin_bp.route('/writing-practices')
def writing_practices_list():
    query = WritingPractice.query.order_by(WritingPractice.unit_id, WritingPractice.order)
    items = _paginate_and_search(query, search_fields=['title', 'instructions'])
    return render_template('admin/content_list.html',
        title='Practicas de Escritura', items=items,
        create_url=url_for('admin.writing_practice_create'),
        edit_url_func=lambda i: url_for('admin.writing_practice_edit', id=i.id),
        delete_url_func=lambda i: url_for('admin.writing_practice_delete', id=i.id),
        fields=['title', 'unit_id', 'difficulty', 'order'],
        filter_options={'unit_id': Unit.query.order_by(Unit.unit_number).all()},
        model_name='WritingPractice')


@admin_bp.route('/writing-practices/new', methods=['GET', 'POST'])
def writing_practice_create():
    if request.method == 'POST':
        item = WritingPractice(
            unit_id=int(request.form['unit_id']),
            title=request.form['title'].strip(),
            instructions=request.form['instructions'].strip(),
            example_text=request.form['example_text'].strip(),
            difficulty=request.form.get('difficulty', 'intermediate'),
            order=int(request.form.get('order', 0)),
            created_by=current_user.id,
        )
        db.session.add(item)
        db.session.commit()
        flash('Practica de escritura creada.', 'success')
        return redirect(url_for('admin.writing_practices_list'))
    units = Unit.query.order_by(Unit.unit_number).all()
    return render_template('admin/content_form.html',
        title='Nueva Practica de Escritura', action=url_for('admin.writing_practice_create'), units=units, model_name='WritingPractice')


@admin_bp.route('/writing-practices/<int:id>/edit', methods=['GET', 'POST'])
def writing_practice_edit(id):
    item = WritingPractice.query.get_or_404(id)
    if request.method == 'POST':
        item.unit_id = int(request.form['unit_id'])
        item.title = request.form['title'].strip()
        item.instructions = request.form['instructions'].strip()
        item.example_text = request.form['example_text'].strip()
        item.difficulty = request.form.get('difficulty', 'intermediate')
        item.order = int(request.form.get('order', 0))
        item.updated_by = current_user.id
        db.session.commit()
        flash('Practica actualizada.', 'success')
        return redirect(url_for('admin.writing_practices_list'))
    units = Unit.query.order_by(Unit.unit_number).all()
    return render_template('admin/content_form.html',
        title='Editar Practica de Escritura', action=url_for('admin.writing_practice_edit', id=id), item=item, units=units)


@admin_bp.route('/writing-practices/<int:id>/delete', methods=['POST'])
def writing_practice_delete(id):
    item = WritingPractice.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    flash('Practica eliminada.', 'success')
    return redirect(url_for('admin.writing_practices_list'))


# ===========================
# READINGS (per unit)
# ===========================

@admin_bp.route('/unit-readings')
def unit_readings_list():
    query = Reading.query.order_by(Reading.unit_id, Reading.order)
    items = _paginate_and_search(query, search_fields=['title', 'content'])
    return render_template('admin/content_list.html',
        title='Lecturas por Unidad', items=items,
        create_url=url_for('admin.unit_reading_create'),
        edit_url_func=lambda i: url_for('admin.unit_reading_edit', id=i.id),
        delete_url_func=lambda i: url_for('admin.unit_reading_delete', id=i.id),
        fields=['title', 'unit_id', 'difficulty', 'order'],
        filter_options={'unit_id': Unit.query.order_by(Unit.unit_number).all()},
        model_name='Reading')


@admin_bp.route('/unit-readings/new', methods=['GET', 'POST'])
def unit_reading_create():
    if request.method == 'POST':
        item = Reading(
            unit_id=int(request.form['unit_id']),
            title=request.form['title'].strip(),
            content=request.form['content'].strip(),
            difficulty=request.form.get('difficulty', 'intermediate'),
            instructions=request.form.get('instructions', '').strip() or None,
            order=int(request.form.get('order', 0)),
            created_by=current_user.id,
        )
        db.session.add(item)
        db.session.commit()
        flash('Lectura creada.', 'success')
        return redirect(url_for('admin.unit_readings_list'))
    units = Unit.query.order_by(Unit.unit_number).all()
    return render_template('admin/content_form.html',
        title='Nueva Lectura (Unidad)', action=url_for('admin.unit_reading_create'), units=units, model_name='Reading')


@admin_bp.route('/unit-readings/<int:id>/edit', methods=['GET', 'POST'])
def unit_reading_edit(id):
    item = Reading.query.get_or_404(id)
    if request.method == 'POST':
        item.unit_id = int(request.form['unit_id'])
        item.title = request.form['title'].strip()
        item.content = request.form['content'].strip()
        item.difficulty = request.form.get('difficulty', 'intermediate')
        item.instructions = request.form.get('instructions', '').strip() or None
        item.order = int(request.form.get('order', 0))
        item.updated_by = current_user.id
        db.session.commit()
        flash('Lectura actualizada.', 'success')
        return redirect(url_for('admin.unit_readings_list'))
    units = Unit.query.order_by(Unit.unit_number).all()
    return render_template('admin/content_form.html',
        title='Editar Lectura (Unidad)', action=url_for('admin.unit_reading_edit', id=id), item=item, units=units)


@admin_bp.route('/unit-readings/<int:id>/delete', methods=['POST'])
def unit_reading_delete(id):
    item = Reading.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    flash('Lectura eliminada.', 'success')
    return redirect(url_for('admin.unit_readings_list'))


# ===========================
# UNIT CHALLENGES
# ===========================

@admin_bp.route('/challenges')
def challenges_list():
    query = UnitChallenge.query.order_by(UnitChallenge.unit_id)
    items = _paginate_and_search(query, search_fields=['title', 'description'])
    return render_template('admin/content_list.html',
        title='Desafios de Unidad', items=items,
        create_url=url_for('admin.challenge_create'),
        edit_url_func=lambda i: url_for('admin.challenge_edit', id=i.id),
        delete_url_func=lambda i: url_for('admin.challenge_delete', id=i.id),
        fields=['title', 'unit_id', 'passing_score', 'time_limit', 'is_active'],
        filter_options={'unit_id': Unit.query.order_by(Unit.unit_number).all()},
        model_name='UnitChallenge')


@admin_bp.route('/challenges/new', methods=['GET', 'POST'])
def challenge_create():
    if request.method == 'POST':
        item = UnitChallenge(
            unit_id=int(request.form['unit_id']),
            title=request.form['title'].strip(),
            description=request.form.get('description', '').strip() or None,
            passing_score=float(request.form.get('passing_score', 70)),
            time_limit=int(request.form.get('time_limit', 30)),
            max_attempts=int(request.form.get('max_attempts', 3)),
            is_active='is_active' in request.form,
            created_by=current_user.id,
        )
        db.session.add(item)
        db.session.commit()
        flash('Desafio creado.', 'success')
        return redirect(url_for('admin.challenges_list'))
    units = Unit.query.order_by(Unit.unit_number).all()
    return render_template('admin/content_form.html',
        title='Nuevo Desafio', action=url_for('admin.challenge_create'), units=units, model_name='UnitChallenge')


@admin_bp.route('/challenges/<int:id>/edit', methods=['GET', 'POST'])
def challenge_edit(id):
    item = UnitChallenge.query.get_or_404(id)
    if request.method == 'POST':
        item.unit_id = int(request.form['unit_id'])
        item.title = request.form['title'].strip()
        item.description = request.form.get('description', '').strip() or None
        item.passing_score = float(request.form.get('passing_score', 70))
        item.time_limit = int(request.form.get('time_limit', 30))
        item.max_attempts = int(request.form.get('max_attempts', 3))
        item.is_active = 'is_active' in request.form
        item.updated_by = current_user.id
        db.session.commit()
        flash('Desafio actualizado.', 'success')
        return redirect(url_for('admin.challenges_list'))
    units = Unit.query.order_by(Unit.unit_number).all()
    return render_template('admin/content_form.html',
        title='Editar Desafio', action=url_for('admin.challenge_edit', id=id), item=item, units=units)


@admin_bp.route('/challenges/<int:id>/delete', methods=['POST'])
def challenge_delete(id):
    item = UnitChallenge.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    flash('Desafio eliminado.', 'success')
    return redirect(url_for('admin.challenges_list'))


@admin_bp.route('/challenges/<int:challenge_id>/questions')
def challenge_questions_list(challenge_id):
    challenge = UnitChallenge.query.get_or_404(challenge_id)
    query = ChallengeQuestion.query.filter_by(challenge_id=challenge_id).order_by(ChallengeQuestion.order)
    questions = _paginate_and_search(query, search_fields=['question_text'])
    return render_template('admin/challenge_questions.html', challenge=challenge, questions=questions)


@admin_bp.route('/challenges/<int:challenge_id>/questions/new', methods=['GET', 'POST'])
def challenge_question_create(challenge_id):
    challenge = UnitChallenge.query.get_or_404(challenge_id)
    if request.method == 'POST':
        q = ChallengeQuestion(
            challenge_id=challenge_id,
            question_type=request.form['question_type'].strip(),
            question_text=request.form['question_text'].strip(),
            correct_answer=request.form['correct_answer'].strip(),
            options=_parse_json('options'),
            explanation=request.form.get('explanation', '').strip() or None,
            points=int(request.form.get('points', 10)),
            difficulty=request.form.get('difficulty', 'medium'),
            skill_tested=request.form.get('skill_tested', '').strip() or None,
            order=int(request.form.get('order', 0)),
        )
        db.session.add(q)
        db.session.commit()
        flash('Pregunta creada.', 'success')
        return redirect(url_for('admin.challenge_questions_list', challenge_id=challenge_id))
    return render_template('admin/content_form.html',
        title=f'Nueva Pregunta - {challenge.title}', action=url_for('admin.challenge_question_create', challenge_id=challenge_id), model_name='ChallengeQuestion')


@admin_bp.route('/challenges/questions/<int:qid>/edit', methods=['GET', 'POST'])
def challenge_question_edit(qid):
    q = ChallengeQuestion.query.get_or_404(qid)
    if request.method == 'POST':
        q.question_type = request.form['question_type'].strip()
        q.question_text = request.form['question_text'].strip()
        q.correct_answer = request.form['correct_answer'].strip()
        q.options = _parse_json('options')
        q.explanation = request.form.get('explanation', '').strip() or None
        q.points = int(request.form.get('points', 10))
        q.difficulty = request.form.get('difficulty', 'medium')
        q.skill_tested = request.form.get('skill_tested', '').strip() or None
        q.order = int(request.form.get('order', 0))
        db.session.commit()
        flash('Pregunta actualizada.', 'success')
        return redirect(url_for('admin.challenge_questions_list', challenge_id=q.challenge_id))
    return render_template('admin/content_form.html',
        title='Editar Pregunta', action=url_for('admin.challenge_question_edit', qid=qid), item=q)


@admin_bp.route('/challenges/questions/<int:qid>/delete', methods=['POST'])
def challenge_question_delete(qid):
    q = ChallengeQuestion.query.get_or_404(qid)
    cid = q.challenge_id
    db.session.delete(q)
    db.session.commit()
    flash('Pregunta eliminada.', 'success')
    return redirect(url_for('admin.challenge_questions_list', challenge_id=cid))


# ===========================
# TOPICS
# ===========================

@admin_bp.route('/topics')
def topics_list():
    query = Topic.query.order_by(Topic.unit_id, Topic.order)
    items = _paginate_and_search(query, search_fields=['title', 'description'])
    return render_template('admin/content_list.html',
        title='Temas', items=items,
        create_url=url_for('admin.topic_create'),
        edit_url_func=lambda i: url_for('admin.topic_edit', id=i.id),
        delete_url_func=lambda i: url_for('admin.topic_delete', id=i.id),
        fields=['title', 'unit_id', 'order'], model_name='Topic')


@admin_bp.route('/topics/new', methods=['GET', 'POST'])
def topic_create():
    if request.method == 'POST':
        item = Topic(
            unit_id=int(request.form['unit_id']),
            title=request.form['title'].strip(),
            description=request.form.get('description', '').strip() or None,
            detailed_explanation=request.form.get('detailed_explanation', '').strip() or None,
            order=int(request.form.get('order', 0)),
            key_concepts=_parse_json('key_concepts'),
            common_mistakes=_parse_json('common_mistakes'),
            tips=_parse_json('tips'),
            examples=_parse_json('examples'),
            created_by=current_user.id,
        )
        db.session.add(item)
        db.session.commit()
        flash('Tema creado.', 'success')
        return redirect(url_for('admin.topics_list'))
    units = Unit.query.order_by(Unit.unit_number).all()
    return render_template('admin/content_form.html',
        title='Nuevo Tema', action=url_for('admin.topic_create'), units=units, model_name='Topic')


@admin_bp.route('/topics/<int:id>/edit', methods=['GET', 'POST'])
def topic_edit(id):
    item = Topic.query.get_or_404(id)
    if request.method == 'POST':
        item.unit_id = int(request.form['unit_id'])
        item.title = request.form['title'].strip()
        item.description = request.form.get('description', '').strip() or None
        item.detailed_explanation = request.form.get('detailed_explanation', '').strip() or None
        item.order = int(request.form.get('order', 0))
        item.key_concepts = _parse_json('key_concepts')
        item.common_mistakes = _parse_json('common_mistakes')
        item.tips = _parse_json('tips')
        item.examples = _parse_json('examples')
        item.updated_by = current_user.id
        db.session.commit()
        flash('Tema actualizado.', 'success')
        return redirect(url_for('admin.topics_list'))
    units = Unit.query.order_by(Unit.unit_number).all()
    return render_template('admin/content_form.html',
        title='Editar Tema', action=url_for('admin.topic_edit', id=id), item=item, units=units)


@admin_bp.route('/topics/<int:id>/delete', methods=['POST'])
def topic_delete(id):
    item = Topic.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    flash('Tema eliminado.', 'success')
    return redirect(url_for('admin.topics_list'))


# ===========================
# QUIZZES
# ===========================

@admin_bp.route('/quizzes')
def quizzes_list():
    query = Quiz.query.order_by(Quiz.unit_id)
    items = _paginate_and_search(query, search_fields=['title', 'description'])
    return render_template('admin/content_list.html',
        title='Quizzes', items=items,
        create_url=url_for('admin.quiz_create'),
        edit_url_func=lambda i: url_for('admin.quiz_edit', id=i.id),
        delete_url_func=lambda i: url_for('admin.quiz_delete', id=i.id),
        fields=['title', 'unit_id', 'description'], model_name='Quiz')


@admin_bp.route('/quizzes/new', methods=['GET', 'POST'])
def quiz_create():
    if request.method == 'POST':
        item = Quiz(
            unit_id=int(request.form['unit_id']),
            title=request.form['title'].strip(),
            description=request.form.get('description', '').strip() or None,
            created_by=current_user.id,
        )
        db.session.add(item)
        db.session.commit()
        flash('Quiz creado.', 'success')
        return redirect(url_for('admin.quizzes_list'))
    units = Unit.query.order_by(Unit.unit_number).all()
    return render_template('admin/content_form.html',
        title='Nuevo Quiz', action=url_for('admin.quiz_create'), units=units, model_name='Quiz')


@admin_bp.route('/quizzes/<int:id>/edit', methods=['GET', 'POST'])
def quiz_edit(id):
    item = Quiz.query.get_or_404(id)
    if request.method == 'POST':
        item.unit_id = int(request.form['unit_id'])
        item.title = request.form['title'].strip()
        item.description = request.form.get('description', '').strip() or None
        item.updated_by = current_user.id
        db.session.commit()
        flash('Quiz actualizado.', 'success')
        return redirect(url_for('admin.quizzes_list'))
    units = Unit.query.order_by(Unit.unit_number).all()
    return render_template('admin/content_form.html',
        title='Editar Quiz', action=url_for('admin.quiz_edit', id=id), item=item, units=units)


@admin_bp.route('/quizzes/<int:id>/delete', methods=['POST'])
def quiz_delete(id):
    item = Quiz.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    flash('Quiz eliminado.', 'success')
    return redirect(url_for('admin.quizzes_list'))


@admin_bp.route('/quizzes/<int:quiz_id>/questions')
def quiz_questions_list(quiz_id):
    quiz = Quiz.query.get_or_404(quiz_id)
    query = QuizQuestion.query.filter_by(quiz_id=quiz_id).order_by(QuizQuestion.order)
    questions = _paginate_and_search(query, search_fields=['prompt'])
    return render_template('admin/quiz_questions.html', quiz=quiz, questions=questions)


@admin_bp.route('/quizzes/<int:quiz_id>/questions/new', methods=['GET', 'POST'])
def quiz_question_create(quiz_id):
    quiz = Quiz.query.get_or_404(quiz_id)
    if request.method == 'POST':
        q = QuizQuestion(quiz_id=quiz_id, prompt=request.form['prompt'].strip(),
                         order=int(request.form.get('order', 0)))
        db.session.add(q)
        db.session.flush()
        for i in range(1, 5):
            text = request.form.get(f'option_{i}', '').strip()
            if text:
                db.session.add(QuizOption(question_id=q.id, text=text,
                    is_correct=(request.form.get('correct_option') == str(i)), order=i))
        db.session.commit()
        flash('Pregunta creada.', 'success')
        return redirect(url_for('admin.quiz_questions_list', quiz_id=quiz_id))
    return render_template('admin/quiz_question_form.html', quiz=quiz,
        action=url_for('admin.quiz_question_create', quiz_id=quiz_id))


@admin_bp.route('/quizzes/<int:quiz_id>/questions/<int:qid>/edit', methods=['GET', 'POST'])
def quiz_question_edit(quiz_id, qid):
    quiz = Quiz.query.get_or_404(quiz_id)
    question = QuizQuestion.query.get_or_404(qid)
    if request.method == 'POST':
        question.prompt = request.form['prompt'].strip()
        question.order = int(request.form.get('order', 0))
        QuizOption.query.filter_by(question_id=qid).delete()
        for i in range(1, 5):
            text = request.form.get(f'option_{i}', '').strip()
            if text:
                db.session.add(QuizOption(question_id=qid, text=text,
                    is_correct=(request.form.get('correct_option') == str(i)), order=i))
        db.session.commit()
        flash('Pregunta actualizada.', 'success')
        return redirect(url_for('admin.quiz_questions_list', quiz_id=quiz_id))
    existing = QuizOption.query.filter_by(question_id=qid).order_by(QuizOption.order).all()
    return render_template('admin/quiz_question_form.html', quiz=quiz, question=question,
        existing_options=existing, action=url_for('admin.quiz_question_edit', quiz_id=quiz_id, qid=qid))


@admin_bp.route('/quizzes/<int:quiz_id>/questions/<int:qid>/delete', methods=['POST'])
def quiz_question_delete(quiz_id, qid):
    question = QuizQuestion.query.get_or_404(qid)
    db.session.delete(question)
    db.session.commit()
    flash('Pregunta eliminada.', 'success')
    return redirect(url_for('admin.quiz_questions_list', quiz_id=quiz_id))


# ===========================
# GRAMMAR RULES
# ===========================

@admin_bp.route('/grammar-rules')
def grammar_rules_list():
    query = GrammarRule.query.order_by(GrammarRule.unit_id, GrammarRule.order)
    items = _paginate_and_search(query, search_fields=['topic', 'rule'])
    return render_template('admin/content_list.html',
        title='Reglas Gramaticales', items=items,
        create_url=url_for('admin.grammar_rule_create'),
        edit_url_func=lambda i: url_for('admin.grammar_rule_edit', id=i.id),
        delete_url_func=lambda i: url_for('admin.grammar_rule_delete', id=i.id),
        fields=['topic', 'unit_id', 'rule', 'order'], model_name='GrammarRule')


@admin_bp.route('/grammar-rules/new', methods=['GET', 'POST'])
def grammar_rule_create():
    if request.method == 'POST':
        item = GrammarRule(
            unit_id=int(request.form['unit_id']),
            topic=request.form['topic'].strip(),
            rule=request.form['rule'].strip(),
            detailed_explanation=request.form.get('detailed_explanation', '').strip() or None,
            example=request.form.get('example', '').strip() or None,
            exceptions=request.form.get('exceptions', '').strip() or None,
            order=int(request.form.get('order', 0)),
            examples=_parse_json('examples'),
            correct_usage=_parse_json('correct_usage'),
            incorrect_usage=_parse_json('incorrect_usage'),
            common_errors=_parse_json('common_errors'),
            created_by=current_user.id,
        )
        db.session.add(item)
        db.session.commit()
        flash('Regla gramatical creada.', 'success')
        return redirect(url_for('admin.grammar_rules_list'))
    units = Unit.query.order_by(Unit.unit_number).all()
    return render_template('admin/content_form.html',
        title='Nueva Regla Gramatical', action=url_for('admin.grammar_rule_create'), units=units, model_name='GrammarRule')


@admin_bp.route('/grammar-rules/<int:id>/edit', methods=['GET', 'POST'])
def grammar_rule_edit(id):
    item = GrammarRule.query.get_or_404(id)
    if request.method == 'POST':
        item.unit_id = int(request.form['unit_id'])
        item.topic = request.form['topic'].strip()
        item.rule = request.form['rule'].strip()
        item.detailed_explanation = request.form.get('detailed_explanation', '').strip() or None
        item.example = request.form.get('example', '').strip() or None
        item.exceptions = request.form.get('exceptions', '').strip() or None
        item.order = int(request.form.get('order', 0))
        item.examples = _parse_json('examples')
        item.correct_usage = _parse_json('correct_usage')
        item.incorrect_usage = _parse_json('incorrect_usage')
        item.common_errors = _parse_json('common_errors')
        item.updated_by = current_user.id
        db.session.commit()
        flash('Regla gramatical actualizada.', 'success')
        return redirect(url_for('admin.grammar_rules_list'))
    units = Unit.query.order_by(Unit.unit_number).all()
    return render_template('admin/content_form.html',
        title='Editar Regla Gramatical', action=url_for('admin.grammar_rule_edit', id=id),
        item=item, units=units)


@admin_bp.route('/grammar-rules/<int:id>/delete', methods=['POST'])
def grammar_rule_delete(id):
    item = GrammarRule.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    flash('Regla gramatical eliminada.', 'success')
    return redirect(url_for('admin.grammar_rules_list'))


# ===========================
# STUDY TOPICS (contenido intensivo)
# ===========================

@admin_bp.route('/study')
def study_list():
    query = StudyTopicContent.query.order_by(StudyTopicContent.id)
    items = _paginate_and_search(query, search_fields=['title', 'slug'])
    return render_template('admin/content_list.html',
        title='Temas de Estudio Intensivo', items=items,
        create_url=url_for('admin.study_create'),
        edit_url_func=lambda t: url_for('admin.study_edit', id=t.id),
        delete_url_func=lambda t: url_for('admin.study_delete', id=t.id),
        fields=['slug', 'title', 'icon', 'difficulty', 'estimated_time'],
        model_name='StudyTopicContent')


@admin_bp.route('/study/new', methods=['GET', 'POST'])
def study_create():
    if request.method == 'POST':
        topic = StudyTopicContent(
            slug=request.form['slug'].strip(), title=request.form['title'].strip(),
            icon=request.form.get('icon', '').strip() or None,
            difficulty=request.form.get('difficulty', '').strip() or None,
            estimated_time=request.form.get('estimated_time', '').strip() or None,
            description=request.form.get('description', '').strip() or None,
            theory=_parse_json('theory'), common_mistakes=_parse_json('common_mistakes'),
            tips=_parse_json('tips'), exercises=_parse_json('exercises'),
            created_by=current_user.id,
        )
        db.session.add(topic)
        db.session.commit()
        flash('Tema de estudio creado.', 'success')
        return redirect(url_for('admin.study_list'))
    return render_template('admin/content_form.html',
        title='Nuevo Tema de Estudio', action=url_for('admin.study_create'), model_name='StudyTopicContent')


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
        topic.theory = _parse_json('theory')
        topic.common_mistakes = _parse_json('common_mistakes')
        topic.tips = _parse_json('tips')
        topic.exercises = _parse_json('exercises')
        topic.updated_by = current_user.id
        db.session.commit()
        flash('Tema de estudio actualizado.', 'success')
        return redirect(url_for('admin.study_list'))
    return render_template('admin/content_form.html',
        title='Editar Tema de Estudio', action=url_for('admin.study_edit', id=id), item=topic)


@admin_bp.route('/study/<int:id>/delete', methods=['POST'])
def study_delete(id):
    topic = StudyTopicContent.query.get_or_404(id)
    db.session.delete(topic)
    db.session.commit()
    flash('Tema de estudio eliminado.', 'success')
    return redirect(url_for('admin.study_list'))


# ===========================
# GRAMMAR TOPICS (contenido referencia)
# ===========================

@admin_bp.route('/grammar')
def grammar_list():
    query = GrammarTopicContent.query.order_by(GrammarTopicContent.id)
    items = _paginate_and_search(query, search_fields=['title', 'slug'])
    return render_template('admin/content_list.html',
        title='Temas de Gramatica', items=items,
        create_url=url_for('admin.grammar_create'),
        edit_url_func=lambda t: url_for('admin.grammar_edit', id=t.id),
        delete_url_func=lambda t: url_for('admin.grammar_delete', id=t.id),
        fields=['slug', 'title', 'level', 'category', 'icon'],
        model_name='GrammarTopicContent')


@admin_bp.route('/grammar/new', methods=['GET', 'POST'])
def grammar_create():
    if request.method == 'POST':
        topic = GrammarTopicContent(
            slug=request.form['slug'].strip(), title=request.form['title'].strip(),
            subtitle=request.form.get('subtitle', '').strip() or None,
            icon=request.form.get('icon', '').strip() or None,
            level=request.form.get('level', '').strip() or None,
            category=request.form.get('category', '').strip() or None,
            description=request.form.get('description', '').strip() or None,
            estimated_time=request.form.get('estimated_time', '').strip() or None,
            sections=_parse_json('sections'), tips=_parse_json('tips'),
            common_mistakes=_parse_json('common_mistakes'),
            created_by=current_user.id,
        )
        db.session.add(topic)
        db.session.commit()
        flash('Tema de gramatica creado.', 'success')
        return redirect(url_for('admin.grammar_list'))
    return render_template('admin/content_form.html',
        title='Nuevo Tema de Gramatica', action=url_for('admin.grammar_create'), model_name='GrammarTopicContent')


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
        topic.sections = _parse_json('sections')
        topic.tips = _parse_json('tips')
        topic.common_mistakes = _parse_json('common_mistakes')
        topic.updated_by = current_user.id
        db.session.commit()
        flash('Tema de gramatica actualizado.', 'success')
        return redirect(url_for('admin.grammar_list'))
    return render_template('admin/content_form.html',
        title='Editar Tema de Gramatica', action=url_for('admin.grammar_edit', id=id), item=topic)


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
    query = WritingErrorPattern.query.order_by(WritingErrorPattern.pattern_type)
    items = _paginate_and_search(query, search_fields=['pattern', 'message'])
    return render_template('admin/content_list.html',
        title='Patrones de Errores de Escritura', items=items,
        create_url=url_for('admin.writing_pattern_create'),
        edit_url_func=lambda p: url_for('admin.writing_pattern_edit', id=p.id),
        delete_url_func=lambda p: url_for('admin.writing_pattern_delete', id=p.id),
        fields=['pattern_type', 'pattern', 'message', 'level'],
        model_name='WritingErrorPattern')


@admin_bp.route('/writing-patterns/new', methods=['GET', 'POST'])
def writing_pattern_create():
    if request.method == 'POST':
        pattern = WritingErrorPattern(
            pattern_type=request.form['pattern_type'].strip(),
            pattern=request.form['pattern'].strip(),
            message=request.form.get('message', '').strip() or None,
            level=request.form.get('level', '').strip() or None,
            is_active='is_active' in request.form,
            replacements=_parse_json('replacements'),
            created_by=current_user.id,
        )
        db.session.add(pattern)
        db.session.commit()
        flash('Patron de escritura creado.', 'success')
        return redirect(url_for('admin.writing_patterns_list'))
    return render_template('admin/content_form.html',
        title='Nuevo Patron de Escritura', action=url_for('admin.writing_pattern_create'), model_name='WritingErrorPattern')


@admin_bp.route('/writing-patterns/<int:id>/edit', methods=['GET', 'POST'])
def writing_pattern_edit(id):
    pattern = WritingErrorPattern.query.get_or_404(id)
    if request.method == 'POST':
        pattern.pattern_type = request.form['pattern_type'].strip()
        pattern.pattern = request.form['pattern'].strip()
        pattern.message = request.form.get('message', '').strip() or None
        pattern.level = request.form.get('level', '').strip() or None
        pattern.is_active = 'is_active' in request.form
        pattern.replacements = _parse_json('replacements')
        pattern.updated_by = current_user.id
        db.session.commit()
        flash('Patron de escritura actualizado.', 'success')
        return redirect(url_for('admin.writing_patterns_list'))
    return render_template('admin/content_form.html',
        title='Editar Patron de Escritura', action=url_for('admin.writing_pattern_edit', id=id), item=pattern)


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
    query = WritingTipContent.query.order_by(WritingTipContent.error_type)
    items = _paginate_and_search(query, search_fields=['title', 'error_type'])
    return render_template('admin/content_list.html',
        title='Tips de Escritura', items=items,
        create_url=url_for('admin.writing_tip_create'),
        edit_url_func=lambda t: url_for('admin.writing_tip_edit', id=t.id),
        delete_url_func=lambda t: url_for('admin.writing_tip_delete', id=t.id),
        fields=['error_type', 'title', 'description'], model_name='WritingTipContent')


@admin_bp.route('/writing-tips/new', methods=['GET', 'POST'])
def writing_tip_create():
    if request.method == 'POST':
        tip = WritingTipContent(
            error_type=request.form['error_type'].strip(),
            title=request.form['title'].strip(),
            description=request.form.get('description', '').strip() or None,
            tips=_parse_json('tips'), examples=_parse_json('examples'),
            created_by=current_user.id,
        )
        db.session.add(tip)
        db.session.commit()
        flash('Tip de escritura creado.', 'success')
        return redirect(url_for('admin.writing_tips_list'))
    return render_template('admin/content_form.html',
        title='Nuevo Tip de Escritura', action=url_for('admin.writing_tip_create'), model_name='WritingTipContent')


@admin_bp.route('/writing-tips/<int:id>/edit', methods=['GET', 'POST'])
def writing_tip_edit(id):
    tip = WritingTipContent.query.get_or_404(id)
    if request.method == 'POST':
        tip.error_type = request.form['error_type'].strip()
        tip.title = request.form['title'].strip()
        tip.description = request.form.get('description', '').strip() or None
        tip.tips = _parse_json('tips')
        tip.examples = _parse_json('examples')
        tip.updated_by = current_user.id
        db.session.commit()
        flash('Tip de escritura actualizado.', 'success')
        return redirect(url_for('admin.writing_tips_list'))
    return render_template('admin/content_form.html',
        title='Editar Tip de Escritura', action=url_for('admin.writing_tip_edit', id=id), item=tip)


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
    query = SentencePatternContent.query.order_by(SentencePatternContent.topic_name)
    items = _paginate_and_search(query, search_fields=['topic_name'])
    return render_template('admin/content_list.html',
        title='Patrones de Oraciones', items=items,
        create_url=url_for('admin.sentence_pattern_create'),
        edit_url_func=lambda i: url_for('admin.sentence_pattern_edit', id=i.id),
        delete_url_func=lambda i: url_for('admin.sentence_pattern_delete', id=i.id),
        fields=['topic_name'], model_name='SentencePatternContent')


@admin_bp.route('/sentence-patterns/new', methods=['GET', 'POST'])
def sentence_pattern_create():
    if request.method == 'POST':
        item = SentencePatternContent(
            topic_name=request.form['topic_name'].strip(),
            patterns=_parse_json('patterns', []),
            created_by=current_user.id,
        )
        db.session.add(item)
        db.session.commit()
        flash('Patron de oraciones creado.', 'success')
        return redirect(url_for('admin.sentence_patterns_list'))
    return render_template('admin/content_form.html',
        title='Nuevo Patron de Oraciones', action=url_for('admin.sentence_pattern_create'), model_name='SentencePatternContent')


@admin_bp.route('/sentence-patterns/<int:id>/edit', methods=['GET', 'POST'])
def sentence_pattern_edit(id):
    item = SentencePatternContent.query.get_or_404(id)
    if request.method == 'POST':
        item.topic_name = request.form['topic_name'].strip()
        item.patterns = _parse_json('patterns', [])
        item.updated_by = current_user.id
        db.session.commit()
        flash('Patron de oraciones actualizado.', 'success')
        return redirect(url_for('admin.sentence_patterns_list'))
    return render_template('admin/content_form.html',
        title='Editar Patron de Oraciones', action=url_for('admin.sentence_pattern_edit', id=id), item=item)


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
    query = ConceptSynonym.query.order_by(ConceptSynonym.concept_key)
    items = _paginate_and_search(query, search_fields=['concept_key'])
    return render_template('admin/content_list.html',
        title='Sinonimos de Conceptos', items=items,
        create_url=url_for('admin.concept_synonym_create'),
        edit_url_func=lambda i: url_for('admin.concept_synonym_edit', id=i.id),
        delete_url_func=lambda i: url_for('admin.concept_synonym_delete', id=i.id),
        fields=['concept_key', 'synonyms'], model_name='ConceptSynonym')


@admin_bp.route('/concept-synonyms/new', methods=['GET', 'POST'])
def concept_synonym_create():
    if request.method == 'POST':
        item = ConceptSynonym(
            concept_key=request.form['concept_key'].strip(),
            synonyms=_parse_json('synonyms', []),
            created_by=current_user.id,
        )
        db.session.add(item)
        db.session.commit()
        flash('Sinonimo creado.', 'success')
        return redirect(url_for('admin.concept_synonyms_list'))
    return render_template('admin/content_form.html',
        title='Nuevo Sinonimo de Concepto', action=url_for('admin.concept_synonym_create'), model_name='ConceptSynonym')


@admin_bp.route('/concept-synonyms/<int:id>/edit', methods=['GET', 'POST'])
def concept_synonym_edit(id):
    item = ConceptSynonym.query.get_or_404(id)
    if request.method == 'POST':
        item.concept_key = request.form['concept_key'].strip()
        item.synonyms = _parse_json('synonyms', [])
        item.updated_by = current_user.id
        db.session.commit()
        flash('Sinonimo actualizado.', 'success')
        return redirect(url_for('admin.concept_synonyms_list'))
    return render_template('admin/content_form.html',
        title='Editar Sinonimo de Concepto', action=url_for('admin.concept_synonym_edit', id=id), item=item)


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
    query = ErrorTipContent.query.order_by(ErrorTipContent.category)
    items = _paginate_and_search(query, search_fields=['category', 'error_type'])
    return render_template('admin/content_list.html',
        title='Tips por Error', items=items,
        create_url=url_for('admin.error_tip_create'),
        edit_url_func=lambda i: url_for('admin.error_tip_edit', id=i.id),
        delete_url_func=lambda i: url_for('admin.error_tip_delete', id=i.id),
        fields=['category', 'error_type'], model_name='ErrorTipContent')


@admin_bp.route('/error-tips/new', methods=['GET', 'POST'])
def error_tip_create():
    if request.method == 'POST':
        item = ErrorTipContent(
            category=request.form['category'].strip(),
            error_type=request.form['error_type'].strip(),
            tips=_parse_json('tips', []),
            created_by=current_user.id,
        )
        db.session.add(item)
        db.session.commit()
        flash('Tip de error creado.', 'success')
        return redirect(url_for('admin.error_tips_list'))
    return render_template('admin/content_form.html',
        title='Nuevo Tip de Error', action=url_for('admin.error_tip_create'), model_name='ErrorTipContent')


@admin_bp.route('/error-tips/<int:id>/edit', methods=['GET', 'POST'])
def error_tip_edit(id):
    item = ErrorTipContent.query.get_or_404(id)
    if request.method == 'POST':
        item.category = request.form['category'].strip()
        item.error_type = request.form['error_type'].strip()
        item.tips = _parse_json('tips', [])
        item.updated_by = current_user.id
        db.session.commit()
        flash('Tip de error actualizado.', 'success')
        return redirect(url_for('admin.error_tips_list'))
    return render_template('admin/content_form.html',
        title='Editar Tip de Error', action=url_for('admin.error_tip_edit', id=id), item=item)


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
    query = AchievementMilestone.query.order_by(AchievementMilestone.threshold)
    items = _paginate_and_search(query, search_fields=['name', 'description'])
    return render_template('admin/content_list.html',
        title='Hitos de Logros', items=items,
        create_url=url_for('admin.milestone_create'),
        edit_url_func=lambda i: url_for('admin.milestone_edit', id=i.id),
        delete_url_func=lambda i: url_for('admin.milestone_delete', id=i.id),
        fields=['name', 'milestone_type', 'threshold', 'icon'],
        model_name='AchievementMilestone')


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
            created_by=current_user.id,
        )
        db.session.add(item)
        db.session.commit()
        flash('Hito creado.', 'success')
        return redirect(url_for('admin.milestones_list'))
    return render_template('admin/content_form.html',
        title='Nuevo Hito de Logro', action=url_for('admin.milestone_create'), model_name='AchievementMilestone')


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
        item.updated_by = current_user.id
        db.session.commit()
        flash('Hito actualizado.', 'success')
        return redirect(url_for('admin.milestones_list'))
    return render_template('admin/content_form.html',
        title='Editar Hito de Logro', action=url_for('admin.milestone_edit', id=id), item=item)


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
    query = User.query.order_by(User.created_at.desc())
    users = _paginate_and_search(query, search_fields=['username', 'email', 'full_name'])
    return render_template('admin/users_list.html', users=users, search=request.args.get('q', '').strip())


@admin_bp.route('/users/new', methods=['GET', 'POST'])
def user_create():
    if request.method == 'POST':
        username = request.form['username'].strip()
        email = request.form['email'].strip()
        password = request.form['password'].strip()
        if not username or not email or not password:
            flash('Username, email y password son requeridos.', 'danger')
            return redirect(url_for('admin.user_create'))
        if User.query.filter_by(username=username).first():
            flash('Ya existe un usuario con ese username.', 'danger')
            return redirect(url_for('admin.user_create'))
        if User.query.filter_by(email=email).first():
            flash('Ya existe un usuario con ese email.', 'danger')
            return redirect(url_for('admin.user_create'))
        user = User(
            username=username, email=email,
            full_name=request.form.get('full_name', '').strip() or None,
            is_admin='is_admin' in request.form,
            subscription_type=request.form.get('subscription_type', 'free'),
        )
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        flash(f'Usuario {username} creado.', 'success')
        return redirect(url_for('admin.users_list'))
    return render_template('admin/user_form.html', title='Nuevo Usuario',
        action=url_for('admin.user_create'))


@admin_bp.route('/users/<int:id>')
def user_detail(id):
    user = User.query.get_or_404(id)
    return render_template('admin/user_detail.html',
        user=user,
        progress=user.progress.all(),
        quiz_subs=UserQuizSubmission.query.filter_by(user_id=id).order_by(desc(UserQuizSubmission.id)).limit(20).all(),
        writing_subs=UserWritingSubmission.query.filter_by(user_id=id).order_by(desc(UserWritingSubmission.id)).limit(20).all(),
        study_results=StudyExerciseResult.query.filter_by(user_id=id).order_by(desc(StudyExerciseResult.id)).limit(20).all(),
        streak=UserStreak.query.filter_by(user_id=id).first(),
    )


@admin_bp.route('/users/<int:id>/edit', methods=['GET', 'POST'])
def user_edit(id):
    user = User.query.get_or_404(id)
    if request.method == 'POST':
        user.username = request.form['username'].strip()
        user.email = request.form['email'].strip()
        user.full_name = request.form.get('full_name', '').strip() or None
        user.subscription_type = request.form.get('subscription_type', 'free')
        new_password = request.form.get('password', '').strip()
        if new_password:
            user.set_password(new_password)
            flash('Contrasena actualizada.', 'success')
        db.session.commit()
        flash('Usuario actualizado.', 'success')
        return redirect(url_for('admin.user_detail', id=id))
    return render_template('admin/user_form.html', title='Editar Usuario',
        action=url_for('admin.user_edit', id=id), user=user)


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


@admin_bp.route('/users/<int:id>/reset-password', methods=['POST'])
def user_reset_password(id):
    user = User.query.get_or_404(id)
    new_password = request.form.get('new_password', '123456').strip()
    if not new_password:
        new_password = '123456'
    user.set_password(new_password)
    db.session.commit()
    flash(f'Contrasena de {user.username} reseteada.', 'success')
    return redirect(url_for('admin.user_detail', id=id))


# ===========================
# STUDENT RESULTS
# ===========================

@admin_bp.route('/results')
def results_overview():
    return render_template('admin/results.html',
        recent_quizzes=UserQuizSubmission.query.order_by(desc(UserQuizSubmission.id)).limit(30).all(),
        recent_writings=UserWritingSubmission.query.order_by(desc(UserWritingSubmission.id)).limit(30).all(),
        recent_study=StudyExerciseResult.query.order_by(desc(StudyExerciseResult.id)).limit(30).all(),
        quiz_avg=db.session.query(func.avg(UserQuizSubmission.score)).scalar() or 0,
        quiz_count=UserQuizSubmission.query.count(),
        writing_count=UserWritingSubmission.query.count(),
        study_count=StudyExerciseResult.query.count(),
    )


# ===========================
# MINI GAMES - Config
# ===========================

@admin_bp.route('/games')
def games_list():
    query = MiniGame.query.order_by(MiniGame.game_type)
    items = _paginate_and_search(query, search_fields=['game_type', 'title'])
    stats = {}
    for g in items:
        stats[g.game_type] = {
            'content_count': MiniGameContent.query.filter_by(game_type=g.game_type).count(),
            'plays': UserGameScore.query.filter_by(game_type=g.game_type).count(),
        }
    return render_template('admin/content_list.html',
        title='Mini Games - Configuracion',
        items=items, fields=['game_type', 'title', 'description', 'is_active'],
        create_url=url_for('admin.game_create'),
        edit_url_func=lambda i: url_for('admin.game_edit', id=i.id),
        delete_url_func=lambda i: url_for('admin.game_delete', id=i.id),
        stats=stats,
        model_name='MiniGame')


@admin_bp.route('/games/new', methods=['GET', 'POST'])
def game_create():
    if request.method == 'POST':
        item = MiniGame(
            game_type=request.form['game_type'].strip(),
            title=request.form['title'].strip(),
            description=request.form.get('description', '').strip(),
            instructions=request.form.get('instructions', '').strip(),
            difficulty_levels=_parse_json('difficulty_levels', {}),
            points_per_level=_parse_json('points_per_level', {}),
            is_active='is_active' in request.form,
            created_by=current_user.id,
        )
        db.session.add(item)
        db.session.commit()
        flash(f'Juego {item.game_type} creado.', 'success')
        return redirect(url_for('admin.games_list'))
    return render_template('admin/content_form.html', title='Nuevo Mini Game',
        action=url_for('admin.game_create'), item=None, model_name='MiniGame')


@admin_bp.route('/games/<int:id>/edit', methods=['GET', 'POST'])
def game_edit(id):
    item = MiniGame.query.get_or_404(id)
    if request.method == 'POST':
        item.game_type = request.form['game_type'].strip()
        item.title = request.form['title'].strip()
        item.description = request.form.get('description', '').strip()
        item.instructions = request.form.get('instructions', '').strip()
        item.difficulty_levels = _parse_json('difficulty_levels', {})
        item.points_per_level = _parse_json('points_per_level', {})
        item.is_active = 'is_active' in request.form
        item.updated_by = current_user.id
        db.session.commit()
        flash('Juego actualizado.', 'success')
        return redirect(url_for('admin.games_list'))
    return render_template('admin/content_form.html', title='Editar Mini Game',
        action=url_for('admin.game_edit', id=id), item=item)


@admin_bp.route('/games/<int:id>/delete', methods=['POST'])
def game_delete(id):
    item = MiniGame.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    flash('Juego eliminado.', 'success')
    return redirect(url_for('admin.games_list'))


# ===========================
# MINI GAMES - Content
# ===========================

@admin_bp.route('/games-content')
def game_content_list():
    game_type = request.args.get('game_type', '')
    query = MiniGameContent.query.order_by(MiniGameContent.game_type, MiniGameContent.level)
    items = _paginate_and_search(query, search_fields=['game_type', 'category'])
    return render_template('admin/content_list.html',
        title='Contenido de Mini Games',
        items=items, fields=['game_type', 'level', 'category', 'is_active'],
        create_url=url_for('admin.game_content_create', game_type=game_type),
        edit_url_func=lambda i: url_for('admin.game_content_edit', id=i.id),
        delete_url_func=lambda i: url_for('admin.game_content_delete', id=i.id),
        extra_filters={'game_type': game_type, 'options': ['word_scramble', 'hangman', 'memory', 'fill_gaps']},
        model_name='MiniGameContent')


@admin_bp.route('/games-content/new', methods=['GET', 'POST'])
def game_content_create():
    game_type = request.args.get('game_type', '') or request.form.get('game_type', '')
    if request.method == 'POST':
        item = MiniGameContent(
            game_type=request.form['game_type'].strip(),
            level=request.form['level'].strip(),
            content_data=_parse_json('content_data', {}),
            category=request.form.get('category', '').strip() or None,
            is_active='is_active' in request.form,
            created_by=current_user.id,
        )
        db.session.add(item)
        db.session.commit()
        flash('Contenido creado.', 'success')
        return redirect(url_for('admin.game_content_list', game_type=item.game_type))
    return render_template('admin/content_form.html', title='Nuevo Contenido de Juego',
        action=url_for('admin.game_content_create'), item=None, game_type=game_type, model_name='MiniGameContent')


@admin_bp.route('/games-content/<int:id>/edit', methods=['GET', 'POST'])
def game_content_edit(id):
    item = MiniGameContent.query.get_or_404(id)
    if request.method == 'POST':
        item.game_type = request.form['game_type'].strip()
        item.level = request.form['level'].strip()
        item.content_data = _parse_json('content_data', {})
        item.category = request.form.get('category', '').strip() or None
        item.is_active = 'is_active' in request.form
        item.updated_by = current_user.id
        db.session.commit()
        flash('Contenido actualizado.', 'success')
        return redirect(url_for('admin.game_content_list', game_type=item.game_type))
    return render_template('admin/content_form.html', title='Editar Contenido de Juego',
        action=url_for('admin.game_content_edit', id=id), item=item)


@admin_bp.route('/games-content/<int:id>/delete', methods=['POST'])
def game_content_delete(id):
    item = MiniGameContent.query.get_or_404(id)
    gt = item.game_type
    db.session.delete(item)
    db.session.commit()
    flash('Contenido eliminado.', 'success')
    return redirect(url_for('admin.game_content_list', game_type=gt))


# ===========================
# QUICK QUIZ
# ===========================

@admin_bp.route('/quick-quizzes')
def quick_quiz_list():
    query = QuickQuiz.query.order_by(QuickQuiz.cefr_level, QuickQuiz.category)
    items = _paginate_and_search(query, search_fields=['question', 'correct_answer'])
    return render_template('admin/content_list.html',
        title='Quick Quiz - Preguntas',
        items=items, fields=['question', 'correct_answer', 'category', 'cefr_level', 'difficulty', 'is_active'],
        create_url=url_for('admin.quick_quiz_create'),
        edit_url_func=lambda i: url_for('admin.quick_quiz_edit', id=i.id),
        delete_url_func=lambda i: url_for('admin.quick_quiz_delete', id=i.id),
        model_name='QuickQuiz')


@admin_bp.route('/quick-quizzes/new', methods=['GET', 'POST'])
def quick_quiz_create():
    if request.method == 'POST':
        item = QuickQuiz(
            question=request.form['question'].strip(),
            correct_answer=request.form['correct_answer'].strip(),
            wrong_answers=_parse_json('wrong_answers', []),
            explanation=request.form.get('explanation', '').strip(),
            category=request.form.get('category', '').strip(),
            cefr_level=request.form.get('cefr_level', 'A1'),
            difficulty=request.form.get('difficulty', 'medium'),
            is_active='is_active' in request.form,
            created_by=current_user.id,
        )
        db.session.add(item)
        db.session.commit()
        flash('Pregunta creada.', 'success')
        return redirect(url_for('admin.quick_quiz_list'))
    return render_template('admin/content_form.html', title='Nueva Pregunta Quick Quiz',
        action=url_for('admin.quick_quiz_create'), item=None, model_name='QuickQuiz')


@admin_bp.route('/quick-quizzes/<int:id>/edit', methods=['GET', 'POST'])
def quick_quiz_edit(id):
    item = QuickQuiz.query.get_or_404(id)
    if request.method == 'POST':
        item.question = request.form['question'].strip()
        item.correct_answer = request.form['correct_answer'].strip()
        item.wrong_answers = _parse_json('wrong_answers', [])
        item.explanation = request.form.get('explanation', '').strip()
        item.category = request.form.get('category', '').strip()
        item.cefr_level = request.form.get('cefr_level', 'A1')
        item.difficulty = request.form.get('difficulty', 'medium')
        item.is_active = 'is_active' in request.form
        item.updated_by = current_user.id
        db.session.commit()
        flash('Pregunta actualizada.', 'success')
        return redirect(url_for('admin.quick_quiz_list'))
    return render_template('admin/content_form.html', title='Editar Pregunta Quick Quiz',
        action=url_for('admin.quick_quiz_edit', id=id), item=item)


@admin_bp.route('/quick-quizzes/<int:id>/delete', methods=['POST'])
def quick_quiz_delete(id):
    item = QuickQuiz.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    flash('Pregunta eliminada.', 'success')
    return redirect(url_for('admin.quick_quiz_list'))


# ===========================
# READING COMPREHENSION
# ===========================

@admin_bp.route('/readings')
def readings_list():
    query = ReadingComprehension.query.order_by(ReadingComprehension.cefr_level, ReadingComprehension.title)
    items = _paginate_and_search(query, search_fields=['title', 'passage'])
    stats = {}
    for r in items:
        stats[r.id] = {
            'questions': len(r.questions),
            'plays': UserReadingScore.query.filter_by(reading_id=r.id).count(),
        }
    return render_template('admin/content_list.html',
        title='Reading Comprehension - Lecturas',
        items=items, fields=['title', 'cefr_level', 'category', 'word_count', 'reading_time_minutes', 'is_active'],
        create_url=url_for('admin.reading_create'),
        edit_url_func=lambda i: url_for('admin.reading_edit', id=i.id),
        delete_url_func=lambda i: url_for('admin.reading_delete', id=i.id),
        stats=stats,
        model_name='ReadingComprehension')


@admin_bp.route('/readings/new', methods=['GET', 'POST'])
def reading_create():
    if request.method == 'POST':
        item = ReadingComprehension(
            title=request.form['title'].strip(),
            passage=request.form['passage'].strip(),
            passage_summary=request.form.get('passage_summary', '').strip() or None,
            cefr_level=request.form.get('cefr_level', 'A1'),
            category=request.form.get('category', '').strip() or None,
            word_count=int(request.form.get('word_count', 0) or 0),
            reading_time_minutes=int(request.form.get('reading_time_minutes', 5) or 5),
            is_active='is_active' in request.form,
            created_by=current_user.id,
        )
        db.session.add(item)
        db.session.commit()
        flash('Lectura creada.', 'success')
        return redirect(url_for('admin.reading_questions_manage', reading_id=item.id))
    return render_template('admin/content_form.html', title='Nueva Lectura',
        action=url_for('admin.reading_create'), item=None, model_name='ReadingComprehension')


@admin_bp.route('/readings/<int:id>/edit', methods=['GET', 'POST'])
def reading_edit(id):
    item = ReadingComprehension.query.get_or_404(id)
    if request.method == 'POST':
        item.title = request.form['title'].strip()
        item.passage = request.form['passage'].strip()
        item.passage_summary = request.form.get('passage_summary', '').strip() or None
        item.cefr_level = request.form.get('cefr_level', 'A1')
        item.category = request.form.get('category', '').strip() or None
        item.word_count = int(request.form.get('word_count', 0) or 0)
        item.reading_time_minutes = int(request.form.get('reading_time_minutes', 5) or 5)
        item.is_active = 'is_active' in request.form
        item.updated_by = current_user.id
        db.session.commit()
        flash('Lectura actualizada.', 'success')
        return redirect(url_for('admin.readings_list'))
    return render_template('admin/content_form.html', title='Editar Lectura',
        action=url_for('admin.reading_edit', id=id), item=item)


@admin_bp.route('/readings/<int:id>/delete', methods=['POST'])
def reading_delete(id):
    item = ReadingComprehension.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    flash('Lectura eliminada.', 'success')
    return redirect(url_for('admin.readings_list'))


@admin_bp.route('/readings/<int:reading_id>/questions')
def reading_questions_manage(reading_id):
    reading = ReadingComprehension.query.get_or_404(reading_id)
    return render_template('admin/reading_questions.html',
        reading=reading,
        questions=ReadingQuestion.query.filter_by(reading_id=reading_id).order_by(ReadingQuestion.question_order).all(),
    )


@admin_bp.route('/readings/<int:reading_id>/questions/new', methods=['GET', 'POST'])
def reading_question_create(reading_id):
    reading = ReadingComprehension.query.get_or_404(reading_id)
    if request.method == 'POST':
        q = ReadingQuestion(
            reading_id=reading_id,
            question=request.form['question'].strip(),
            question_type=request.form.get('question_type', 'multiple_choice'),
            correct_answer=request.form['correct_answer'].strip(),
            wrong_answers=_parse_json('wrong_answers', []),
            question_order=int(request.form.get('question_order', 1) or 1),
        )
        db.session.add(q)
        db.session.commit()
        flash('Pregunta creada.', 'success')
        return redirect(url_for('admin.reading_questions_manage', reading_id=reading_id))
    return render_template('admin/content_form.html',
        title=f'Nueva Pregunta - {reading.title}',
        action=url_for('admin.reading_question_create', reading_id=reading_id), item=None, model_name='ReadingQuestion')


@admin_bp.route('/readings/questions/<int:qid>/edit', methods=['GET', 'POST'])
def reading_question_edit(qid):
    q = ReadingQuestion.query.get_or_404(qid)
    if request.method == 'POST':
        q.question = request.form['question'].strip()
        q.question_type = request.form.get('question_type', 'multiple_choice')
        q.correct_answer = request.form['correct_answer'].strip()
        q.wrong_answers = _parse_json('wrong_answers', [])
        q.question_order = int(request.form.get('question_order', 1) or 1)
        db.session.commit()
        flash('Pregunta actualizada.', 'success')
        return redirect(url_for('admin.reading_questions_manage', reading_id=q.reading_id))
    return render_template('admin/content_form.html',
        title=f'Editar Pregunta', action=url_for('admin.reading_question_edit', qid=qid), item=q)


@admin_bp.route('/readings/questions/<int:qid>/delete', methods=['POST'])
def reading_question_delete(qid):
    q = ReadingQuestion.query.get_or_404(qid)
    rid = q.reading_id
    db.session.delete(q)
    db.session.commit()
    flash('Pregunta eliminada.', 'success')
    return redirect(url_for('admin.reading_questions_manage', reading_id=rid))


# ===========================
# SPEED TYPING
# ===========================

@admin_bp.route('/speed-typing')
def speed_typing_list():
    query = SpeedTyping.query.order_by(SpeedTyping.cefr_level, SpeedTyping.category)
    items = _paginate_and_search(query, search_fields=['phrase', 'meaning'])
    return render_template('admin/content_list.html',
        title='Speed Typing - Frases',
        items=items, fields=['phrase', 'category', 'cefr_level', 'difficulty', 'meaning', 'is_active'],
        create_url=url_for('admin.speed_typing_create'),
        edit_url_func=lambda i: url_for('admin.speed_typing_edit', id=i.id),
        delete_url_func=lambda i: url_for('admin.speed_typing_delete', id=i.id),
        model_name='SpeedTyping')


@admin_bp.route('/speed-typing/new', methods=['GET', 'POST'])
def speed_typing_create():
    if request.method == 'POST':
        item = SpeedTyping(
            phrase=request.form['phrase'].strip(),
            category=request.form.get('category', '').strip() or None,
            cefr_level=request.form.get('cefr_level', 'A1'),
            difficulty=request.form.get('difficulty', 'medium'),
            pronunciation_hint=request.form.get('pronunciation_hint', '').strip() or None,
            meaning=request.form.get('meaning', '').strip() or None,
            example_sentence=request.form.get('example_sentence', '').strip() or None,
            is_active='is_active' in request.form,
            created_by=current_user.id,
        )
        db.session.add(item)
        db.session.commit()
        flash('Frase creada.', 'success')
        return redirect(url_for('admin.speed_typing_list'))
    return render_template('admin/content_form.html', title='Nueva Frase Speed Typing',
        action=url_for('admin.speed_typing_create'), item=None, model_name='SpeedTyping')


@admin_bp.route('/speed-typing/<int:id>/edit', methods=['GET', 'POST'])
def speed_typing_edit(id):
    item = SpeedTyping.query.get_or_404(id)
    if request.method == 'POST':
        item.phrase = request.form['phrase'].strip()
        item.category = request.form.get('category', '').strip() or None
        item.cefr_level = request.form.get('cefr_level', 'A1')
        item.difficulty = request.form.get('difficulty', 'medium')
        item.pronunciation_hint = request.form.get('pronunciation_hint', '').strip() or None
        item.meaning = request.form.get('meaning', '').strip() or None
        item.example_sentence = request.form.get('example_sentence', '').strip() or None
        item.is_active = 'is_active' in request.form
        item.updated_by = current_user.id
        db.session.commit()
        flash('Frase actualizada.', 'success')
        return redirect(url_for('admin.speed_typing_list'))
    return render_template('admin/content_form.html', title='Editar Frase Speed Typing',
        action=url_for('admin.speed_typing_edit', id=id), item=item)


@admin_bp.route('/speed-typing/<int:id>/delete', methods=['POST'])
def speed_typing_delete(id):
    item = SpeedTyping.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    flash('Frase eliminada.', 'success')
    return redirect(url_for('admin.speed_typing_list'))


# ===========================
# THEMATIC SCENARIOS
# ===========================

@admin_bp.route('/scenarios')
def scenarios_list():
    query = ThematicScenario.query.order_by(ThematicScenario.category, ThematicScenario.title)
    items = _paginate_and_search(query, search_fields=['title', 'category', 'description'])
    return render_template('admin/content_list.html',
        title='Escenarios Tematicos', items=items,
        create_url=url_for('admin.scenario_create'),
        edit_url_func=lambda i: url_for('admin.scenario_edit', id=i.id),
        delete_url_func=lambda i: url_for('admin.scenario_delete', id=i.id),
        fields=['title', 'category', 'difficulty', 'is_premium', 'price_points', 'is_active'],
        model_name='ThematicScenario')


@admin_bp.route('/scenarios/new', methods=['GET', 'POST'])
def scenario_create():
    if request.method == 'POST':
        item = ThematicScenario(
            title=request.form['title'].strip(),
            category=request.form.get('category', '').strip() or None,
            description=request.form.get('description', '').strip() or None,
            difficulty=request.form.get('difficulty', 'beginner'),
            icon_or_image=request.form.get('icon_or_image', '').strip() or None,
            is_premium='is_premium' in request.form,
            price_points=int(request.form.get('price_points', 100)),
            is_active='is_active' in request.form,
        )
        db.session.add(item)
        db.session.commit()
        flash('Escenario creado.', 'success')
        return redirect(url_for('admin.scenarios_list'))
    return render_template('admin/content_form.html',
        title='Nuevo Escenario', action=url_for('admin.scenario_create'),
        item=None, model_name='ThematicScenario')


@admin_bp.route('/scenarios/<int:id>/edit', methods=['GET', 'POST'])
def scenario_edit(id):
    item = ThematicScenario.query.get_or_404(id)
    if request.method == 'POST':
        item.title = request.form['title'].strip()
        item.category = request.form.get('category', '').strip() or None
        item.description = request.form.get('description', '').strip() or None
        item.difficulty = request.form.get('difficulty', 'beginner')
        item.icon_or_image = request.form.get('icon_or_image', '').strip() or None
        item.is_premium = 'is_premium' in request.form
        item.price_points = int(request.form.get('price_points', 100))
        item.is_active = 'is_active' in request.form
        db.session.commit()
        flash('Escenario actualizado.', 'success')
        return redirect(url_for('admin.scenarios_list'))
    return render_template('admin/content_form.html',
        title='Editar Escenario', action=url_for('admin.scenario_edit', id=id), item=item)


@admin_bp.route('/scenarios/<int:id>/delete', methods=['POST'])
def scenario_delete(id):
    item = ThematicScenario.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    flash('Escenario eliminado.', 'success')
    return redirect(url_for('admin.scenarios_list'))


# ===========================
# SCENARIO VOCABULARY (nested)
# ===========================

@admin_bp.route('/scenarios/<int:scenario_id>/vocabulary')
def scenario_vocab_list(scenario_id):
    scenario = ThematicScenario.query.get_or_404(scenario_id)
    items = ScenarioVocabulary.query.filter_by(scenario_id=scenario_id).order_by(ScenarioVocabulary.word).all()
    return render_template('admin/content_list.html',
        title=f'Vocabulario - {scenario.title}', items=items,
        create_url=url_for('admin.scenario_vocab_create', scenario_id=scenario_id),
        edit_url_func=lambda i: url_for('admin.scenario_vocab_edit', scenario_id=scenario_id, id=i.id),
        delete_url_func=lambda i: url_for('admin.scenario_vocab_delete', scenario_id=scenario_id, id=i.id),
        fields=['word', 'translation', 'part_of_speech', 'example_usage'],
        model_name='ScenarioVocabulary',
        back_url=url_for('admin.scenario_edit', id=scenario_id))


@admin_bp.route('/scenarios/<int:scenario_id>/vocabulary/new', methods=['GET', 'POST'])
def scenario_vocab_create(scenario_id):
    scenario = ThematicScenario.query.get_or_404(scenario_id)
    if request.method == 'POST':
        item = ScenarioVocabulary(
            scenario_id=scenario_id,
            word=request.form['word'].strip(),
            translation=request.form['translation'].strip(),
            part_of_speech=request.form.get('part_of_speech', '').strip() or None,
            example_usage=request.form.get('example_usage', '').strip() or None,
            audio_url=request.form.get('audio_url', '').strip() or None,
        )
        db.session.add(item)
        db.session.commit()
        flash('Vocabulario agregado.', 'success')
        return redirect(url_for('admin.scenario_vocab_list', scenario_id=scenario_id))
    return render_template('admin/content_form.html',
        title=f'Nuevo Vocabulario - {scenario.title}',
        action=url_for('admin.scenario_vocab_create', scenario_id=scenario_id),
        item=None, model_name='ScenarioVocabulary')


@admin_bp.route('/scenarios/<int:scenario_id>/vocabulary/<int:id>/edit', methods=['GET', 'POST'])
def scenario_vocab_edit(scenario_id, id):
    scenario = ThematicScenario.query.get_or_404(scenario_id)
    item = ScenarioVocabulary.query.get_or_404(id)
    if request.method == 'POST':
        item.word = request.form['word'].strip()
        item.translation = request.form['translation'].strip()
        item.part_of_speech = request.form.get('part_of_speech', '').strip() or None
        item.example_usage = request.form.get('example_usage', '').strip() or None
        item.audio_url = request.form.get('audio_url', '').strip() or None
        db.session.commit()
        flash('Vocabulario actualizado.', 'success')
        return redirect(url_for('admin.scenario_vocab_list', scenario_id=scenario_id))
    return render_template('admin/content_form.html',
        title=f'Editar Vocabulario - {scenario.title}',
        action=url_for('admin.scenario_vocab_edit', scenario_id=scenario_id, id=id), item=item)


@admin_bp.route('/scenarios/<int:scenario_id>/vocabulary/<int:id>/delete', methods=['POST'])
def scenario_vocab_delete(scenario_id, id):
    item = ScenarioVocabulary.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    flash('Vocabulario eliminado.', 'success')
    return redirect(url_for('admin.scenario_vocab_list', scenario_id=scenario_id))


# ===========================
# SCENARIO PHRASES (nested)
# ===========================

@admin_bp.route('/scenarios/<int:scenario_id>/phrases')
def scenario_phrases_list(scenario_id):
    scenario = ThematicScenario.query.get_or_404(scenario_id)
    items = ScenarioPhrase.query.filter_by(scenario_id=scenario_id).order_by(ScenarioPhrase.order).all()
    return render_template('admin/content_list.html',
        title=f'Frases - {scenario.title}', items=items,
        create_url=url_for('admin.scenario_phrase_create', scenario_id=scenario_id),
        edit_url_func=lambda i: url_for('admin.scenario_phrase_edit', scenario_id=scenario_id, id=i.id),
        delete_url_func=lambda i: url_for('admin.scenario_phrase_delete', scenario_id=scenario_id, id=i.id),
        fields=['role', 'phrase_type', 'english_text', 'spanish_translation', 'order'],
        model_name='ScenarioPhrase',
        back_url=url_for('admin.scenario_edit', id=scenario_id))


@admin_bp.route('/scenarios/<int:scenario_id>/phrases/new', methods=['GET', 'POST'])
def scenario_phrase_create(scenario_id):
    scenario = ThematicScenario.query.get_or_404(scenario_id)
    if request.method == 'POST':
        item = ScenarioPhrase(
            scenario_id=scenario_id,
            role=request.form['role'].strip(),
            phrase_type=request.form.get('phrase_type', '').strip() or None,
            english_text=request.form['english_text'].strip(),
            spanish_translation=request.form['spanish_translation'].strip(),
            audio_url=request.form.get('audio_url', '').strip() or None,
            order=int(request.form.get('order', 0)),
        )
        db.session.add(item)
        db.session.commit()
        flash('Frase agregada.', 'success')
        return redirect(url_for('admin.scenario_phrases_list', scenario_id=scenario_id))
    return render_template('admin/content_form.html',
        title=f'Nueva Frase - {scenario.title}',
        action=url_for('admin.scenario_phrase_create', scenario_id=scenario_id),
        item=None, model_name='ScenarioPhrase')


@admin_bp.route('/scenarios/<int:scenario_id>/phrases/<int:id>/edit', methods=['GET', 'POST'])
def scenario_phrase_edit(scenario_id, id):
    scenario = ThematicScenario.query.get_or_404(scenario_id)
    item = ScenarioPhrase.query.get_or_404(id)
    if request.method == 'POST':
        item.role = request.form['role'].strip()
        item.phrase_type = request.form.get('phrase_type', '').strip() or None
        item.english_text = request.form['english_text'].strip()
        item.spanish_translation = request.form['spanish_translation'].strip()
        item.audio_url = request.form.get('audio_url', '').strip() or None
        item.order = int(request.form.get('order', 0))
        db.session.commit()
        flash('Frase actualizada.', 'success')
        return redirect(url_for('admin.scenario_phrases_list', scenario_id=scenario_id))
    return render_template('admin/content_form.html',
        title=f'Editar Frase - {scenario.title}',
        action=url_for('admin.scenario_phrase_edit', scenario_id=scenario_id, id=id), item=item)


@admin_bp.route('/scenarios/<int:scenario_id>/phrases/<int:id>/delete', methods=['POST'])
def scenario_phrase_delete(scenario_id, id):
    item = ScenarioPhrase.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    flash('Frase eliminada.', 'success')
    return redirect(url_for('admin.scenario_phrases_list', scenario_id=scenario_id))
