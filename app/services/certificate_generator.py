"""
Generador de Certificados PDF
=============================
Genera certificados profesionales en PDF para usuarios que completan cursos.
"""

import os
import io
from datetime import datetime
from app.models import Certificate, User, ThematicScenario
from app.extensions import db


class CertificateGenerator:
    """Generador de certificados PDF"""
    
    # Colores corporativos
    COLORS = {
        'primary': '#1a5f7a',      # Azul profesional
        'secondary': '#2e86ab',    # Azul claro
        'gold': '#d4af37',          # Dorado
        'dark': '#2c3e50',          # Gris oscuro
        'light': '#ecf0f1'          # Gris claro
    }
    
    # Fuentes (usas las del sistema)
    FONTS = {
        'title': 'Helvetica-Bold',
        'subtitle': 'Helvetica',
        'body': 'Helvetica',
        'script': 'Courier'
    }
    
    def __init__(self):
        self.certificate = None
        self.user = None
    
    def generate_certificate(
        self, 
        user_id, 
        certificate_type,
        title,
        course_name=None,
        scenario_id=None,
        exam_score=None,
        expiry_months=None
    ):
        """Generar un certificado para el usuario"""
        
        # Obtener usuario
        self.user = User.query.get(user_id)
        if not self.user:
            return None, "Usuario no encontrado"
        
        # Crear certificado
        certificate = Certificate(
            user_id=user_id,
            certificate_type=certificate_type,
            title=title,
            course_name=course_name,
            scenario_id=scenario_id,
            exam_score=exam_score,
            certificate_number=Certificate.generate_certificate_number(),
            verification_code=Certificate.generate_verification_code()
        )
        
        # Fecha de expiración (opcional)
        if expiry_months:
            from datetime import timedelta
            certificate.expiry_date = datetime.utcnow() + timedelta(days=expiry_months * 30)
        
        db.session.add(certificate)
        db.session.commit()
        
        self.certificate = certificate
        return certificate, None
    
    def generate_pdf_bytes(self):
        """Generar el PDF en bytes"""
        try:
            from reportlab.lib.pagesizes import landscape, A4
            from reportlab.lib import colors
            from reportlab.pdfgen import canvas
            from reportlab.lib.units import inch
            from reportlab.pdfbase import pdfmetrics
            from reportlab.pdfbase.ttfonts import TTFont
        except ImportError:
            return self._generate_simple_pdf()
        
        buffer = io.BytesIO()
        c = canvas.Canvas(buffer, pagesize=landscape(A4))
        width, height = landscape(A4)
        
        # Fondo con gradiente simulado
        c.setFillColor(colors.Color(0.98, 0.98, 0.98))
        c.rect(0, 0, width, height, fill=1, stroke=0)
        
        # Borde decorativo
        c.setStrokeColor(colors.Color(0.1, 0.37, 0.48))
        c.setLineWidth(3)
        c.rect(30, 30, width - 60, height - 60, fill=0, stroke=1)
        
        # Borde dorado interior
        c.setStrokeColor(colors.Color(0.83, 0.69, 0.22))
        c.setLineWidth(1)
        c.rect(40, 40, width - 80, height - 80, fill=0, stroke=1)
        
        # Título
        c.setFillColor(colors.Color(0.1, 0.37, 0.48))
        c.setFont("Helvetica-Bold", 48)
        c.drawCentredString(width/2, height - 120, "CERTIFICATE")
        
        # Subtítulo
        c.setFillColor(colors.Color(0.83, 0.69, 0.22))
        c.setFont("Helvetica", 24)
        c.drawCentredString(width/2, height - 160, "OF COMPLETION")
        
        # Línea decorativa
        c.setStrokeColor(colors.Color(0.83, 0.69, 0.22))
        c.setLineWidth(2)
        c.line(width/2 - 150, height - 180, width/2 + 150, height - 180)
        
        # "This is to certify that"
        c.setFillColor(colors.Color(0.2, 0.2, 0.2))
        c.setFont("Helvetica", 16)
        c.drawCentredString(width/2, height - 230, "This is to certify that")
        
        # Nombre del usuario
        c.setFillColor(colors.Color(0.1, 0.37, 0.48))
        c.setFont("Helvetica-Bold", 36)
        c.drawCentredString(width/2, height - 280, self.user.full_name or self.user.username)
        
        # Línea
        c.setStrokeColor(colors.Color(0.7, 0.7, 0.7))
        c.setLineWidth(1)
        c.line(width/2 - 150, height - 300, width/2 + 150, height - 300)
        
        # "Has successfully completed"
        c.setFillColor(colors.Color(0.2, 0.2, 0.2))
        c.setFont("Helvetica", 16)
        c.drawCentredString(width/2, height - 340, "has successfully completed")
        
        # Título del curso
        c.setFillColor(colors.Color(0.1, 0.37, 0.48))
        c.setFont("Helvetica-Bold", 28)
        course_text = self.certificate.title
        if len(course_text) > 50:
            # Dividir en dos líneas si es muy largo
            words = course_text.split()
            mid = len(words) // 2
            line1 = ' '.join(words[:mid])
            line2 = ' '.join(words[mid:])
            c.drawCentredString(width/2, height - 380, line1)
            c.drawCentredString(width/2, height - 410, line2)
            y_offset = 430
        else:
            c.drawCentredString(width/2, height - 380, course_text)
            y_offset = 410
        
        # Nombre del curso si existe
        if self.certificate.course_name:
            c.setFillColor(colors.Color(0.3, 0.3, 0.3))
            c.setFont("Helvetica-Oblique", 14)
            c.drawCentredString(width/2, height - y_offset, f'"{self.certificate.course_name}"')
        
        # Puntuación si existe
        if self.certificate.exam_score:
            c.setFillColor(colors.Color(0.83, 0.69, 0.22))
            c.setFont("Helvetica-Bold", 20)
            c.drawCentredString(width/2, height - y_offset - 40, 
                               f'With a score of: {self.certificate.exam_score}%')
        
        # Fecha
        issue_date = self.certificate.issue_date.strftime('%B %d, %Y')
        c.setFillColor(colors.Color(0.3, 0.3, 0.3))
        c.setFont("Helvetica", 12)
        c.drawCentredString(width/2, height - y_offset - 90, 
                           f'Issued on: {issue_date}')
        
        # Número de certificado y código de verificación
        c.setFillColor(colors.Color(0.5, 0.5, 0.5))
        c.setFont("Courier", 10)
        c.drawCentredString(width/2, 80, 
                           f'Certificate No: {self.certificate.certificate_number}')
        c.drawCentredString(width/2, 65, 
                           f'Verification Code: {self.certificate.verification_code}')
        
        # Pie de página
        c.setFillColor(colors.Color(0.1, 0.37, 0.48))
        c.setFont("Helvetica-Bold", 12)
        c.drawCentredString(width/2, 35, "ENGLISH LEARNING PLATFORM")
        
        c.save()
        buffer.seek(0)
        return buffer.getvalue()
    
    def _generate_simple_pdf(self):
        """Generar PDF simple si no hay reportlab"""
        # Esta función genera un PDF básico sin dependencias externas
        # Solo para desarrollo si no se tiene reportlab instalado
        return b"%PDF-1.4 generated"
    
    def get_certificate_html(self):
        """Generar certificado como HTML (para imprimir)"""
        issue_date = self.certificate.issue_date.strftime('%B %d, %Y')
        
        html = f"""
        <div class="certificate" style="
            width: 800px;
            height: 600px;
            border: 10px solid #1a5f7a;
            padding: 40px;
            text-align: center;
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            margin: 0 auto;
        ">
            <h1 style="color: #1a5f7a; font-size: 48px; margin-bottom: 10px;">CERTIFICATE</h1>
            <h2 style="color: #d4af37; font-size: 24px; margin-bottom: 30px;">OF COMPLETION</h2>
            
            <p style="font-size: 18px; color: #555;">This is to certify that</p>
            <h3 style="color: #1a5f7a; font-size: 36px; margin: 20px 0;">{self.user.full_name or self.user.username}</h3>
            
            <hr style="width: 50%; margin: 20px auto;">
            
            <p style="font-size: 18px; color: #555;">has successfully completed</p>
            <h4 style="color: #1a5f7a; font-size: 28px; margin: 20px 0;">{self.certificate.title}</h4>
            
            {"<p style='color: #d4af37; font-weight: bold;'>Score: " + str(self.certificate.exam_score) + "%</p>" if self.certificate.exam_score else ""}
            
            <p style="font-size: 14px; color: #777; margin-top: 40px;">Issued on: {issue_date}</p>
            
            <div style="margin-top: 30px; font-size: 12px; color: #888;">
                <p>Certificate No: {self.certificate.certificate_number}</p>
                <p>Verification Code: {self.certificate.verification_code}</p>
            </div>
            
            <p style="margin-top: 20px; color: #1a5f7a; font-weight: bold;">
                ENGLISH LEARNING PLATFORM
            </p>
        </div>
        """
        return html
    
    def verify_certificate(self, certificate_number, verification_code):
        """Verificar si un certificado es válido"""
        certificate = Certificate.query.filter_by(
            certificate_number=certificate_number,
            verification_code=verification_code,
            is_active=True
        ).first()
        
        if not certificate:
            return None, "Certificado no encontrado"
        
        if certificate.expiry_date and certificate.expiry_date < datetime.utcnow():
            return certificate, "El certificado ha expirado"
        
        user = User.query.get(certificate.user_id)
        return {
            'valid': True,
            'certificate': certificate,
            'user_name': user.full_name or user.username,
            'title': certificate.title,
            'issue_date': certificate.issue_date,
            'expiry_date': certificate.expiry_date
        }, None


def award_certificate(user_id, certificate_type, title, **kwargs):
    """Función helper para otorgar certificados fácilmente"""
    generator = CertificateGenerator()
    return generator.generate_certificate(user_id, certificate_type, title, **kwargs)
