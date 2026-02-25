"""
Rutas para Certificados
======================
"""

from flask import Blueprint, render_template, send_file, request, flash, redirect, url_for
from flask_login import login_required, current_user
from app.models import Certificate, ThematicScenario, UserScenarioProgress
from app.services.certificate_generator import CertificateGenerator
from app.extensions import db

certificates_bp = Blueprint('certificates', __name__, url_prefix='/certificates')


@certificates_bp.route('/')
@login_required
def list_certificates():
    """Lista de certificados del usuario"""
    certificates = Certificate.query.filter_by(
        user_id=current_user.id,
        is_active=True
    ).order_by(Certificate.issue_date.desc()).all()
    
    return render_template('certificates/list.html', certificates=certificates)


@certificates_bp.route('/<int:certificate_id>')
@login_required
def view_certificate(certificate_id):
    """Ver detalles de un certificado"""
    certificate = Certificate.query.get_or_404(certificate_id)
    
    # Verificar propiedad
    if certificate.user_id != current_user.id and not current_user.is_admin:
        flash('No tienes acceso a este certificado', 'danger')
        return redirect(url_for('certificates.list_certificates'))
    
    generator = CertificateGenerator()
    generator.certificate = certificate
    generator.user = certificate.user
    html_content = generator.get_certificate_html()
    
    return render_template(
        'certificates/view.html', 
        certificate=certificate,
        html_content=html_content
    )


@certificates_bp.route('/<int:certificate_id>/download')
@login_required
def download_certificate(certificate_id):
    """Descargar certificado en PDF"""
    certificate = Certificate.query.get_or_404(certificate_id)
    
    # Verificar propiedad
    if certificate.user_id != current_user.id and not current_user.is_admin:
        flash('No tienes acceso a este certificado', 'danger')
        return redirect(url_for('certificates.list_certificates'))
    
    generator = CertificateGenerator()
    certificate.user = certificate.user
    pdf_bytes = generator.generate_pdf_bytes()
    
    return send_file(
        io.BytesIO(pdf_bytes),
        mimetype='application/pdf',
        as_attachment=True,
        download_name=f'certificate_{certificate.certificate_number}.pdf'
    )


@certificates_bp.route('/verify', methods=['GET', 'POST'])
def verify():
    """Verificar un certificado"""
    certificate_number = request.args.get('certificate_number') or request.form.get('certificate_number')
    verification_code = request.args.get('verification_code') or request.form.get('verification_code')
    
    result = None
    error = None
    
    if certificate_number and verification_code:
        generator = CertificateGenerator()
        result, error = generator.verify_certificate(certificate_number, verification_code)
    
    return render_template('certificates/verify.html', result=result, error=error)


@certificates_bp.route('/claim/scenario/<int:scenario_id>', methods=['POST'])
@login_required
def claim_scenario_certificate(scenario_id):
    """Reclamar certificado por completar un escenario"""
    scenario = ThematicScenario.query.get_or_404(scenario_id)
    
    # Verificar que completó el escenario
    progress = UserScenarioProgress.query.filter_by(
        user_id=current_user.id,
        scenario_id=scenario_id
    ).first()
    
    if not progress or not progress.is_completed:
        flash('Debes completar el escenario primero', 'warning')
        return redirect(url_for('scenarios.dashboard', scenario_id=scenario_id))
    
    # Verificar si ya tiene certificado
    existing = Certificate.query.filter_by(
        user_id=current_user.id,
        scenario_id=scenario_id,
        certificate_type='scenario_master',
        is_active=True
    ).first()
    
    if existing:
        flash('Ya tienes un certificado para este escenario', 'info')
        return redirect(url_for('certificates.view_certificate', certificate_id=existing.id))
    
    # Generar certificado
    generator = CertificateGenerator()
    certificate, error = generator.generate_certificate(
        user_id=current_user.id,
        certificate_type='scenario_master',
        title=f'Master of {scenario.title}',
        course_name=f'Thematic Scenario: {scenario.title}',
        scenario_id=scenario_id,
        expiry_months=12
    )
    
    if error:
        flash(f'Error al generar certificado: {error}', 'danger')
    else:
        flash('¡Felicidades! Tu certificado ha sido generado', 'success')
    
    return redirect(url_for('certificates.view_certificate', certificate_id=certificate.id))


@certificates_bp.route('/api/verify', methods=['GET'])
def api_verify():
    """API para verificar certificados"""
    certificate_number = request.args.get('certificate_number')
    verification_code = request.args.get('verification_code')
    
    if not certificate_number or not verification_code:
        return {'success': False, 'error': 'Missing parameters'}, 400
    
    generator = CertificateGenerator()
    result, error = generator.verify_certificate(certificate_number, verification_code)
    
    if error:
        if result is None:
            return {'success': False, 'error': 'Certificate not found'}, 404
        return {'success': False, 'warning': error, 'data': result}, 200
    
    return {
        'success': True,
        'data': {
            'valid': True,
            'user_name': result['user_name'],
            'title': result['title'],
            'issue_date': result['issue_date'].isoformat() if result['issue_date'] else None,
            'expiry_date': result['expiry_date'].isoformat() if result['expiry_date'] else None
        }
    }, 200


# Importar io para el download
import io
