# Sistema de Retroalimentación por Tema

## Resumen
El sistema de retroalimentación analiza textos en inglés y proporciona feedback específico según los temas de gramática de cada unidad.

## Características

### Análisis por Tema
- Lee los temas de gramática de cada unidad desde la base de datos
- Ejecuta chequeos específicos solo para los temas presentes
- Reconoce sinónimos y variaciones de títulos gramaticales

### Conceptos Reconocidos (con sinónimos)

| Concepto | Sinónimos/Variaciones |
|----------|----------------------|
| Articles | article, a/an/the, definite article, indefinite article, zero article, no article |
| Used to | used to |
| Reflexive Pronouns | reflexive pronouns, reflexive |
| Infinitive of Purpose | infinitive of purpose, to-infinitive, purpose |
| First Conditional | first conditional, conditional type 1, type 1 conditional |
| Second Conditional | second conditional, conditional type 2, type 2 conditional |
| Gerunds | gerunds, gerund, -ing form as noun |
| Adjective Clauses | adjective clauses, essential adjective clauses, relative clauses |
| Comparatives | comparatives, comparative, more/less than, er than |
| Superlatives | superlatives, superlative, the most, the least, est |
| Need to | need to, need |
| Passive Voice | passive voice, passive |
| Adjective + Infinitive | adjective + infinitive, it is adj to verb |
| Where Words | words with -where, somewhere, nowhere, everywhere, -where |
| Reported Speech | reported speech, indirect speech, reported statements |
| Past Perfect | past perfect, pluperfect |
| Should | should |

## Sistema de Puntuación

### Base
- Score inicial: 50 puntos
- +10 puntos por cada estructura gramatical usada correctamente
- -5 puntos por cada sugerencia de mejora

### Chequeos Generales
- Textos de 40+ palabras reciben +1 punto positivo
- Textos cortos (<40 palabras) reciben sugerencia (-5 puntos)

### Mensajes Finales
- Score < 60: "Revisa las reglas clave de la unidad y vuelve a intentar."
- Score 60-79: "Buen trabajo; puedes mejorar incluyendo más ejemplos de la gramática clave."
- Score 80+: "Excelente; tu texto demuestra dominio de la unidad."

## Uso en el Código

### En las Rutas
```python
from app.models import GrammarRule
from app.services.feedback import analyze_text

# Obtener títulos de gramática de la unidad
grammar_titles = [gr.topic for gr in GrammarRule.query.filter_by(
    unit_id=unit_id
).order_by(GrammarRule.order).all()]

# Analizar texto
result = analyze_text(text, unit_number, grammar_titles)

# Acceder a resultados
score = result['score']           # int: 0-100
messages = result['messages']     # list[str]: feedback messages
```

### API Endpoint
```bash
POST /practice/api/analyze
Content-Type: application/json

{
  "text": "I used to go to school every day...",
  "unit_number": 7
}

# Respuesta:
{
  "ok": true,
  "score": 65,
  "messages": [
    "Buen uso de 'used to' (1 ocurrencias).",
    "El texto es corto; intenta desarrollar más ideas (>=40 palabras)."
  ],
  "metrics": {
    "word_count": 35,
    "char_count": 180
  }
}
```

## Agregar Nuevos Conceptos

1. **Añadir al mapa de sinónimos** en `app/services/feedback.py`:
```python
CONCEPT_SYNONYMS = {
    # ... existing concepts
    'nuevo_concepto': ['keyword1', 'keyword2', 'alias'],
}
```

2. **Crear chequeo en la unidad correspondiente**:
```python
if has_concept('nuevo_concepto'):
    if _match(r"patron_regex", text):
        positives += 1
        messages.append("Mensaje de éxito.")
    else:
        suggestions += 1
        messages.append("Sugerencia de mejora.")
```

## Ejemplos de Patrones Regex

```python
# Used to
r"\bused to\b"

# Passive voice
r"\b(is|are|was|were|been|being)\s+[a-z]+ed\b"

# First conditional
r"\bIf\b[^.?!]*\b(will|won't)\b"

# Reflexive pronouns
r"\b(myself|yourself|himself|herself|itself|ourselves|yourselves|themselves)\b"
```

## Testing

Ejecutar pruebas del sistema:
```bash
export DATABASE_URL=postgresql:///english_learning
python test_feedback_system.py
```

Ver casos de prueba en `test_feedback_system.py` para ejemplos de textos buenos y malos por unidad.
