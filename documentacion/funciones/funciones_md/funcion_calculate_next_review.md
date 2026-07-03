# Función: calculate_next_review()

## Información General

| Campo | Valor |
|-------|-------|
| **Nombre** | calculate_next_review() |
| **Archivo** | app/services/srs.py |
| **Ruta** | app/services/srs.py |
| **Tipo** | Lógica de negocio (Servicio) |

## Propósito

Implementa el algoritmo SM-2 de repetición espaciada para calcular la próxima fecha de revisión de una tarjeta flashcard.

## Flujo Lógico

1. Recibe quality (0-5), ease_factor, interval, repetitions
2. Calcula nuevo ease_factor basado en quality
3. Calcula nuevo interval basado en repetitions y ease_factor
4. Calcula próximo fecha de revisión
5. Retorna diccionario con nuevos valores

## Parámetros

| Parámetro | Tipo | Descripción |
|-----------|------|-------------|
| quality | int | Calidad de respuesta (0-5) |
| ease_factor | float | Factor de facilidad actual |
| interval | int | Intervalo actual en días |
| repetitions | int | Número de repeticiones |

## Retorna

```python
{
    'ease_factor': float,
    'interval': int,
    'repetitions': int,
    'next_review': datetime
}
```

## Tablas Utilizadas

- `user_flashcard_srs` - Lee y actualiza estado SRS

## Archivos Relacionados

- `app/routes/flashcards.py` - Usa este servicio
- `app/models.py` - UserFlashcardSRS

## Dependencias

- `datetime` - Para calcular fechas
- `timedelta` - Para sumar días

## Algoritmo SM-2

```
if quality >= 3:
    if repetitions == 0: interval = 1
    elif repetitions == 1: interval = 6
    else: interval = interval * ease_factor
    repetitions += 1
else:
    repetitions = 0
    interval = 1

ease_factor = ease_factor + (0.1 - (5 - quality) * (0.08 + (5 - quality) * 0.02))
```

## Impacto si se Modifica

**Alto impacto** - Afecta:
- Sistema SRS completo
- Fechas de复习
- Aprendizaje del usuario
