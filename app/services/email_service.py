"""
Servicio de envío de correos electrónicos
"""
from flask import current_app, render_template_string
from flask_mail import Message
from threading import Thread
from app.extensions import mail

def send_async_email(app, msg):
    """Enviar email de forma asíncrona"""
    with app.app_context():
        try:
            mail.send(msg)
            app.logger.info(f"Email enviado a {msg.recipients}")
        except Exception as e:
            app.logger.error(f"Error enviando email: {e}")

def send_email(subject, recipient, html_body, text_body=None):
    """
    Enviar un correo electrónico
    
    Args:
        subject: Asunto del correo
        recipient: Email del destinatario
        html_body: Cuerpo del mensaje en HTML
        text_body: Cuerpo del mensaje en texto plano (opcional)
    """
    try:
        sender = current_app.config.get('MAIL_DEFAULT_SENDER') or current_app.config.get('MAIL_USERNAME')
        msg = Message(
            subject=subject,
            sender=sender,
            recipients=[recipient],
            html=html_body,
            body=text_body or html_body
        )
        
        # Enviar de forma asíncrona para no bloquear la respuesta
        Thread(
            target=send_async_email,
            args=(current_app._get_current_object(), msg)
        ).start()
        
        return True
    except Exception as e:
        current_app.logger.error(f"Error preparando email: {e}")
        return False

def send_welcome_email(user):
    """
    Enviar correo de bienvenida a un nuevo usuario
    
    Args:
        user: Objeto User con email y username
    """
    subject = "🎉 ¡Bienvenido a English Learning Platform!"
    
    html_body = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <style>
            body {{
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                line-height: 1.6;
                color: #333;
                max-width: 600px;
                margin: 0 auto;
                padding: 20px;
            }}
            .header {{
                background: linear-gradient(135deg, #0066cc, #004499);
                color: white;
                padding: 30px;
                text-align: center;
                border-radius: 10px 10px 0 0;
            }}
            .content {{
                background: #f9f9f9;
                padding: 30px;
                border: 1px solid #ddd;
            }}
            .button {{
                display: inline-block;
                background: #0066cc;
                color: white;
                padding: 12px 30px;
                text-decoration: none;
                border-radius: 5px;
                margin: 20px 0;
            }}
            .features {{
                background: white;
                padding: 20px;
                border-radius: 8px;
                margin: 20px 0;
            }}
            .feature-item {{
                padding: 10px 0;
                border-bottom: 1px solid #eee;
            }}
            .footer {{
                text-align: center;
                padding: 20px;
                color: #666;
                font-size: 12px;
            }}
        </style>
    </head>
    <body>
        <div class="header">
            <h1>🎓 English Learning Platform</h1>
            <p>Tu camino hacia el dominio del inglés comienza aquí</p>
        </div>
        
        <div class="content">
            <h2>¡Hola {user.full_name or user.username}! 👋</h2>
            
            <p>¡Gracias por registrarte en <strong>English Learning Platform</strong>! 
            Estamos emocionados de acompañarte en tu viaje de aprendizaje del inglés.</p>
            
            <div class="features">
                <h3>🚀 Lo que puedes hacer:</h3>
                <div class="feature-item">📚 <strong>12+ Unidades</strong> - Desde nivel básico hasta avanzado</div>
                <div class="feature-item">🎮 <strong>Juegos interactivos</strong> - Aprende jugando</div>
                <div class="feature-item">📖 <strong>Lecturas</strong> - Mejora tu comprensión</div>
                <div class="feature-item">✍️ <strong>Ejercicios de escritura</strong> - Practica tu gramática</div>
                <div class="feature-item">🏆 <strong>Logros y badges</strong> - Celebra tu progreso</div>
                <div class="feature-item">📊 <strong>Estadísticas</strong> - Visualiza tu avance</div>
            </div>
            
            <p style="text-align: center;">
                <a href="https://ingles.jaripeo.online/dashboard" class="button">
                    🎯 Comenzar a Aprender
                </a>
            </p>
            
            <h3>💡 Consejos para empezar:</h3>
            <ol>
                <li>Comienza con la <strong>Unidad 1</strong> si eres principiante</li>
                <li>Practica <strong>15 minutos diarios</strong> para mejores resultados</li>
                <li>Usa los <strong>flashcards</strong> para memorizar vocabulario</li>
                <li>No tengas miedo de cometer errores, ¡son parte del aprendizaje!</li>
            </ol>
            
            <p>Si tienes alguna pregunta, no dudes en contactarnos.</p>
            
            <p>¡Mucho éxito en tu aprendizaje! 🌟</p>
            
            <p><strong>El equipo de English Learning Platform</strong></p>
        </div>
        
        <div class="footer">
            <p>Este correo fue enviado a {user.email}</p>
            <p>© 2026 English Learning Platform - ingles.jaripeo.online</p>
        </div>
    </body>
    </html>
    """
    
    text_body = f"""
    ¡Bienvenido a English Learning Platform!
    
    Hola {user.full_name or user.username},
    
    ¡Gracias por registrarte! Estamos emocionados de acompañarte en tu viaje de aprendizaje del inglés.
    
    Lo que puedes hacer:
    - 12+ Unidades desde nivel básico hasta avanzado
    - Juegos interactivos para aprender jugando
    - Lecturas para mejorar tu comprensión
    - Ejercicios de escritura
    - Logros y badges
    - Estadísticas de tu progreso
    
    Visita: https://ingles.jaripeo.online/dashboard
    
    ¡Mucho éxito en tu aprendizaje!
    
    El equipo de English Learning Platform
    """
    
    return send_email(subject, user.email, html_body, text_body)

def send_password_reset_email(user, reset_token):
    """
    Enviar correo para restablecer contraseña
    
    Args:
        user: Objeto User
        reset_token: Token para restablecer contraseña
    """
    subject = "🔐 Restablecer tu contraseña - English Learning Platform"
    
    reset_url = f"https://ingles.jaripeo.online/auth/reset-password/{reset_token}"
    
    html_body = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <style>
            body {{
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                line-height: 1.6;
                color: #333;
                max-width: 600px;
                margin: 0 auto;
                padding: 20px;
            }}
            .header {{
                background: #dc3545;
                color: white;
                padding: 20px;
                text-align: center;
                border-radius: 10px 10px 0 0;
            }}
            .content {{
                background: #f9f9f9;
                padding: 30px;
                border: 1px solid #ddd;
            }}
            .button {{
                display: inline-block;
                background: #0066cc;
                color: white;
                padding: 12px 30px;
                text-decoration: none;
                border-radius: 5px;
                margin: 20px 0;
            }}
            .warning {{
                background: #fff3cd;
                border: 1px solid #ffc107;
                padding: 15px;
                border-radius: 5px;
                margin: 20px 0;
            }}
        </style>
    </head>
    <body>
        <div class="header">
            <h1>🔐 Restablecer Contraseña</h1>
        </div>
        
        <div class="content">
            <h2>Hola {user.username},</h2>
            
            <p>Recibimos una solicitud para restablecer la contraseña de tu cuenta.</p>
            
            <p style="text-align: center;">
                <a href="{reset_url}" class="button">
                    Restablecer mi contraseña
                </a>
            </p>
            
            <div class="warning">
                ⚠️ Este enlace expirará en <strong>1 hora</strong>.
            </div>
            
            <p>Si no solicitaste restablecer tu contraseña, puedes ignorar este correo.</p>
            
            <p><strong>El equipo de English Learning Platform</strong></p>
        </div>
    </body>
    </html>
    """
    
    return send_email(subject, user.email, html_body)
