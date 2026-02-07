# 🚀 ADMIN DASHBOARD - COMIENZA AQUÍ

## Ejecución Local - Lista para Usar

Tu **Admin Dashboard está 100% funcional y listo para ejecutar en tu máquina local**.

---

## ⚡ Inicio en 30 Segundos

```bash
# Paso 1: Ir al directorio
cd ~/Documentos/guia_estudio/english-learning-platform

# Paso 2: Ejecutar (se inicia automáticamente)
bash run_local_admin.sh
```

**Eso es todo.** El servidor estará disponible en `http://localhost:5000`

---

## 🔑 Credenciales (Demo)

```
Usuario:     admin
Contraseña:  admin123
Email:       admin@example.com
```

---

## ✅ Qué está Incluido

| Característica | Estado | Ubicación |
|---|---|---|
| 📊 Base de Datos SQLite | ✅ | `/test_data/admin_test.db` |
| 👤 Usuario Admin | ✅ | `admin / admin123` |
| 🔐 Autenticación PBKDF2 | ✅ | `admin_dashboard/routes/` |
| 🔑 2FA/TOTP (QR) | ✅ | `admin_dashboard/routes/` |
| 📝 Auditoría | ✅ | `admin_dashboard/services/` |
| 🛡️ 10 Decoradores Seguridad | ✅ | `admin_dashboard/decorators/` |
| 📊 Dashboard Web | ✅ | `/admin/` |
| 🔗 API REST (13 endpoints) | ✅ | `/admin/*` |

---

## 🌐 URLs Disponibles (después de iniciar)

```
http://localhost:5000/                    ← Página de inicio
http://localhost:5000/admin/login         ← Login (formulario)
http://localhost:5000/admin/              ← Dashboard principal
http://localhost:5000/admin/quick-stats   ← Estadísticas
http://localhost:5000/admin/activities    ← Historial
http://localhost:5000/api/status          ← Estado del sistema (JSON)
```

---

## 📚 Documentación

### 📄 Lee Primero
1. **[QUICK_START_ADMIN.md](./QUICK_START_ADMIN.md)** - Guía rápida
2. **[ADMIN_DASHBOARD_LOCAL_SETUP.md](./ADMIN_DASHBOARD_LOCAL_SETUP.md)** - Configuración completa
3. **[ADMIN_EXECUTION_SUMMARY.md](./ADMIN_EXECUTION_SUMMARY.md)** - Resumen ejecutivo

### 📖 Documentación del Módulo
- `admin_dashboard/README.md` - Descripción del módulo
- `admin_dashboard/INSTALL.md` - Instalación
- `admin_dashboard/docs/` - Docs adicionales

---

## 🛠️ Tecnologías

- **Flask 3.0.0** - Web framework
- **SQLAlchemy 2.0.23** - ORM
- **Flask-Login 0.6.3** - Sesiones
- **pyotp 2.9.0** - 2FA/TOTP
- **qrcode 7.4.2** - QR generation
- **SQLite** - Base de datos

---

## 🐛 Si Hay Problemas

### Puerto 5000 ocupado
```bash
# Cambiar puerto en run_admin_dashboard.py línea ~120
app.run(port=5001)  # Usar otro puerto
```

### Error de módulo
```bash
# Asegurar que venv está activado
source venv/bin/activate
```

### Base de datos corrupta
```bash
# Eliminar y recrear
rm test_data/admin_test.db
python test_app.py
```

---

## 🔍 Verificar Instalación

```bash
# Ver estado del sistema
curl http://localhost:5000/api/status
```

Respuesta esperada:
```json
{
  "status": "operational",
  "database": "sqlite",
  "users": 1,
  "active_sessions": 0
}
```

---

## 📊 Estructura del Proyecto

```
english-learning-platform/
├── 00_COMIENZA_AQUI.md              ← Este archivo
├── run_local_admin.sh               ← Script de inicio
├── run_admin_dashboard.py           ← App Flask
├── test_app.py                      ← Inicializador
├── test_data/admin_test.db          ← Base de datos
└── admin_dashboard/                 ← Módulo principal
    ├── models/                      ├─ ORM (5 tablas)
    ├── routes/                      ├─ API (13 endpoints)
    ├── services/                    ├─ Lógica de negocio
    ├── decorators/                  ├─ Seguridad
    ├── templates/                   ├─ HTML
    ├── static/                      ├─ CSS/JS
    ├── config.py                    ├─ Configuración
    └── docs/                        └─ Documentación
```

---

## ⚠️ Notas Importantes

🔴 **NO usar en PRODUCCIÓN sin:**
- Cambiar credenciales
- Usar PostgreSQL o MySQL
- Configurar HTTPS
- Cambiar SECRET_KEY
- Implementar backups

---

## ✨ Características Principales

✅ **Autenticación segura** - PBKDF2 hash
✅ **2FA opcional** - TOTP/Google Authenticator
✅ **Control de acceso** - RBAC (4 roles)
✅ **Auditoría completa** - Todas las acciones registradas
✅ **Gestión de sesiones** - Múltiples dispositivos
✅ **API REST** - 13 endpoints
✅ **Dashboard web** - Interfaz HTML
✅ **Documentación** - 4000+ líneas

---

## 🎯 Próximos Pasos

### Paso 1: Iniciar
```bash
bash run_local_admin.sh
```

### Paso 2: Acceder
Abre en el navegador: **http://localhost:5000**

### Paso 3: Login
```
Usuario: admin
Contraseña: admin123
```

### Paso 4: Explorar
- Dashboard principal
- Configurar 2FA
- Ver actividades
- Probar API endpoints

---

## 💡 Tips Útiles

### Ver logs en tiempo real
```bash
tail -f test_data/admin.log  # Si existe
```

### Probar endpoint API
```bash
curl -X POST http://localhost:5000/admin/login \
  -d "username=admin&password=admin123"
```

### Cambiar puerto
Editar `run_admin_dashboard.py` línea 120 y cambiar `port=5000`

### Usar otra base de datos
Editar `run_admin_dashboard.py` línea 15 y cambiar URI de conexión

---

## 📞 Soporte

Para más detalles:
- Lee `QUICK_START_ADMIN.md`
- Consulta `ADMIN_EXECUTION_SUMMARY.md`
- Revisa `admin_dashboard/README.md`

---

## 🎉 ¡Listo!

Tu Admin Dashboard está **100% funcional** y listo para usar.

```bash
# Ejecuta esto ahora:
cd ~/Documentos/guia_estudio/english-learning-platform
bash run_local_admin.sh
```

Luego abre: **http://localhost:5000**

---

**¡Que disfrutes!** 🚀

Documentado: 2025-02-04 | Versión: 1.0.0 | Estado: ✅ PRODUCTIVO
