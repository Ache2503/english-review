from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
@login_required
def index():
    # Filtro mágico: Si es menor de 15, lo mandamos directo a Kids Zone
    if current_user.age < 15:
        return redirect(url_for('kids.select_profile'))
        
    # Si es mayor o igual a 15, lo redirigimos al controlador real del dashboard
    return redirect(url_for('dashboard.index'))

@main_bp.route('/about')
def about():
    """Página de información"""
    return render_template('about.html')

@main_bp.route('/contact')
def contact():
    """Página de contacto"""
    return render_template('contact.html')