# Función: index() - Stats

## Información General

| Campo | Valor |
|-------|-------|
| **Nombre** | index() |
| **Archivo** | app/routes/stats.py |
| **Ruta** | app/routes/stats.py |
| **Tipo** | Ruta Flask |

## Propósito

Muestra el dashboard de estadísticas del usuario con métricas de aprendizaje, progreso y actividad.

## Flujo Lógico

1. Verifica usuario autenticado
2. Obtiene estadísticas completas del servicio
3. Obtiene heatmap de actividad
4. Obtiene progreso semanal
5. Obtiene rendimiento por habilidad
6. Renderiza template de estadísticas

## Parámetros

| Parámetro | Tipo | Descripción |
|-----------|------|-------------|
| Ninguno | - | - |

## Tablas Utilizadas

- `user_progress` - Progreso por unidad
- `user_grammar_progress` - Progreso gramática
- `user_vocabulary_progress` - Progreso vocabulario
- `user_activities` - Historial de actividad
- `user_streaks` - Rachas
- `user_game_scores` - Puntuaciones juegos

## Templates Relacionados

- `stats/dashboard.html` - Dashboard de estadísticas

## APIs Relacionadas

- `/stats/api/activity-heatmap`
- `/stats/api/weekly-progress`
- `/stats/api/performance-skill`

## Archivos Relacionados

- `app/services/statistics.py` - get_comprehensive_stats()

## Impacto si se Modifica

**Medio impacto** - Afecta:
- Dashboard de estadísticas
- Métricas mostradas
- Visualizaciones
