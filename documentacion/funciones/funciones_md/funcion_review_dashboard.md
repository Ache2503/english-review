# Función: index() - Reviews

## Información General

| Campo | Valor |
|-------|-------|
| **Nombre** | dashboard() |
| **Archivo** | app/routes/review.py |
| **Ruta** | app/routes/review.py |
| **Tipo** | Ruta Flask |

## Propósito

Muestra el dashboard del sistema de repaso donde el usuario puede practicar vocabulario y gramática pendientes.

## Flujo Lógico

1. Verifica usuario autenticado
2. Obtiene items para repaso del servicio
3. Calcula estadísticas de repaso
4. Renderiza template de repaso

## Parámetros

| Parámetro | Tipo | Descripción |
|-----------|------|-------------|
| Ninguno | - | - |

## Tablas Utilizadas

- `user_vocabulary_progress` - Vocabulario pendiente
- `user_grammar_progress` - Gramática pendiente
- `user_flashcard_srs` - Tarjetas SRS pendientes
- `review_session_logs` - Historial de repasos

## Templates Relacionados

- `review/dashboard.html` - Dashboard repaso
- `review/start_session.html` - Iniciar repaso
- `review/practice.html` - Practicar

## Archivos Relacionados

- `app/services/review_system.py` - get_review_items()

## Impacto si se Modifica

**Medio impacto** - Afecta:
- Sistema de repaso
- Repasos programados
