"""
Rutas para Idioms & Phrasal Verbs
"""
from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user
from app.extensions import db
from app.models import (
    Idiom, PhrasalVerb, UserIdiomProgress, UserPhrasalVerbProgress
)
from datetime import datetime, timedelta
from sqlalchemy import func
from app.routes.challenges import add_points
import random

idioms_bp = Blueprint('idioms', __name__, url_prefix='/idioms')


# ==========================================
# IDIOMS
# ==========================================

@idioms_bp.route('/')
@login_required
def idiom_list():
    """Lista de idioms por nivel y categoría"""
    level = request.args.get('level', None)
    category = request.args.get('category', None)
    
    query = Idiom.query.filter_by(is_active=True)
    
    if level:
        query = query.filter_by(level=level)
    if category:
        query = query.filter_by(category=category)
    
    idioms = query.order_by(Idiom.level, Idiom.phrase).all()
    
    # Progreso del usuario
    user_progress = {}
    for idiom in idioms:
        progress = UserIdiomProgress.query.filter_by(
            user_id=current_user.id,
            idiom_id=idiom.id
        ).first()
        user_progress[idiom.id] = progress
    
    # Categorías y niveles disponibles
    categories = db.session.query(Idiom.category).filter(
        Idiom.category.isnot(None)
    ).distinct().all()
    levels = db.session.query(Idiom.level).distinct().all()
    
    # Estadísticas
    total_idioms = Idiom.query.filter_by(is_active=True).count()
    mastered = UserIdiomProgress.query.filter_by(
        user_id=current_user.id,
        mastery_level='mastered'
    ).count()
    
    return render_template(
        'idioms/list.html',
        idioms=idioms,
        user_progress=user_progress,
        categories=[c[0] for c in categories if c[0]],
        levels=[l[0] for l in levels],
        current_level=level,
        current_category=category,
        total_idioms=total_idioms,
        mastered=mastered
    )


@idioms_bp.route('/<int:idiom_id>')
@login_required
def idiom_detail(idiom_id):
    """Detalle de un idiom"""
    idiom = Idiom.query.get_or_404(idiom_id)
    
    progress = UserIdiomProgress.query.filter_by(
        user_id=current_user.id,
        idiom_id=idiom_id
    ).first()
    
    # Idioms relacionados (misma categoría)
    related = Idiom.query.filter(
        Idiom.category == idiom.category,
        Idiom.id != idiom.id,
        Idiom.is_active == True
    ).limit(5).all()
    
    return render_template(
        'idioms/detail.html',
        idiom=idiom,
        progress=progress,
        related=related
    )


@idioms_bp.route('/practice')
@login_required
def practice_idioms():
    """Práctica de idioms"""
    level = request.args.get('level', None)
    mode = request.args.get('mode', 'learn')  # learn, quiz, review
    
    query = Idiom.query.filter_by(is_active=True)
    if level:
        query = query.filter_by(level=level)
    
    idioms = query.all()
    
    if mode == 'review':
        # Obtener idioms que necesitan repaso
        due_progress = UserIdiomProgress.query.filter(
            UserIdiomProgress.user_id == current_user.id,
            UserIdiomProgress.next_review <= datetime.utcnow()
        ).all()
        idiom_ids = [p.idiom_id for p in due_progress]
        idioms = Idiom.query.filter(Idiom.id.in_(idiom_ids)).all() if idiom_ids else []
    
    random.shuffle(idioms)
    
    return render_template(
        'idioms/practice.html',
        idioms=idioms[:10],
        mode=mode,
        level=level
    )


@idioms_bp.route('/practice/submit', methods=['POST'])
@login_required
def submit_idiom_practice():
    """Enviar respuestas de práctica"""
    data = request.get_json()
    results = data.get('results', [])
    
    correct_count = 0
    for result in results:
        idiom_id = result.get('idiom_id')
        is_correct = result.get('is_correct', False)
        
        if is_correct:
            correct_count += 1
        
        # Actualizar progreso
        progress = UserIdiomProgress.query.filter_by(
            user_id=current_user.id,
            idiom_id=idiom_id
        ).first()
        
        if not progress:
            progress = UserIdiomProgress(
                user_id=current_user.id,
                idiom_id=idiom_id
            )
            db.session.add(progress)
        
        progress.times_reviewed += 1
        if is_correct:
            progress.times_correct += 1
        progress.last_reviewed = datetime.utcnow()
        
        # Calcular próximo repaso (SRS simple)
        if is_correct:
            if progress.mastery_level == 'new':
                progress.mastery_level = 'learning'
                progress.next_review = datetime.utcnow() + timedelta(days=1)
            elif progress.mastery_level == 'learning':
                if progress.times_correct >= 3:
                    progress.mastery_level = 'mastered'
                    progress.next_review = datetime.utcnow() + timedelta(days=7)
                else:
                    progress.next_review = datetime.utcnow() + timedelta(days=2)
            else:
                progress.next_review = datetime.utcnow() + timedelta(days=14)
        else:
            progress.mastery_level = 'learning'
            progress.next_review = datetime.utcnow() + timedelta(hours=12)
    
    # Dar puntos
    points = correct_count * 5
    add_points(current_user.id, points, 'idioms', f'Práctica de idioms')
    
    db.session.commit()
    
    return jsonify({
        'success': True,
        'correct': correct_count,
        'total': len(results),
        'points_earned': points
    })


# ==========================================
# PHRASAL VERBS
# ==========================================

@idioms_bp.route('/phrasal-verbs')
@login_required
def phrasal_verb_list():
    """Lista de phrasal verbs"""
    level = request.args.get('level', None)
    verb = request.args.get('verb', None)
    
    query = PhrasalVerb.query.filter_by(is_active=True)
    
    if level:
        query = query.filter_by(level=level)
    if verb:
        query = query.filter_by(verb=verb)
    
    phrasal_verbs = query.order_by(PhrasalVerb.verb, PhrasalVerb.particle).all()
    
    # Agrupar por verbo base
    by_verb = {}
    for pv in phrasal_verbs:
        if pv.verb not in by_verb:
            by_verb[pv.verb] = []
        by_verb[pv.verb].append(pv)
    
    # Progreso del usuario
    user_progress = {}
    for pv in phrasal_verbs:
        progress = UserPhrasalVerbProgress.query.filter_by(
            user_id=current_user.id,
            phrasal_verb_id=pv.id
        ).first()
        user_progress[pv.id] = progress
    
    # Verbos base disponibles
    base_verbs = db.session.query(PhrasalVerb.verb).distinct().order_by(PhrasalVerb.verb).all()
    levels = db.session.query(PhrasalVerb.level).distinct().all()
    
    # Estadísticas
    total_pv = PhrasalVerb.query.filter_by(is_active=True).count()
    mastered = UserPhrasalVerbProgress.query.filter_by(
        user_id=current_user.id,
        mastery_level='mastered'
    ).count()
    
    return render_template(
        'idioms/phrasal_verbs.html',
        by_verb=by_verb,
        user_progress=user_progress,
        base_verbs=[v[0] for v in base_verbs],
        levels=[l[0] for l in levels],
        current_level=level,
        current_verb=verb,
        total_pv=total_pv,
        mastered=mastered
    )


@idioms_bp.route('/phrasal-verbs/<int:pv_id>')
@login_required
def phrasal_verb_detail(pv_id):
    """Detalle de phrasal verb"""
    pv = PhrasalVerb.query.get_or_404(pv_id)
    
    progress = UserPhrasalVerbProgress.query.filter_by(
        user_id=current_user.id,
        phrasal_verb_id=pv_id
    ).first()
    
    # Otros phrasal verbs con el mismo verbo base
    related = PhrasalVerb.query.filter(
        PhrasalVerb.verb == pv.verb,
        PhrasalVerb.id != pv.id,
        PhrasalVerb.is_active == True
    ).all()
    
    return render_template(
        'idioms/phrasal_detail.html',
        phrasal_verb=pv,
        progress=progress,
        related=related
    )


@idioms_bp.route('/phrasal-verbs/practice')
@login_required
def practice_phrasal_verbs():
    """Práctica de phrasal verbs"""
    level = request.args.get('level', None)
    verb = request.args.get('verb', None)
    
    query = PhrasalVerb.query.filter_by(is_active=True)
    if level:
        query = query.filter_by(level=level)
    if verb:
        query = query.filter_by(verb=verb)
    
    phrasal_verbs = query.all()
    random.shuffle(phrasal_verbs)
    
    return render_template(
        'idioms/phrasal_practice.html',
        phrasal_verbs=phrasal_verbs[:10],
        level=level,
        verb=verb
    )


@idioms_bp.route('/phrasal-verbs/practice/submit', methods=['POST'])
@login_required
def submit_phrasal_practice():
    """Enviar respuestas de práctica de phrasal verbs"""
    data = request.get_json()
    results = data.get('results', [])
    
    correct_count = 0
    for result in results:
        pv_id = result.get('phrasal_verb_id')
        is_correct = result.get('is_correct', False)
        
        if is_correct:
            correct_count += 1
        
        # Actualizar progreso
        progress = UserPhrasalVerbProgress.query.filter_by(
            user_id=current_user.id,
            phrasal_verb_id=pv_id
        ).first()
        
        if not progress:
            progress = UserPhrasalVerbProgress(
                user_id=current_user.id,
                phrasal_verb_id=pv_id
            )
            db.session.add(progress)
        
        progress.times_reviewed += 1
        if is_correct:
            progress.times_correct += 1
        progress.last_reviewed = datetime.utcnow()
        
        # SRS simple
        if is_correct:
            if progress.mastery_level == 'new':
                progress.mastery_level = 'learning'
                progress.next_review = datetime.utcnow() + timedelta(days=1)
            elif progress.mastery_level == 'learning':
                if progress.times_correct >= 3:
                    progress.mastery_level = 'mastered'
                    progress.next_review = datetime.utcnow() + timedelta(days=7)
                else:
                    progress.next_review = datetime.utcnow() + timedelta(days=2)
            else:
                progress.next_review = datetime.utcnow() + timedelta(days=14)
        else:
            progress.mastery_level = 'learning'
            progress.next_review = datetime.utcnow() + timedelta(hours=12)
    
    points = correct_count * 5
    add_points(current_user.id, points, 'phrasal_verbs', f'Práctica de phrasal verbs')
    
    db.session.commit()
    
    return jsonify({
        'success': True,
        'correct': correct_count,
        'total': len(results),
        'points_earned': points
    })


# ==========================================
# API para Quiz
# ==========================================

@idioms_bp.route('/api/quiz')
@login_required
def get_quiz_data():
    """Obtener datos para quiz de idioms/phrasal verbs"""
    quiz_type = request.args.get('type', 'idiom')  # idiom o phrasal
    count = int(request.args.get('count', 5))
    level = request.args.get('level', None)
    
    if quiz_type == 'idiom':
        query = Idiom.query.filter_by(is_active=True)
        if level:
            query = query.filter_by(level=level)
        items = query.all()
        
        random.shuffle(items)
        selected = items[:count]
        
        questions = []
        for item in selected:
            # Obtener opciones incorrectas
            wrong_options = [i.meaning for i in items if i.id != item.id][:3]
            options = [item.meaning] + wrong_options
            random.shuffle(options)
            
            questions.append({
                'id': item.id,
                'question': f'What does "{item.phrase}" mean?',
                'phrase': item.phrase,
                'options': options,
                'correct': item.meaning
            })
    else:
        query = PhrasalVerb.query.filter_by(is_active=True)
        if level:
            query = query.filter_by(level=level)
        items = query.all()
        
        random.shuffle(items)
        selected = items[:count]
        
        questions = []
        for item in selected:
            wrong_options = [i.meaning for i in items if i.id != item.id][:3]
            options = [item.meaning] + wrong_options
            random.shuffle(options)
            
            questions.append({
                'id': item.id,
                'question': f'What does "{item.full_form}" mean?',
                'phrase': item.full_form,
                'options': options,
                'correct': item.meaning
            })
    
    return jsonify({'questions': questions})
