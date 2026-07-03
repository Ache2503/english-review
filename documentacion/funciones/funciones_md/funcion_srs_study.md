# Función: srs_study()

## Información General

| Campo | Valor |
|-------|-------|
| **Nombre** | srs_study() |
| **Archivo** | app/routes/flashcards.py |
| **Ruta** | app/routes/flashcards.py |
| **Tipo** | Ruta Flask |

## Propósito

Permite al usuario estudiar flashcards usando el sistema de repetición espaciada (SRS).

## Flujo Lógico

1. Obtiene tarjetas pendientes de revisión (get_due_flashcards)
2. Muestra flashcards una por una
3. Usuario califica respuesta (1-5)
4. Actualiza estado SRS con calculate_next_review()
5. Guarda historial de revisión

## Parámetros

| Parámetro | Tipo | Descripción |
|-----------|------|-------------|
| flashcard_id | int | ID de tarjeta (opcional) |
| quality | int | Calidad respuesta 1-5 (POST) |

## Tablas Utilizadas

- `flashcards` - Consulta tarjetas
- `user_flashcard_srs` - Estado SRS
- `user_flashcard_review` - Historial

## Templates Relacionados

- `flashcards/srs_study.html` - Interfaz de estudio

## Archivos Relacionados

- `app/services/srs.py` - calculate_next_review(), get_due_flashcards()

## Flujo Real

```
Usuario entra /flashcards/srs/study
↓
Flask ejecuta srs_study()
↓
Consulta UserFlashcardSRS para tarjetas pendientes (next_review <= now)
↓
Renderiza template con flashcards
↓
Usuario ve pregunta, hace click en "Mostrar respuesta"
↓
Usuario califica 1-5
↓
POST a srs_study() con quality
↓
calculate_next_review() calcula nuevo interval
↓
Guarda en UserFlashcardSRS
↓
Guarda en UserFlashcardReview (historial)
↓
Renderiza siguiente tarjeta
```

## Impacto si se Modifica

**Alto impacto** - Afecta:
- Sistema SRS completo
- Aprendizaje de vocabulario
- Repasos programados
