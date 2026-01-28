from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    """Página principal"""
    return render_template('index.html')

@main_bp.route('/about')
def about():
    """Página de información"""
    return render_template('about.html')

@main_bp.route('/contact')
def contact():
    """Página de contacto"""
    return render_template('contact.html')
