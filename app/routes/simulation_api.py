"""
API para Simulador Roleplay
===========================
Endpoints JSON para el simulador de roleplay
"""

from flask import Blueprint, jsonify, request, session
from flask_login import login_required, current_user
from app.models import (
    ThematicScenario, SimulationStep, SimulationOption,
    SimulationAttempt, UserScenarioProgress
)
from app.services.roleplay_simulator import RoleplaySimulator, create_sample_scenario
from app.extensions import db

simulation_bp = Blueprint('simulation', __name__, url_prefix='/api/simulation')


@simulation_bp.route('/<int:scenario_id>/start', methods=['POST'])
@login_required
def start_simulation(scenario_id):
    """Iniciar una nueva simulación"""
    try:
        data = request.get_json() or {}
        difficulty = data.get('difficulty', 'normal')
        
        scenario = ThematicScenario.query.get_or_404(scenario_id)
        
        # Verificar que hay pasos de simulación
        steps_count = SimulationStep.query.filter_by(scenario_id=scenario_id).count()
        if steps_count == 0:
            return jsonify({'success': False, 'error': 'No simulation steps configured for this scenario'}), 400
        
        # Crear simulador
        simulator = RoleplaySimulator(current_user.id, scenario_id, difficulty)
        step_data, error = simulator.start_attempt()
        
        if error:
            return jsonify({'success': False, 'error': error}), 400
        
        if not step_data:
            return jsonify({'success': False, 'error': 'Failed to create simulation step'}), 500
        
        # Guardar estado en sesión
        session[f'simulator_{scenario_id}'] = {
            'attempt_id': simulator.attempt.id,
            'current_step_id': step_data['step_id']
        }
        session.modified = True
        
        return jsonify({
            'success': True,
            'data': {
                'attempt_id': simulator.attempt.id,
                'step': step_data,
                'scenario': {
                    'title': scenario.title,
                    'difficulty': difficulty
                }
            }
        })
        
    except Exception as e:
        import traceback
        error_msg = f'Server error: {str(e)}'
        print(f"ERROR in start_simulation: {error_msg}")
        print(traceback.format_exc())
        return jsonify({'success': False, 'error': error_msg}), 500


@simulation_bp.route('/<int:scenario_id>/step/<int:step_id>', methods=['GET'])
@login_required
def get_step(scenario_id, step_id):
    """Obtener un paso específico"""
    step = SimulationStep.query.get_or_404(step_id)
    
    if step.scenario_id != scenario_id:
        return jsonify({'success': False, 'error': 'Step not found'}), 404
    
    # Obtener opciones
    options = SimulationOption.query.filter_by(
        step_id=step_id
    ).order_by(SimulationOption.order).all()
    
    return jsonify({
        'success': True,
        'data': {
            'step_id': step.id,
            'order': step.step_order,
            'message': step.customer_message,
            'mood': step.customer_mood,
            'context': step.situation_context,
            'audio_url': step.audio_url,
            'time_limit': step.time_limit_seconds,
            'points': step.points_value,
            'is_final': step.is_final_step,
            'options': [
                {
                    'id': opt.id,
                    'text': opt.option_text,
                    'order': opt.order
                }
                for opt in options
            ]
        }
    })


@simulation_bp.route('/<int:scenario_id>/answer', methods=['POST'])
@login_required
def submit_answer(scenario_id):
    """Enviar respuesta de un paso"""
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({'success': False, 'error': 'No data provided'}), 400
        
        step_id = data.get('step_id')
        option_id = data.get('option_id')
        time_taken = data.get('time_taken')
        attempt_id = data.get('attempt_id')  # Ahora también aceptamos el attempt_id desde el cliente
        
        if not step_id or not option_id:
            return jsonify({'success': False, 'error': f'Missing parameters: step_id={step_id}, option_id={option_id}'}), 400
        
        #优先使用客户端提供的attempt_id，也可以从会话中获取
        if not attempt_id:
            session_key = f'simulator_{scenario_id}'
            session_data = session.get(session_key)
            if session_data:
                attempt_id = session_data.get('attempt_id')
        
        if not attempt_id:
            return jsonify({'success': False, 'error': 'No active simulation. Please start a new simulation.'}), 400
            
        attempt = SimulationAttempt.query.get(attempt_id)
        
        if not attempt:
            return jsonify({'success': False, 'error': 'Simulation attempt not found in database'}), 404
        
        # Crear simulador y cargar estado del attempt
        simulator = RoleplaySimulator(current_user.id, scenario_id, attempt.difficulty_level)
        simulator.attempt = attempt
        # Cargar estado del mood desde el attempt
        simulator.current_mood = attempt.final_mood or 'neutral'
        simulator.mood_score = attempt.mood_score or 75
        
        # Procesar respuesta
        result, error = simulator.submit_answer(step_id, option_id, time_taken)
        
        if error:
            return jsonify({'success': False, 'error': error}), 400
        
        if not result:
            return jsonify({'success': False, 'error': 'No result returned'}), 500
        
        # Actualizar sesión
        try:
            session_key = f'simulator_{scenario_id}'
            session_data = session.get(session_key)
            if session_data:
                next_step_id = None
                if result.get('next_step') and result['next_step']:
                    next_step_id = result['next_step'].get('step_id')
                session_data['current_step_id'] = next_step_id
                session[session_key] = session_data
                session.modified = True
        except Exception as session_err:
            print(f"Session update error (non-critical): {session_err}")
        
        response_data = {
            'feedback': result['feedback'],
            'is_complete': result['is_complete']
        }
        
        if result.get('next_step'):
            response_data['next_step'] = result['next_step']
        
        response = {
            'success': True,
            'data': response_data
        }
        
        return jsonify(response)
        
    except Exception as e:
        import traceback
        error_msg = f'Server error: {str(e)}'
        print(f"ERROR in submit_answer: {error_msg}")
        print(traceback.format_exc())
        return jsonify({'success': False, 'error': error_msg}), 500


@simulation_bp.route('/<int:scenario_id>/complete', methods=['POST'])
@login_required
def complete_simulation(scenario_id):
    """Finalizar la simulación"""
    session_key = f'simulator_{scenario_id}'
    session_data = session.get(session_key)
    
    if not session_data:
        return jsonify({'success': False, 'error': 'No active simulation'}), 400
    
    attempt_id = session_data.get('attempt_id')
    attempt = SimulationAttempt.query.get(attempt_id)
    
    if not attempt:
        return jsonify({'success': False, 'error': 'Simulation not found'}), 404
    
    simulator = RoleplaySimulator(current_user.id, scenario_id, attempt.difficulty_level)
    simulator.attempt = attempt
    
    # Completar simulación
    result = simulator.complete_attempt()
    
    # Limpiar sesión
    session.pop(session_key, None)
    
    return jsonify({
        'success': True,
        'data': result
    })


@simulation_bp.route('/<int:scenario_id>/status', methods=['GET'])
@login_required
def get_status(scenario_id):
    """Obtener estado actual de la simulación"""
    session_key = f'simulator_{scenario_id}'
    session_data = session.get(session_key)
    
    if not session_data:
        return jsonify({
            'success': True,
            'data': {'active': False}
        })
    
    attempt_id = session_data.get('attempt_id')
    attempt = SimulationAttempt.query.get(attempt_id)
    
    if not attempt:
        return jsonify({
            'success': True,
            'data': {'active': False}
        })
    
    return jsonify({
        'success': True,
        'data': {
            'active': True,
            'attempt_id': attempt.id,
            'steps_completed': attempt.steps_completed,
            'total_points': attempt.total_points,
            'current_mood': attempt.final_mood or 'neutral'
        }
    })


@simulation_bp.route('/<int:scenario_id>/setup-sample', methods=['POST'])
@login_required
def setup_sample_scenario(scenario_id):
    """Crear datos de ejemplo para un escenario (solo admin)"""
    if not current_user.is_admin:
        return jsonify({'success': False, 'error': 'Unauthorized'}), 403
    
    # Verificar si ya hay pasos
    existing = SimulationStep.query.filter_by(scenario_id=scenario_id).count()
    if existing > 0:
        return jsonify({'success': False, 'error': 'Scenario already has steps'}), 400
    
    result = create_sample_scenario(scenario_id)
    
    if result:
        return jsonify({'success': True, 'message': 'Sample scenario created'})
    
    return jsonify({'success': False, 'error': 'Failed to create sample'}), 500


@simulation_bp.route('/history', methods=['GET'])
@login_required
def get_history():
    """Obtener historial de simulaciones del usuario"""
    attempts = SimulationAttempt.query.filter_by(
        user_id=current_user.id
    ).order_by(SimulationAttempt.completed_at.desc()).limit(20).all()
    
    return jsonify({
        'success': True,
        'data': [
            {
                'id': a.id,
                'scenario_id': a.scenario_id,
                'scenario_title': ThematicScenario.query.get(a.scenario_id).title if ThematicScenario.query.get(a.scenario_id) else 'Unknown',
                'difficulty': a.difficulty_level,
                'score': a.score_percentage,
                'passed': a.passed,
                'completed_at': a.completed_at.isoformat() if a.completed_at else None,
                'steps_completed': a.steps_completed
            }
            for a in attempts
        ]
    })
