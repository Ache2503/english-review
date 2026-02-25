"""
Rutas para Bookmarks/Favoritos
=============================
"""

from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user
from app.models import Bookmark, UserActivity
from app.extensions import db

bookmarks_bp = Blueprint('bookmarks', __name__, url_prefix='/bookmarks')


@bookmarks_bp.route('/')
@login_required
def list():
    """Lista de favoritos del usuario"""
    filter_type = request.args.get('type', 'all')
    
    query = Bookmark.query.filter_by(user_id=current_user.id)
    
    if filter_type != 'all':
        query = query.filter_by(bookmark_type=filter_type)
    
    bookmarks = query.order_by(Bookmark.created_at.desc()).all()
    
    # Agrupar por tipo
    grouped = {}
    for b in bookmarks:
        if b.bookmark_type not in grouped:
            grouped[b.bookmark_type] = []
        grouped[b.bookmark_type].append(b)
    
    return render_template('bookmarks/list.html', 
                           bookmarks=bookmarks,
                           grouped=grouped,
                           filter_type=filter_type)


@bookmarks_bp.route('/add', methods=['POST'])
@login_required
def add():
    """Agregar un favorito"""
    bookmark_type = request.form.get('bookmark_type')
    english_text = request.form.get('english_text', '').strip()
    spanish_translation = request.form.get('spanish_translation', '').strip()
    notes = request.form.get('notes', '').strip()
    source = request.form.get('source', '')
    
    # IDs opcionales
    vocabulary_id = request.form.get('vocabulary_id')
    phrase_id = request.form.get('phrase_id')
    grammar_id = request.form.get('grammar_id')
    sentence_id = request.form.get('sentence_id')
    
    if not english_text:
        flash('El texto en inglés es requerido', 'warning')
        return redirect(request.referrer or url_for('bookmarks.list'))
    
    # Verificar si ya existe
    existing = Bookmark.query.filter_by(
        user_id=current_user.id,
        bookmark_type=bookmark_type
    )
    
    if vocabulary_id:
        existing = existing.filter_by(vocabulary_id=vocabulary_id).first()
    elif phrase_id:
        existing = existing.filter_by(phrase_id=phrase_id).first()
    else:
        existing = None
    
    if existing:
        flash('Ya tienes este elemento en favoritos', 'info')
        return redirect(request.referrer or url_for('bookmarks.list'))
    
    # Crear bookmark
    bookmark = Bookmark(
        user_id=current_user.id,
        bookmark_type=bookmark_type,
        english_text=english_text,
        spanish_translation=spanish_translation,
        notes=notes,
        source=source,
        vocabulary_id=vocabulary_id,
        phrase_id=phrase_id,
        grammar_id=grammar_id,
        sentence_id=sentence_id
    )
    
    db.session.add(bookmark)
    db.session.commit()
    
    flash('Agregado a favoritos', 'success')
    return redirect(request.referrer or url_for('bookmarks.list'))


@bookmarks_bp.route('/add/ajax', methods=['POST'])
@login_required
def add_ajax():
    """Agregar favorito via AJAX"""
    data = request.get_json()
    
    bookmark = Bookmark(
        user_id=current_user.id,
        bookmark_type=data.get('bookmark_type', 'phrase'),
        english_text=data.get('english_text', ''),
        spanish_translation=data.get('spanish_translation', ''),
        notes=data.get('notes', ''),
        source=data.get('source', ''),
        vocabulary_id=data.get('vocabulary_id'),
        phrase_id=data.get('phrase_id'),
        grammar_id=data.get('grammar_id'),
        sentence_id=data.get('sentence_id')
    )
    
    db.session.add(bookmark)
    db.session.commit()
    
    return jsonify({'success': True, 'bookmark_id': bookmark.id})


@bookmarks_bp.route('/<int:bookmark_id>/delete', methods=['POST'])
@login_required
def delete(bookmark_id):
    """Eliminar un favorito"""
    bookmark = Bookmark.query.get_or_404(bookmark_id)
    
    if bookmark.user_id != current_user.id:
        flash('No tienes permiso', 'danger')
        return redirect(url_for('bookmarks.list'))
    
    db.session.delete(bookmark)
    db.session.commit()
    
    flash('Eliminado de favoritos', 'success')
    return redirect(url_for('bookmarks.list'))


@bookmarks_bp.route('/<int:bookmark_id>/update', methods=['POST'])
@login_required
def update(bookmark_id):
    """Actualizar notas de un favorito"""
    bookmark = Bookmark.query.get_or_404(bookmark_id)
    
    if bookmark.user_id != current_user.id:
        return jsonify({'success': False, 'error': 'Unauthorized'}), 403
    
    bookmark.notes = request.form.get('notes', '')
    db.session.commit()
    
    return jsonify({'success': True})


@bookmarks_bp.route('/check')
@login_required
def check():
    """Verificar si un elemento está en favoritos (para AJAX)"""
    bookmark_type = request.args.get('type')
    vocabulary_id = request.args.get('vocabulary_id')
    phrase_id = request.args.get('phrase_id')
    
    query = Bookmark.query.filter_by(user_id=current_user.id, bookmark_type=bookmark_type)
    
    if vocabulary_id:
        bookmark = query.filter_by(vocabulary_id=vocabulary_id).first()
    elif phrase_id:
        bookmark = query.filter_by(phrase_id=phrase_id).first()
    else:
        bookmark = None
    
    return jsonify({'is_bookmarked': bookmark is not None, 'bookmark_id': bookmark.id if bookmark else None})
