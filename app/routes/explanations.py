"""
Rutas para acceder a las explicaciones de unidades y temas.
"""

from flask import Blueprint, render_template, abort
from app.models import Unit, Topic, UnitExplanation, TopicExplanation
from flask_login import login_required

explanations_bp = Blueprint('explanations', __name__, url_prefix='/explanations')


@explanations_bp.route('/unit/<int:unit_id>')
@login_required
def unit_explanation(unit_id):
    """Mostrar explicación detallada de una unidad"""
    unit = Unit.query.get_or_404(unit_id)
    explanations = UnitExplanation.query.filter_by(unit_id=unit_id).order_by(UnitExplanation.order).all()
    
    return render_template('explanations/unit_explanation.html', 
                         unit=unit, 
                         explanations=explanations)


@explanations_bp.route('/topic/<int:topic_id>')
@login_required
def topic_explanation(topic_id):
    """Mostrar explicación detallada de un tema"""
    topic = Topic.query.get_or_404(topic_id)
    unit = topic.unit
    explanations = TopicExplanation.query.filter_by(topic_id=topic_id).order_by(TopicExplanation.order).all()
    
    return render_template('explanations/topic_explanation.html', 
                         unit=unit,
                         topic=topic, 
                         explanations=explanations)
