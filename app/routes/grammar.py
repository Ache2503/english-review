from flask import Blueprint, render_template, abort, request, session, jsonify
from flask_login import login_required, current_user
from app.extensions import db
from app.models import UserSentence, SentenceLike, Verb, GrammarExerciseResult, GrammarTopicContent
from datetime import datetime
from sqlalchemy import func
import random

grammar_bp = Blueprint('grammar', __name__, url_prefix='/grammar')


def load_grammar_topics():
    rows = GrammarTopicContent.query.order_by(GrammarTopicContent.id).all()
    result = {}
    for r in rows:
        result[r.slug] = {
            'title': r.title,
            'subtitle': r.subtitle,
            'icon': r.icon,
            'level': r.level,
            'category': r.category,
            'description': r.description,
            'estimated_time': r.estimated_time,
            'sections': r.sections or [],
            'tips': r.tips or [],
            'common_mistakes': r.common_mistakes or [],
        }
    return result


@grammar_bp.route('/')
def index():
    grammar_topics = load_grammar_topics()
    levels = {'Beginner': [], 'Intermediate': [], 'Advanced': []}

    for key, topic in grammar_topics.items():
        level = topic.get('level', 'Beginner')
        levels[level].append({
            'key': key,
            **topic
        })

    return render_template(
        'grammar/index.html',
        levels=levels,
        total_topics=len(grammar_topics)
    )


@grammar_bp.route('/<topic_key>')
def topic_detail(topic_key):
    grammar_topics = load_grammar_topics()
    if topic_key not in grammar_topics:
        abort(404)

    topic = grammar_topics[topic_key]

    related = []
    current_category = topic.get('category', '')
    for key, t in grammar_topics.items():
        if key != topic_key and t.get('category') == current_category:
            related.append({'key': key, **t})
            if len(related) >= 3:
                break

    topics_list = list(grammar_topics.keys())
    current_index = topics_list.index(topic_key)
    prev_topic = topics_list[current_index - 1] if current_index > 0 else None
    next_topic = topics_list[current_index + 1] if current_index < len(topics_list) - 1 else None

    return render_template(
        'grammar/topic.html',
        topic=topic,
        topic_key=topic_key,
        related=related,
        prev_topic=prev_topic,
        next_topic=next_topic,
        prev_title=grammar_topics.get(prev_topic, {}).get('title') if prev_topic else None,
        next_title=grammar_topics.get(next_topic, {}).get('title') if next_topic else None
    )


@grammar_bp.route('/check-exercise', methods=['POST'])
def check_exercise():
    data = request.get_json()
    user_answer = data.get('answer', '').strip().lower()
    correct_answer = data.get('correct', '').strip().lower()

    is_correct = user_answer == correct_answer

    if not is_correct and '/' in correct_answer:
        alternatives = [a.strip() for a in correct_answer.split('/')]
        is_correct = user_answer in alternatives

    return jsonify({
        'correct': is_correct,
        'expected': correct_answer
    })


@grammar_bp.route('/<topic_key>/sentences')
def topic_sentences(topic_key):
    grammar_topics = load_grammar_topics()
    if topic_key not in grammar_topics:
        abort(404)

    topic = grammar_topics[topic_key]

    sentences = UserSentence.query.filter_by(
        grammar_topic=topic_key,
        is_approved=True
    ).order_by(UserSentence.likes_count.desc()).limit(50).all()

    featured = UserSentence.query.filter_by(
        grammar_topic=topic_key,
        is_featured=True
    ).limit(5).all()

    return render_template(
        'grammar/sentences.html',
        topic=topic,
        topic_key=topic_key,
        sentences=sentences,
        featured=featured
    )


@grammar_bp.route('/submit-sentence', methods=['POST'])
@login_required
def submit_sentence():
    grammar_topics = load_grammar_topics()
    data = request.get_json()
    topic_key = data.get('topic')
    sentence = data.get('sentence', '').strip()
    translation = data.get('translation', '').strip()

    if not topic_key or topic_key not in grammar_topics:
        return jsonify({'success': False, 'error': 'Tema inválido'})

    if not sentence or len(sentence) < 3:
        return jsonify({'success': False, 'error': 'La oración es muy corta'})

    if len(sentence) > 500:
        return jsonify({'success': False, 'error': 'La oración es muy larga (máx 500 caracteres)'})

    new_sentence = UserSentence(
        user_id=current_user.id,
        grammar_topic=topic_key,
        original_sentence=sentence,
        spanish_translation=translation if translation else None,
        difficulty=grammar_topics[topic_key].get('level', 'beginner').lower()
    )

    db.session.add(new_sentence)
    db.session.commit()

    return jsonify({
        'success': True,
        'message': '¡Oración enviada! Será revisada pronto.',
        'sentence_id': new_sentence.id
    })


@grammar_bp.route('/correct-sentence', methods=['POST'])
@login_required
def correct_sentence():
    data = request.get_json()
    sentence_id = data.get('sentence_id')
    corrected_text = data.get('corrected_text', '').strip()
    correction_notes = data.get('notes', '').strip()

    sentence = UserSentence.query.get_or_404(sentence_id)

    if sentence.user_id != current_user.id and not getattr(current_user, 'is_admin', False):
        return jsonify({'success': False, 'error': 'No tienes permiso'})

    if corrected_text:
        sentence.corrected_sentence = corrected_text
        sentence.is_correct = (corrected_text.lower() == sentence.original_sentence.lower())

    if correction_notes:
        sentence.correction_notes = correction_notes

    db.session.commit()

    return jsonify({
        'success': True,
        'message': 'Corrección guardada'
    })


@grammar_bp.route('/approve-sentence/<int:sentence_id>', methods=['POST'])
@login_required
def approve_sentence(sentence_id):
    if not getattr(current_user, 'is_admin', False):
        return jsonify({'success': False, 'error': 'Solo administradores'})

    sentence = UserSentence.query.get_or_404(sentence_id)
    sentence.is_approved = True
    db.session.commit()

    return jsonify({'success': True})


@grammar_bp.route('/like-sentence/<int:sentence_id>', methods=['POST'])
@login_required
def like_sentence(sentence_id):
    sentence = UserSentence.query.get_or_404(sentence_id)

    existing = SentenceLike.query.filter_by(
        user_id=current_user.id,
        sentence_id=sentence_id
    ).first()

    if existing:
        db.session.delete(existing)
        sentence.likes_count = max(0, sentence.likes_count - 1)
        liked = False
    else:
        like = SentenceLike(user_id=current_user.id, sentence_id=sentence_id)
        db.session.add(like)
        sentence.likes_count += 1
        liked = True

    db.session.commit()

    return jsonify({
        'success': True,
        'liked': liked,
        'likes_count': sentence.likes_count
    })


@grammar_bp.route('/random-sentence/<topic_key>')
def random_sentence(topic_key):
    sentences = UserSentence.query.filter_by(
        grammar_topic=topic_key,
        is_approved=True,
        is_correct=True
    ).all()

    if not sentences:
        return jsonify({'success': False, 'error': 'No hay oraciones disponibles'})

    sentence = random.choice(sentences)
    sentence.used_in_exercises += 1
    db.session.commit()

    return jsonify({
        'success': True,
        'sentence': {
            'id': sentence.id,
            'text': sentence.corrected_sentence or sentence.original_sentence,
            'translation': sentence.spanish_translation,
            'author': sentence.user.username if sentence.user else 'Anónimo'
        }
    })


@grammar_bp.route('/my-sentences')
@login_required
def my_sentences():
    sentences = UserSentence.query.filter_by(
        user_id=current_user.id
    ).order_by(UserSentence.created_at.desc()).all()

    stats = {
        'total': len(sentences),
        'approved': sum(1 for s in sentences if s.is_approved),
        'featured': sum(1 for s in sentences if s.is_featured),
        'total_likes': sum(s.likes_count for s in sentences)
    }

    return render_template(
        'grammar/my_sentences.html',
        sentences=sentences,
        stats=stats
    )


@grammar_bp.route('/verbs')
def verbs_index():
    stats = {
        'total': Verb.query.count(),
        'irregular': Verb.query.filter_by(is_irregular=True).count(),
        'regular': Verb.query.filter_by(is_irregular=False).count(),
        'modal': Verb.query.filter_by(is_modal=True).count()
    }

    featured_verbs = Verb.query.filter(
        Verb.frequency_rank != None
    ).order_by(Verb.frequency_rank).limit(20).all()

    categories = db.session.query(Verb.category).distinct().filter(
        Verb.category != None
    ).all()
    categories = [c[0] for c in categories]

    return render_template(
        'grammar/verbs.html',
        stats=stats,
        featured_verbs=featured_verbs,
        categories=categories
    )


@grammar_bp.route('/verbs/search')
def search_verbs():
    query = request.args.get('q', '').strip().lower()
    filter_type = request.args.get('type', 'all')
    category = request.args.get('category', '')
    limit = min(int(request.args.get('limit', 20)), 100)

    verbs_query = Verb.query

    if query:
        verbs_query = verbs_query.filter(
            db.or_(
                Verb.infinitive.ilike(f'%{query}%'),
                Verb.spanish_translation.ilike(f'%{query}%'),
                Verb.past_simple.ilike(f'%{query}%'),
                Verb.past_participle.ilike(f'%{query}%')
            )
        )

    if filter_type == 'irregular':
        verbs_query = verbs_query.filter_by(is_irregular=True)
    elif filter_type == 'regular':
        verbs_query = verbs_query.filter_by(is_irregular=False)
    elif filter_type == 'modal':
        verbs_query = verbs_query.filter_by(is_modal=True)

    if category:
        verbs_query = verbs_query.filter_by(category=category)

    verbs_query = verbs_query.order_by(Verb.frequency_rank.nullslast())

    verbs = verbs_query.limit(limit).all()

    return jsonify({
        'success': True,
        'count': len(verbs),
        'verbs': [{
            'id': v.id,
            'infinitive': v.infinitive,
            'past_simple': v.past_simple,
            'past_participle': v.past_participle,
            'present_participle': v.present_participle,
            'third_person': v.third_person,
            'spanish': v.spanish_translation,
            'is_irregular': v.is_irregular,
            'is_modal': v.is_modal,
            'category': v.category,
            'example': v.example_sentence,
            'example_translation': v.example_translation,
            'notes': v.notes
        } for v in verbs]
    })


@grammar_bp.route('/verbs/<infinitive>')
def verb_detail(infinitive):
    verb = Verb.query.filter(
        func.lower(Verb.infinitive) == infinitive.lower()
    ).first_or_404()

    similar = Verb.query.filter(
        Verb.category == verb.category,
        Verb.id != verb.id
    ).limit(5).all()

    return render_template(
        'grammar/verb_detail.html',
        verb=verb,
        similar=similar
    )


@grammar_bp.route('/verbs/random')
def random_verb():
    verb_type = request.args.get('type', 'all')

    query = Verb.query
    if verb_type == 'irregular':
        query = query.filter_by(is_irregular=True)
    elif verb_type == 'regular':
        query = query.filter_by(is_irregular=False)

    verbs = query.all()
    if not verbs:
        return jsonify({'success': False})

    verb = random.choice(verbs)

    return jsonify({
        'success': True,
        'verb': {
            'infinitive': verb.infinitive,
            'past_simple': verb.past_simple,
            'past_participle': verb.past_participle,
            'spanish': verb.spanish_translation,
            'is_irregular': verb.is_irregular
        }
    })


@grammar_bp.route('/save-exercise-result', methods=['POST'])
@login_required
def save_exercise_result():
    data = request.get_json()

    result = GrammarExerciseResult(
        user_id=current_user.id,
        grammar_topic=data.get('topic'),
        exercise_type=data.get('exercise_type', 'fill_blank'),
        total_questions=data.get('total', 0),
        correct_answers=data.get('correct', 0),
        score_percentage=data.get('score', 0.0),
        time_spent_seconds=data.get('time_seconds')
    )

    db.session.add(result)
    db.session.commit()

    return jsonify({
        'success': True,
        'result_id': result.id
    })


@grammar_bp.route('/my-progress')
@login_required
def grammar_progress():
    grammar_topics = load_grammar_topics()

    results = db.session.query(
        GrammarExerciseResult.grammar_topic,
        func.count(GrammarExerciseResult.id).label('attempts'),
        func.avg(GrammarExerciseResult.score_percentage).label('avg_score'),
        func.max(GrammarExerciseResult.score_percentage).label('best_score')
    ).filter_by(user_id=current_user.id).group_by(
        GrammarExerciseResult.grammar_topic
    ).all()

    progress = []
    for r in results:
        topic_info = grammar_topics.get(r.grammar_topic, {})
        progress.append({
            'topic_key': r.grammar_topic,
            'title': topic_info.get('title', r.grammar_topic),
            'icon': topic_info.get('icon', '📚'),
            'attempts': r.attempts,
            'avg_score': round(r.avg_score or 0, 1),
            'best_score': round(r.best_score or 0, 1)
        })

    total_exercises = GrammarExerciseResult.query.filter_by(
        user_id=current_user.id
    ).count()

    avg_overall = db.session.query(
        func.avg(GrammarExerciseResult.score_percentage)
    ).filter_by(user_id=current_user.id).scalar() or 0

    return render_template(
        'grammar/progress.html',
        progress=progress,
        total_exercises=total_exercises,
        avg_overall=round(avg_overall, 1),
        grammar_topics=grammar_topics
    )
