from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from app.models import (
    ThematicScenario, ScenarioVocabulary, ScenarioPhrase, 
    SimulationStep, UserScenarioProgress
)
from app.decorators import require_scenario_access, adults_only
from app.services.roleplay_simulator import create_sample_scenario
from app.extensions import db

scenarios_bp = Blueprint('scenarios', __name__, url_prefix='/scenarios')

@scenarios_bp.route('/')
@login_required
@adults_only
def list_scenarios():
    """Muestra todos los escenarios disponibles en la tienda/catálogo"""
    scenarios = ThematicScenario.query.filter_by(is_active=True).all()
    return render_template('scenarios/list.html', scenarios=scenarios)

@scenarios_bp.route('/<int:scenario_id>/preview')
@login_required
def preview(scenario_id):
    """Página de venta/información del escenario (antes de comprar)"""
    scenario = ThematicScenario.query.get_or_404(scenario_id)
    # Si ya lo tiene comprado o es premium, lo mandamos directo al dashboard
    if current_user.has_access_to_scenario(scenario_id):
        return redirect(url_for('scenarios.dashboard', scenario_id=scenario.id))
        
    return render_template('scenarios/preview.html', scenario=scenario)

@scenarios_bp.route('/<int:scenario_id>/dashboard')
@login_required
@require_scenario_access
def dashboard(scenario_id):
    """El hub principal del escenario (Solo entran los que pagaron o son Premium)"""
    scenario = ThematicScenario.query.get_or_404(scenario_id)
    
    # Obtenemos todo el contenido relacionado a este escenario específico
    vocabulary = ScenarioVocabulary.query.filter_by(scenario_id=scenario_id).all()
    phrases = ScenarioPhrase.query.filter_by(scenario_id=scenario_id).order_by(ScenarioPhrase.order).all()
    
    # Verificar si hay pasos de simulación
    has_simulation = SimulationStep.query.filter_by(scenario_id=scenario_id).count() > 0
    
    # Si no hay simulación, crear datos de ejemplo (solo para demo)
    if not has_simulation:
        # Crear datos de ejemplo automáticamente
        create_sample_scenario(scenario_id)
        has_simulation = True
    
    # Progreso del usuario
    progress = UserScenarioProgress.query.filter_by(
        user_id=current_user.id,
        scenario_id=scenario_id
    ).first()
    
    return render_template('scenarios/dashboard.html', 
                           scenario=scenario, 
                           vocabulary=vocabulary, 
                           phrases=phrases,
                           has_simulation=has_simulation,
                           progress=progress)


@scenarios_bp.route('/<int:scenario_id>/simulate')
@login_required
@require_scenario_access
def simulate(scenario_id):
    """Página del simulador de roleplay"""
    scenario = ThematicScenario.query.get_or_404(scenario_id)
    
    # Verificar que hay pasos de simulación
    has_simulation = SimulationStep.query.filter_by(scenario_id=scenario_id).count() > 0
    
    if not has_simulation:
        # Crear datos de ejemplo
        create_sample_scenario(scenario_id)
    
    return render_template('scenarios/simulation.html', scenario=scenario)