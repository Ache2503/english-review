# Función: login()

## Información General

| Campo | Valor |
|-------|-------|
| **Nombre** | login() |
| **Archivo** | app/routes/auth.py |
| **Ruta** | app/routes/auth.py |
| **Tipo** | Ruta Flask |

## Propósito

Maneja el inicio de sesión de usuarios existentes. Valida credenciales y crea sesión.

## Flujo Lógico

1. Procesa formulario POST con email y password
2. Busca usuario por email
3. Verifica contraseña con `check_password()`
4. Actualiza `last_login_date`
5. Inicia sesión con `login_user()`
6. Redirige a dashboard o página anterior

## Parámetros

| Parámetro | Tipo | Descripción |
|-----------|------|-------------|
| Ninguno (form data) | - | email, password |

## Tablas Utilizadas

- `users` - Consulta y actualiza

## Templates Relacionados

- `auth/login.html` - Formulario de login

## Archivos Relacionados

- `app/models.py` - User.check_password()

## Impacto si se Modifica

**Medio impacto** - Afecta:
- Acceso al sistema
- Seguridad de autenticación
