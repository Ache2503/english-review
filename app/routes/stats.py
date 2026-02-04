"""
Rutas para el dashboard de estadísticas con visualizaciones.
"""

from flask import Blueprint, render_template, jsonify, request
from flask_login import login_required, current_user
from app.services.statistics import (
    get_activity_heatmap,
    get_weekly_progress,
    get_performance_by_skill,
    get_study_time_distribution,
    get_streak_history,
    get_unit_progress_breakdown,
    get_comprehensive_stats
)

stats_bp = Blueprint('stats', __name__, url_prefix='/stats')


@stats_bp.route('/')
@login_required
def index():
    """Dashboard principal de estadísticas"""
    stats = get_comprehensive_stats(current_user.id)
    return render_template('stats/dashboard.html', stats=stats)


@stats_bp.route('/api/heatmap')
@login_required
def api_heatmap():
    """API para datos del heatmap de actividad"""
    days = request.args.get('days', 365, type=int)
    data = get_activity_heatmap(current_user.id, days)
    return jsonify(data)


@stats_bp.route('/api/weekly')
@login_required
def api_weekly():
    """API para datos de progreso semanal"""
    weeks = request.args.get('weeks', 12, type=int)
    data = get_weekly_progress(current_user.id, weeks)
    return jsonify(data)


@stats_bp.route('/api/skills')
@login_required
def api_skills():
    """API para rendimiento por habilidad"""
    data = get_performance_by_skill(current_user.id)
    return jsonify(data)


@stats_bp.route('/api/study-days')
@login_required
def api_study_days():
    """API para distribución de estudio por día"""
    days = request.args.get('days', 30, type=int)
    data = get_study_time_distribution(current_user.id, days)
    return jsonify(data)


@stats_bp.route('/api/units')
@login_required
def api_units():
    """API para progreso por unidad"""
    data = get_unit_progress_breakdown(current_user.id)
    return jsonify(data)


@stats_bp.route('/api/all')
@login_required
def api_all():
    """API para todas las estadísticas"""
    data = get_comprehensive_stats(current_user.id)
    return jsonify(data)
