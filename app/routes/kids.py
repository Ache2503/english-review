from flask import Blueprint, render_template, redirect, url_for, request
from app.extensions import db
from flask_login import login_required, current_user
from app.models import ChildProfile, KidsTopic, KidsVocabulary
import json

kids_bp = Blueprint('kids', __name__, url_prefix='/kids')

@kids_bp.route('/')
@login_required
def select_profile():
    """Pantalla para elegir qué niño va a jugar (estilo Netflix)"""
    children = ChildProfile.query.filter_by(parent_id=current_user.id).all()
    return render_template('kids/select_profile.html', children=children)

@kids_bp.route('/profile/<int:child_id>/map')
@login_required
def learning_map(child_id):
    """El mapa visual de temas para el niño (Colores, Animales, etc.)"""
    child = ChildProfile.query.get_or_404(child_id)
    if child.parent_id != current_user.id:
        return redirect(url_for('kids.select_profile'))
        
    topics = KidsTopic.query.filter_by(is_active=True).order_by(KidsTopic.order).all()
    return render_template('kids/map.html', child=child, topics=topics)

@kids_bp.route('/profile/<int:child_id>/topic/<int:topic_id>')
@login_required
def topic_view(child_id, topic_id):
    """La pantalla interactiva donde el niño aprende las palabras"""
    child = ChildProfile.query.get_or_404(child_id)
    if child.parent_id != current_user.id:
        return redirect(url_for('kids.select_profile'))
        
    topic = KidsTopic.query.get_or_404(topic_id)
    vocabulary = topic.vocabulary.all()
    
    return render_template('kids/topic_view.html', child=child, topic=topic, vocabulary=vocabulary)

@kids_bp.route('/add_profile', methods=['GET', 'POST'])
@login_required
def add_profile():
    """Pantalla para que el papá cree un nuevo perfil de niño"""
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        
        if name and age:
            new_child = ChildProfile(
                parent_id=current_user.id, 
                name=name, 
                age=int(age), 
                avatar_url="/static/img/kids/avatars/lion.png" # Avatar genérico por ahora
            )
            db.session.add(new_child)
            db.session.commit()
            return redirect(url_for('kids.select_profile'))
            
    return render_template('kids/add_profile.html')

@kids_bp.route('/profile/<int:child_id>/topic/<int:topic_id>/game')
@login_required
def play_game(child_id, topic_id):
    """El minijuego interactivo 'Escucha y Toca' para los niños"""
    child = ChildProfile.query.get_or_404(child_id)
    if child.parent_id != current_user.id:
        return redirect(url_for('kids.select_profile'))
        
    topic = KidsTopic.query.get_or_404(topic_id)
    vocabulary = topic.vocabulary.all()
    
    vocab_list = []
    for v in vocabulary:
        vocab_list.append({
            'word_en': v.word_english,
            'word_es': v.word_spanish,
            'image': v.image_url, 
            'color': '#ffffff' 
        })
        
    return render_template('kids/game.html', child=child, topic=topic, vocab_data=vocab_list)