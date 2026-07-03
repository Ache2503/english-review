# Fix: Rutas de templates incorrectas en units.py

## Problema
Error 500 al acceder a `/units/7/vocabulary`:
```
jinja2.exceptions.TemplateNotFound: vocabulary_view.html
```

## Causa
Las rutas de los templates en `app/routes/units.py` no incluían el directorio del template.

## Solución

Corregidas las rutas de los templates:

| Ruta | Antes | Después |
|------|-------|---------|
| vocabulary | `vocabulary_view.html` | `vocabulary/vocabulary_view.html` |
| writing | `writing_practice.html` | `writing/writing_practice.html` |
| sentences | `sentence_structures.html` | `sentences/sentence_structures.html` |

## Archivos Modificados
- `app/routes/units.py` - Líneas 97, 119, 211
