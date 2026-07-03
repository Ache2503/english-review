# Función: view()

## Información General

| Campo | Valor |
|-------|-------|
| **Nombre** | view() |
| **Archivo** | app/routes/profile.py |
| **Ruta** | app/routes/profile.py |
| **Tipo** | Ruta Flask |

## Propósito

Muestra el perfil del usuario con su información personal, estadísticas y progreso.

## Flujo Lógico

1. Verifica usuario autenticado
2. Obtiene datos del usuario
3. Obtiene estadísticas de aprendizaje
4. Obtiene badges obtenidos
5. Renderiza template de perfil

## Parámetros

| Parámetro | Tipo | Descripción |
|-----------|------|-------------|
| Ninguno | - | - |

## Tablas Utilizadas

- `users` - Datos del usuario
- `user_progress` - Progreso
- `badges` / `user_badges` - Logros
- `user_streaks` - Rachas
- `user_points` - Puntos

## Templates Relacionados

- `profile/view.html` - Ver perfil
- `profile/edit.html` - Editar perfil
- `profile/preferences.html` - Preferencias

## Información Mostrada

- Nombre de usuario
- Email
- Fecha de registro
- Suscripción actual
- Racha actual
- Puntos acumulados
- Unidades completadas
- Badges obtenidos

## Impacto si se Modifica

**Bajo impacto** - Afecta:
- Vista de perfil
- Información mostrada
