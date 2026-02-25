"""
Rutas para Feedback de Usuarios
===============================
"""

from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user
from app.models import UserFeedback
from app.extensions import db
from datetime import datetime

feedback_bp = Blueprint('feedback', __name__, url_prefix='/feedback')


@feedback_bp.route('/', methods=['GET'])
def index():
    """Página principal de feedback (para usuarios)"""
    return render_template('feedback/index.html')


@feedback_bp.route('/submit', methods=['POST'])
def submit():
    """Enviar feedback"""
    feedback_type = request.form.get('feedback_type', 'suggestion')
    category = request.form.get('category', 'general')
    subject = request.form.get('subject', '')
    message = request.form.get('message', '').strip()
    rating = request.form.get('rating')
    page_url = request.form.get('page_url', '')
    
    if not message:
        flash('Por favor escribe un mensaje', 'warning')
        return redirect(request.referrer or url_for('main.index'))
    
    # Validar tipo de feedback
    valid_types = ['bug', 'suggestion', 'compliment', 'complaint']
    if feedback_type not in valid_types:
        feedback_type = 'suggestion'
    
    # Crear feedback
    feedback = UserFeedback(
        user_id=current_user.id if current_user.is_authenticated else None,
        feedback_type=feedback_type,
        category=category,
        subject=subject,
        message=message,
        rating=int(rating) if rating else None,
        page_url=page_url,
        browser_info=request.user_agent.string[:200]
    )
    
    db.session.add(feedback)
    db.session.commit()
    
    flash('¡Gracias por tu feedback! Nos ayuda a mejorar.', 'success')
    return redirect(request.referrer or url_for('main.index'))


@feedback_bp.route('/api/submit', methods=['POST'])
def api_submit():
    """API para enviar feedback via JSON"""
    data = request.get_json()
    
    if not data or not data.get('message'):
        return jsonify({'success': False, 'error': 'Message required'}), 400
    
    feedback = UserFeedback(
        user_id=current_user.id if current_user.is_authenticated else None,
        feedback_type=data.get('feedback_type', 'suggestion'),
        category=data.get('category', 'general'),
        subject=data.get('subject', ''),
        message=data['message'],
        rating=data.get('rating'),
        page_url=data.get('page_url', ''),
        browser_info=request.user_agent.string[:200]
    )
    
    db.session.add(feedback)
    db.session.commit()
    
    return jsonify({'success': True, 'message': 'Feedback received'})


# ============================================================================
# ADMIN: GESTIÓN DE FEEDBACK
# ============================================================================

@feedback_bp.route('/admin')
@login_required
def admin_list():
    """Lista de feedback (solo admin)"""
    if not current_user.is_admin:
        flash('Acceso denegado', 'danger')
        return redirect(url_for('main.index'))
    
    status_filter = request.args.get('status', 'all')
    type_filter = request.args.get('type', 'all')
    
    query = UserFeedback.query
    
    if status_filter != 'all':
        query = query.filter_by(status=status_filter)
    if type_filter != 'all':
        query = query.filter_by(feedback_type=type_filter)
    
    feedback_list = query.order_by(UserFeedback.created_at.desc()).limit(100).all()
    pending_count = UserFeedback.query.filter_by(status='new').count()
    
    return render_template('feedback/admin.html', 
                           feedback_list=feedback_list,
                           pending_count=pending_count,
                           status_filter=status_filter,
                           type_filter=type_filter)


@feedback_bp.route('/admin/<int:feedback_id>/respond', methods=['POST'])
@login_required
def admin_respond(feedback_id):
    """Responder a un feedback"""
    if not current_user.is_admin:
        return jsonify({'success': False, 'error': 'Unauthorized'}), 403
    
    feedback = UserFeedback.query.get_or_404(feedback_id)
    response = request.form.get('response', '').strip()
    
    if not response:
        return jsonify({'success': False, 'error': 'Response required'}), 400
    
    feedback.admin_response = response
    feedback.responded_at = datetime.utcnow()
    feedback.status = 'resolved'
    
    db.session.commit()
    
    flash('Respuesta enviada', 'success')
    return redirect(url_for('feedback.admin_list'))


@feedback_bp.route('/admin/<int:feedback_id>/dismiss', methods=['POST'])
@login_required
def admin_dismiss(feedback_id):
    """Descartar un feedback"""
    if not current_user.is_admin:
        return jsonify({'success': False, 'error': 'Unauthorized'}), 403
    
    feedback = UserFeedback.query.get_or_404(feedback_id)
    feedback.status = 'dismissed'
    
    db.session.commit()
    
    return jsonify({'success': True})
