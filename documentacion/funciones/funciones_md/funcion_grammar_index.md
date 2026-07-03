# Función: index() - Grammar

## Información General

| Campo | Valor |
|-------|-------|
| **Nombre** | index() |
| **Archivo** | app/routes/grammar.py |
| **Ruta** | app/routes/grammar.py |
| **Tipo** | Ruta Flask |

## Propósito

Muestra el índice de gramática con todas las reglas disponibles organizadas por categoría.

## Flujo Lógico

1. Obtiene reglas gramaticales de la base de datos
2. Agrupa por categoría
3. Obtiene progreso del usuario en cada regla
4. Renderiza template con índice

## Parámetros

| Parámetro | Tipo | Descripción |
|-----------|------|-------------|
| Ninguno | - | - |

## Tablas Utilizadas

- `grammar_rules` - Reglas gramaticales
- `user_grammar_progress` - Progreso usuario

## Templates Relacionados

- `grammar/index.html` - Índice gramática
- `grammar/grammar_view.html` - Ver regla

## Contenido Hardcodeado

El archivo `grammar.py` contiene ~1000+ líneas con contenido gramático hardcodeado como diccionario Python que debería estar en la base de datos.

## Impacto si se Modifica

**Alto impacto** - Afecta:
- Contenido gramatical
- Aprendizaje de gramática
