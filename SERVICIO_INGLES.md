# 📋 Documentación del Servicio ingles.service

## 📊 Estado Actual
- **Estado:** ✅ Activo y funcionando
- **URL:** https://ingles.jaripeo.online
- **Última verificación:** 8 de febrero de 2026

## 🔧 Configuración del Servicio Systemd

**Archivo:** `/etc/systemd/system/ingles.service`

```ini
[Unit]
Description=Gunicorn service for English Review Platform
After=network.target postgresql.service
Wants=postgresql.service

[Service]
Type=simple
User=www-data
Group=www-data
WorkingDirectory=/var/www/english-review
Environment="PATH=/var/www/english-review/venv/bin"
EnvironmentFile=/var/www/english-review/.env

ExecStart=/var/www/english-review/venv/bin/gunicorn \
    --workers 4 \
    --worker-class sync \
    --bind unix:/var/www/english-review/ingles.sock \
    --timeout 30 \
    --access-logfile /var/log/english-review/access.log \
    --error-logfile /var/log/english-review/error.log \
    --log-level info \
    run:app

Restart=always
RestartSec=10
LimitNOFILE=65535
LimitNPROC=4096
UMask=0002

[Install]
WantedBy=multi-user.target
```

## 🌐 Configuración de Nginx

**Archivo:** `/etc/nginx/sites-available/ingles.jaripeo.online`

```nginx
upstream ingles_app {
    server unix:/var/www/english-review/ingles.sock fail_timeout=0;
}

server {
    listen 80;
    listen [::]:80;
    server_name ingles.jaripeo.online www.ingles.jaripeo.online;

    # Logs
    access_log /var/log/nginx/ingles.jaripeo.online_access.log;
    error_log /var/log/nginx/ingles.jaripeo.online_error.log;

    client_max_body_size 20M;

    location / {
        proxy_pass http://unix:/var/www/english-review/ingles.sock;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto https;
        proxy_redirect off;
        proxy_connect_timeout 60s;
        proxy_send_timeout 60s;
        proxy_read_timeout 60s;
    }

    location /static/ {
        alias /var/www/english-review/app/static/;
        expires 30d;
        add_header Cache-Control "public, immutable";
    }

    location /media/ {
        alias /var/www/english-review/app/media/;
        expires 7d;
        add_header Cache-Control "public";
    }
}
```

## 🛠️ Comandos de Administración

### Estado del servicio
```bash
sudo systemctl status ingles.service
```

### Reiniciar servicio
```bash
sudo systemctl restart ingles.service
```

### Ver logs en tiempo real
```bash
# Logs de la aplicación
sudo tail -f /var/log/english-review/error.log
sudo tail -f /var/log/english-review/access.log

# Logs de Nginx
sudo tail -f /var/log/nginx/ingles.jaripeo.online_error.log
```

### Detener servicio
```bash
sudo systemctl stop ingles.service
```

### Habilitar inicio automático
```bash
sudo systemctl enable ingles.service
```

## 🔍 Verificación de Rutas

| Ruta | Estado | Descripción |
|------|--------|-------------|
| `/` | ✅ 200 | Página principal |
| `/dashboard/` | ✅ 200 | Panel de usuario |
| `/grammar/` | ✅ 200 | Sección de gramática |
| `/games/` | ✅ 200 | Juegos interactivos |

## 🐛 Solución de Problemas

### Error de permisos en el socket
```bash
sudo chown -R $(whoami):$(whoami) /var/www/english-review
sudo systemctl restart ingles.service
```

### Error 502 Bad Gateway
1. Verificar que el servicio esté corriendo:
   ```bash
   sudo systemctl status ingles.service
   ```
2. Verificar permisos del socket:
   ```bash
   ls -la /var/www/english-review/ingles.sock
   ```
3. Reiniciar ambos servicios:
   ```bash
   sudo systemctl restart ingles.service
   sudo systemctl restart nginx
   ```

### Error de conexión a PostgreSQL
1. Verificar que PostgreSQL esté corriendo:
   ```bash
   sudo systemctl status postgresql
   ```
2. Verificar las credenciales en `.env`

## 📁 Estructura de Archivos Importantes

```
/var/www/english-review/
├── .env                    # Variables de entorno
├── run.py                  # Punto de entrada de la app
├── ingles.sock            # Socket Unix de Gunicorn
├── venv/                  # Entorno virtual Python
└── app/
    ├── __init__.py        # Inicialización de Flask
    ├── static/            # Archivos estáticos
    └── templates/         # Plantillas HTML

/var/log/english-review/
├── access.log             # Logs de acceso
└── error.log              # Logs de errores

/etc/systemd/system/
└── ingles.service         # Configuración del servicio

/etc/nginx/sites-available/
└── ingles.jaripeo.online  # Configuración de Nginx
```

## 📅 Historial de Cambios

- **2026-02-08:** Verificación completa del servicio después de actualización
- **2026-02-04:** Migración a PostgreSQL
- **2026-01-29:** Configuración inicial del servicio
