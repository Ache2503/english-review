"""
Rutas Legales (Términos y Privacidad)
====================================
"""

from flask import Blueprint, render_template
from datetime import datetime

legal_bp = Blueprint('legal', __name__)


@legal_bp.route('/terms')
def terms():
    """Términos y Condiciones"""
    return render_template('legal/terms.html', current_date=datetime.now().strftime('%d de %B de %Y'))


@legal_bp.route('/privacy')
def privacy():
    """Política de Privacidad"""
    return render_template('legal/privacy.html', current_date=datetime.now().strftime('%d de %B de %Y'))
