# Función: view_unit()

## Información General

| Campo | Valor |
|-------|-------|
| **Nombre** | view_unit() |
| **Archivo** | app/routes/units.py |
| **Ruta** | app/routes/units.py |
| **Tipo** | Ruta Flask |

## Propósito

Muestra los detalles de una unidad de estudio incluyendo temas, gramática, vocabulario y ejercicios.

## Flujo Lógico

1. Obtiene unidad por ID
2. Verifica acceso del usuario
3. Obtiene temas de la unidad
4. Obtiene reglas gramaticales
5. Obtiene vocabulario
6. Obtiene progreso del usuario
7. Renderiza template

## Parámetros

| Parámetro | Tipo | Descripción |
|-----------|------|-------------|
| unit_id | int | ID de la unidad |

## Tablas Utilizadas

- `units` - Consulta unidad
- `topics` - Temas de la unidad
- `grammar_rules` - Reglas gramaticales
- `vocabulary_categories` - Categorías vocabulario
- `user_progress` - Progreso usuario

## Templates Relacionados

- `unit_detail.html` - Vista de unidad

## Archivos Relacionados

- `app/routes/units.py` - view_grammar(), view_vocabulary()

## Impacto si se Modifica

**Alto impacto** - Afecta:
- Contenido educativo
- Progreso del usuario
- Desbloqueo de unidades
