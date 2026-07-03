# Función: register()

## Información General

| Campo | Valor |
|-------|-------|
| **Nombre** | register() |
| **Archivo** | app/routes/auth.py |
| **Ruta** | app/routes/auth.py |
| **Tipo** | Ruta Flask |

## Propósito

Maneja el registro de nuevos usuarios en la plataforma. Procesa el formulario de registro, valida datos, crea el usuario y lo autentica.

## Flujo Lógico

1. Procesa formulario POST con username, email, password
2. Valida que username no exista
3. Valida que email no exista
4. Crea nuevo usuario con `User()`
5. Hashea contraseña con `set_password()`
6. Guarda en base de datos
7. Envía email de bienvenida (si está habilitado)
8. Inicia sesión automáticamente
9. Redirige al dashboard

## Parámetros

| Parámetro | Tipo | Descripción |
|-----------|------|-------------|
| Ninguno (form data) | - | username, email, password, full_name |

## Tablas Utilizadas

- `users` - Crea nuevo registro

## Templates Relacionados

- `auth/register.html` - Formulario de registro

## Archivos Relacionados

- `app/models.py` - Modelo User
- `app/routes/auth.py` - send_welcome_email_if_enabled()

## Dependencias

- `User.set_password()` - Hashear contraseña
- `flask_login.login_user()` - Iniciar sesión

## Impacto si se Modifica

**Medio impacto** - Afecta:
- Proceso de registro
- Validación de usuarios
- Creación de cuentas
