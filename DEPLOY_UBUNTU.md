# 🚀 Guía de Despliegue - English Learning Platform

## Servidor Ubuntu con Nginx, Systemd y PostgreSQL

Esta guía te ayudará a desplegar la plataforma en tu servidor Ubuntu.

---

## 📋 Requisitos Previos

- Ubuntu 20.04/22.04 LTS
- Python 3.10+
- PostgreSQL 13+
- Nginx
- Git

---

## 📁 Estructura de Archivos a Modificar

```
/home/tu-usuario/english-learning-platform/
├── .env                    ← CREAR (credenciales)
├── config.py               ← Verificar configuración
├── run.py                  ← Punto de entrada
└── requirements.txt        ← Dependencias
```

---

## 1️⃣ Clonar/Actualizar el Repositorio

```bash
# Si es primera vez
cd /home/tu-usuario
git clone https://github.com/Ache2503/english-review.git english-learning-platform
cd english-learning-platform

# Si ya existe (actualizar)
cd /home/tu-usuario/english-learning-platform
git pull origin main
```

---

## 2️⃣ Crear Entorno Virtual

```bash
# Crear entorno virtual
python3 -m venv .venv

# Activar entorno
source .venv/bin/activate

# Instalar dependencias
pip install --upgrade pip
pip install -r requirements.txt

# Instalar gunicorn para producción
pip install gunicorn
```

---

## 3️⃣ Configurar Variables de Entorno (.env)

Crear el archivo `.env` en la raíz del proyecto:

```bash
nano .env
```

Contenido del archivo `.env`:

```env
# =====================================================
# CONFIGURACIÓN DE PRODUCCIÓN
# =====================================================

# Flask
FLASK_APP=run.py
FLASK_ENV=production
SECRET_KEY=tu-clave-secreta-muy-larga-y-segura-aqui

# Base de datos PostgreSQL
# Formato: postgresql://usuario:contraseña@host:puerto/nombre_db
DATABASE_URL=postgresql://english_user:tu_password@localhost:5432/english_learning

# Debug (SIEMPRE false en producción)
DEBUG=False
```

**⚠️ IMPORTANTE:** Cambia `tu-clave-secreta-muy-larga-y-segura-aqui` por una clave real y segura.

---

## 4️⃣ Configurar PostgreSQL

Si aún no has creado la base de datos:

```bash
# Conectar a PostgreSQL
sudo -u postgres psql

# Crear usuario y base de datos
CREATE USER english_user WITH PASSWORD 'tu_password';
CREATE DATABASE english_learning OWNER english_user;
GRANT ALL PRIVILEGES ON DATABASE english_learning TO english_user;
\q
```

---

## 5️⃣ Inicializar Base de Datos

```bash
# Activar entorno virtual
source .venv/bin/activate

# Ejecutar migraciones
flask db upgrade

# Poblar con datos iniciales (primera vez)
python seed_cefr_units.py
python seed_complete_content.py
python seed_extended_grammar.py
python seed_more_grammar.py
python seed_badges.py
python seed_explanations.py
python seed_unit_challenges.py
python seed_master.py
```

---

## 6️⃣ Crear Servicio Systemd

Crear el archivo de servicio:

```bash
sudo nano /etc/systemd/system/english-learning.service
```

Contenido:

```ini
[Unit]
Description=English Learning Platform
After=network.target postgresql.service
Wants=postgresql.service

[Service]
User=tu-usuario
Group=www-data
WorkingDirectory=/home/tu-usuario/english-learning-platform
Environment="PATH=/home/tu-usuario/english-learning-platform/.venv/bin"
EnvironmentFile=/home/tu-usuario/english-learning-platform/.env
ExecStart=/home/tu-usuario/english-learning-platform/.venv/bin/gunicorn \
    --workers 3 \
    --bind 127.0.0.1:5100 \
    --timeout 120 \
    --access-logfile /var/log/english-learning/access.log \
    --error-logfile /var/log/english-learning/error.log \
    "app:create_app()"
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```

**📝 Cambiar:**
- `tu-usuario` → Tu nombre de usuario en el servidor
- Ruta del proyecto si es diferente

Crear directorio de logs:

```bash
sudo mkdir -p /var/log/english-learning
sudo chown tu-usuario:www-data /var/log/english-learning
```

Habilitar e iniciar servicio:

```bash
sudo systemctl daemon-reload
sudo systemctl enable english-learning
sudo systemctl start english-learning
sudo systemctl status english-learning
```

---

## 7️⃣ Configurar Nginx

Crear archivo de configuración:

```bash
sudo nano /etc/nginx/sites-available/english-learning
```

Contenido:

```nginx
upstream english_app {
    server 127.0.0.1:5100;
}

server {
    listen 80;
    server_name ingles.jaripeo.online;  # ← CAMBIAR por tu dominio

    client_max_body_size 10M;

    access_log /var/log/nginx/english-learning-access.log;
    error_log /var/log/nginx/english-learning-error.log;

    location / {
        proxy_pass http://english_app;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_redirect off;
        
        proxy_connect_timeout 60s;
        proxy_send_timeout 60s;
        proxy_read_timeout 60s;
    }

    location /static/ {
        alias /home/tu-usuario/english-learning-platform/app/static/;
        expires 7d;
        add_header Cache-Control "public, immutable";
    }
}
```

**📝 Cambiar:**
- `ingles.jaripeo.online` → Tu dominio
- `tu-usuario` → Tu nombre de usuario

Habilitar sitio:

```bash
sudo ln -sf /etc/nginx/sites-available/english-learning /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

---

## 8️⃣ Configurar SSL con Certbot (Opcional pero Recomendado)

```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d ingles.jaripeo.online
```

---

## 🔄 Comandos Útiles

### Ver estado del servicio
```bash
sudo systemctl status english-learning
```

### Ver logs de la aplicación
```bash
sudo journalctl -u english-learning -f
# o
tail -f /var/log/english-learning/error.log
```

### Reiniciar servicio
```bash
sudo systemctl restart english-learning
```

### Actualizar código
```bash
cd /home/tu-usuario/english-learning-platform
git pull origin main
source .venv/bin/activate
pip install -r requirements.txt
flask db upgrade
sudo systemctl restart english-learning
```

---

## 📁 Archivos que DEBES Modificar

| Archivo | Qué cambiar |
|---------|-------------|
| `.env` | Credenciales de BD y SECRET_KEY |
| `/etc/systemd/system/english-learning.service` | Ruta y usuario |
| `/etc/nginx/sites-available/english-learning` | Dominio y ruta |

---

## ⚠️ Troubleshooting

### Error: "Connection refused"
```bash
# Verificar que el servicio esté corriendo
sudo systemctl status english-learning

# Verificar que el puerto esté escuchando
sudo netstat -tlnp | grep 5100
```

### Error: "502 Bad Gateway"
```bash
# Ver logs de nginx
sudo tail -f /var/log/nginx/english-learning-error.log

# Ver logs de la app
sudo tail -f /var/log/english-learning/error.log
```

### Error de base de datos
```bash
# Verificar conexión
source .venv/bin/activate
python3 -c "from app import create_app; app = create_app(); print('OK')"
```

---

## 📊 Verificar Instalación

Una vez todo configurado:

```bash
# Verificar servicio
sudo systemctl status english-learning

# Verificar nginx
sudo systemctl status nginx

# Probar localmente
curl http://127.0.0.1:5100

# Probar por dominio
curl http://ingles.jaripeo.online
```

---

## 👤 Usuarios de Prueba

| Usuario | Contraseña |
|---------|------------|
| axel | 12345678 |
| ache | 12345678 |
| testuser | 12345678 |

---

¡Listo! Tu plataforma debería estar funcionando en `http://tu-dominio.com` 🎉
