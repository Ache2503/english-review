# Función: daily_challenge()

## Información General

| Campo | Valor |
|-------|-------|
| **Nombre** | daily_challenge() |
| **Archivo** | app/routes/challenges.py |
| **Ruta** | app/routes/challenges.py |
| **Tipo** | Ruta Flask |

## Propósito

Muestra y gestiona el desafío diario del usuario. Permite tomar y enviar respuestas del reto.

## Flujo Lógico

1. Verifica usuario autenticado
2. Obtiene o crea DailyChallenge para hoy
3. Verifica si usuario ya completó el reto
4. Si GET: renderiza template con desafío
5. Si POST: procesa respuestas, calcula puntuación
6. Guarda resultado y actualiza puntos/racha
7. Retorna respuesta JSON o redirect

## Parámetros

| Parámetro | Tipo | Descripción |
|-----------|------|-------------|
| challenge_id | int | ID del desafío (opcional) |

## Tablas Utilizadas

- `daily_challenges` - Consulta desafío
- `user_daily_challenges` - Progreso usuario
- `user_streaks` - Actualizar racha
- `user_points` - Actualizar puntos

## Templates Relacionados

- `challenges/daily.html` - Template del desafío

## Archivos Relacionados

- `app/routes/challenges.py` - add_points(), update_streak()

## Impacto si se Modifica

**Medio impacto** - Afecta:
- Desafíos diarios
- Sistema de puntos
- Sistema de rachas
