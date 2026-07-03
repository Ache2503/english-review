# Función: index() - Dashboard

## Información General

| Campo | Valor |
|-------|-------|
| **Nombre** | index() |
| **Archivo** | app/routes/dashboard.py |
| **Ruta** | app/routes/dashboard.py |
| **Tipo** | Ruta Flask |

## Propósito

Muestra el dashboard principal del usuario con su progreso, estadísticas y accesos directos.

## Flujo Lógico

1. Requiere usuario autenticado (@login_required)
2. Obtiene progreso del usuario
3. Obtiene rachas activas
4. Obtiene badges recientes
5. Obtiene próximo desafío diario
6. Renderiza template dashboard

## Parámetros

| Parámetro | Tipo | Descripción |
|-----------|------|-------------|
| Ninguno | - | - |

## Tablas Utilizadas

- `users` - Consulta usuario actual
- `user_progress` - Progreso por unidad
- `user_streaks` - Rachas
- `badges` / `user_badges` - Logros
- `user_points` - Puntos

## Templates Relacionados

- `dashboard.html` - Template principal

## Archivos Relacionados

- `app/services/statistics.py` -get_comprehensive_stats()
- `app/services/streaks.py` - get_streak()

## Impacto si se Modifica

**Medio impacto** - Afecta:
- Vista principal del usuario
- Información mostrada en dashboard
