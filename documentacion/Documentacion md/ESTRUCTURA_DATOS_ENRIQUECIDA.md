# Estructura de Datos Enriquecida - Ejemplos

## 📋 Cómo se Almacenan los Datos

### 1. Vocabulario Detallado con Pronunciación

```json
{
  "categories": [
    {
      "name": "Sentimientos",
      "description": "Emotions related to happiness and well-being",
      "words": [
        {
          "word": "happiness",
          "translation": "felicidad",
          "pronunciation": "/ˈhæpɪnəs/",
          "example": "True happiness comes from within."
        },
        {
          "word": "anxiety",
          "translation": "ansiedad",
          "pronunciation": "/æŋˈzaɪəti/",
          "example": "Meditation reduces anxiety."
        }
      ]
    }
  ]
}
```

**Campos Almacenados en BD**:
- `word`: Palabra en inglés
- `definition`: Traducción + ejemplo combinados
- `example`: Ejemplo completo
- `pronunciation`: Formato IPA
- `category_id`: Referencia a la categoría
- `order`: Posición en la categoría

---

### 2. Ejercicios de Escritura Progresivos

```json
{
  "exercises": [
    {
      "type": "writing",
      "title": "Past Habits Reflection",
      "instructions": "Write 5-7 sentences about what you used to do that is different now.",
      "example": "I used to think money was the only way to happiness. Now I realize connections matter more.",
      "min_words": 50,
      "difficulty": "beginner"
    },
    {
      "type": "writing",
      "title": "Internet Impact Analysis",
      "instructions": "Discuss how the internet has changed your brain and thinking patterns.",
      "example": "The internet has changed how I think. I used to read books, but now I scroll quickly.",
      "min_words": 70,
      "difficulty": "intermediate"
    },
    {
      "type": "writing",
      "title": "Intelligence Redefined",
      "instructions": "Write about what intelligence means beyond just IQ.",
      "example": "Intelligence is more than test scores. Emotional intelligence matters too.",
      "min_words": 100,
      "difficulty": "advanced"
    }
  ]
}
```

**Tabla WritingPractice**:
```
id | unit_id | title                      | instructions                   | example_text              | difficulty    | order
---|---------|---------------------------|--------------------------------|--------------------------|----------------|-------
1  | 7       | Past Habits Reflection    | Write 5-7 sentences about...   | I used to think money...  | beginner       | 0
2  | 7       | Internet Impact Analysis  | Discuss how internet changed...| The internet has changed..| intermediate   | 1
3  | 7       | Intelligence Redefined    | Write about intelligence...    | Intelligence is more...   | advanced       | 2
...
```

---

### 3. Diálogos Prácticos

```json
{
  "dialogues": [
    {
      "title": "Coffee Shop - What Makes You Happy",
      "lines": [
        {
          "speaker": "A",
          "text": "I used to think happiness was about money and success."
        },
        {
          "speaker": "B",
          "text": "But now you realize simple things matter more, right?"
        },
        {
          "speaker": "A",
          "text": "Exactly! Real happiness comes from relationships and growth."
        }
      ]
    }
  ]
}
```

**Almacenado en UnitExtra como JSON**:
```
{
  "unit_id": 7,
  "data": {
    "dialogues": [
      {
        "title": "Coffee Shop - What Makes You Happy",
        "lines": [...]
      }
    ]
  }
}
```

---

### 4. Reglas Gramaticales

```json
{
  "grammar": [
    {
      "title": "Articles (a/an/the/no article)",
      "rule": "Use 'the' with specific things, use 'a/an' with general things.",
      "example": "I go to school (as a student) vs I go to the school (the building). The happiness I feel is real.",
      "level": "beginner"
    },
    {
      "title": "Used to",
      "rule": "Express habits or states in the past that no longer occur.",
      "example": "I used to feel anxious. She used to spend hours on social media.",
      "level": "beginner"
    }
  ]
}
```

**Tabla GrammarRule**:
```
id | unit_id | topic              | rule                          | example                    | order
---|---------|-------------------|-------------------------------|---------------------------|-------
1  | 7       | Articles           | Use 'the' with specific...    | I go to school...          | 0
2  | 7       | Used to            | Express habits in past...     | I used to feel anxious...  | 1
...
```

---

## 🗄️ Estructura de Base de Datos Completa

### Tabla: Units
```
id | unit_number | title                  | description
---|-------------|------------------------|-------------------------------------------
7  | 7           | MIND (La Mente)        | Exploring topics about happiness, the...
8  | 8           | ART (Arte)             | Discover art, music, and creative...
9  | 9           | MONEY (Dinero)         | Understanding money, finance, and...
10 | 10          | SCIENCE AND TECHNOLOGY | Exploring technology, innovation, and...
11 | 11          | NATURAL WORLD          | Understanding nature, environment, and...
12 | 12          | MEDIA                  | Understanding media, information, and...
```

### Tabla: VocabularyCategory
```
id | unit_id | category_name      | order
---|---------|-------------------|-------
1  | 7       | Sentimientos       | 0
2  | 7       | Phrasal Verbs      | 1
3  | 8       | Géneros de Música  | 0
...
```

### Tabla: VocabularyItem
```
id | category_id | word        | definition                  | example                    | pronunciation       | order
---|-------------|-------------|----------------------------|---------------------------|---------------------|-------
1  | 1           | happiness   | felicidad - True happiness..| True happiness comes from..| /ˈhæpɪnəs/          | 0
2  | 1           | anxiety     | ansiedad - Meditation...    | Meditation reduces anxiety | /æŋˈzaɪəti/         | 1
...
```

### Tabla: GrammarRule
```
id | unit_id | topic           | rule                    | example                  | order
---|---------|-----------------|-------------------------|--------------------------|-------
1  | 7       | Articles        | Use 'the' with specific | I go to school...        | 0
2  | 7       | Used to         | Express habits in past  | I used to feel anxious...| 1
...
```

### Tabla: WritingPractice
```
id | unit_id | title                   | instructions              | example_text         | difficulty   | order
---|---------|------------------------|---------------------------|----------------------|--------------|-------
1  | 7       | Past Habits Reflection | Write 5-7 sentences...   | I used to think...   | beginner     | 0
2  | 7       | Internet Impact...     | Discuss how internet...  | The internet has...  | intermediate | 1
3  | 7       | Intelligence Redefined | Write about intelligence | Intelligence is...   | advanced     | 2
...
```

### Tabla: UnitExtra (JSON Storage)
```
id | unit_id | data (JSON)
---|---------|---------------------------
1  | 7       | {
             |   "dialogues": [
             |     {
             |       "title": "Coffee Shop...",
             |       "lines": [...]
             |     }
             |   ],
             |   "exercises_count": 3
             | }
2  | 8       | { "dialogues": [...], "exercises_count": 2 }
...
```

---

## 🎯 Flujo de Datos en la Plataforma

### Cuando Un Estudiante Accede a una Unidad:

```
1. CARGAR VOCABULARIO
   ├─ SELECT * FROM vocabulary_items 
   │  WHERE category_id IN (
   │    SELECT id FROM vocabulary_categories 
   │    WHERE unit_id = 7
   │  )
   └─ Mostrar: palabra, traducción, pronunciación, ejemplo

2. CARGAR GRAMÁTICA
   ├─ SELECT * FROM grammar_rules 
   │  WHERE unit_id = 7
   └─ Mostrar: title, rule, example, level

3. CARGAR DIÁLOGOS
   ├─ SELECT data FROM unit_extra 
   │  WHERE unit_id = 7
   ├─ Parse JSON dialogues
   └─ Mostrar: título, conversación

4. CARGAR EJERCICIOS
   ├─ SELECT * FROM writing_practices 
   │  WHERE unit_id = 7
   └─ Mostrar: título, instrucciones, ejemplo, min_words
```

---

## 📝 Cuando Un Estudiante Envía un Ejercicio de Escritura:

```
1. GUARDAR INTENTO
   └─ INSERT INTO user_writing_submissions
      (user_id, writing_practice_id, text, submitted_at)

2. ANALIZAR TEXTO
   ├─ Extraer palabras claves de reglas gramaticales
   ├─ Verificar presencia en el texto
   ├─ Calcular puntuación (0-100)
   └─ Generar mensajes de feedback

3. GUARDAR RESULTADO
   ├─ UPDATE user_writing_submissions
   │  SET feedback = '...', score = 85
   └─ Mostrar al usuario:
      - Puntuación
      - Mensajes de feedback
      - Áreas de mejora
```

---

## 🔍 Ejemplos de Queries Útiles

### Obtener Todo Contenido de una Unidad:
```sql
SELECT 
  u.unit_number,
  u.title,
  gc.category_name,
  vi.word,
  vi.pronunciation,
  vi.example,
  gr.topic,
  wp.title as exercise_title,
  wp.difficulty
FROM units u
LEFT JOIN vocabulary_categories vc ON u.id = vc.unit_id
LEFT JOIN vocabulary_items vi ON vc.id = vi.category_id
LEFT JOIN grammar_rules gr ON u.id = gr.unit_id
LEFT JOIN writing_practices wp ON u.id = wp.unit_id
WHERE u.unit_number = 7
ORDER BY vc.order, vi.order, gr.order, wp.order;
```

### Obtener Ejercicios por Nivel de Dificultad:
```sql
SELECT wp.title, wp.instructions, wp.example_text, wp.difficulty
FROM writing_practices wp
JOIN units u ON wp.unit_id = u.id
WHERE u.unit_number = 7
AND wp.difficulty = 'beginner'
ORDER BY wp.order;
```

### Obtener Vocabulario de una Categoría:
```sql
SELECT vi.word, vi.pronunciation, vi.definition, vi.example
FROM vocabulary_items vi
JOIN vocabulary_categories vc ON vi.category_id = vc.id
WHERE vc.category_name = 'Sentimientos'
AND vc.unit_id = (SELECT id FROM units WHERE unit_number = 7)
ORDER BY vi.order;
```

---

## 💾 Ventajas de esta Estructura

✅ **Flexible**: Fácil agregar más contenido
✅ **Escalable**: Soporta crecer el número de unidades
✅ **Queryable**: Búsquedas complejas son rápidas
✅ **JSON Storage**: Diálogos y datos complejos sin normalización excesiva
✅ **Progresivo**: Diferentes niveles de dificultad
✅ **Relaciones**: Vinculación clara entre tablas

---

## 📊 Total de Contenido Almacenado

- **60 palabras de vocabulario** (10 por unidad × 6 unidades)
- **13+ ejercicios de escritura** (3 en Unit 7, 2 en otras)
- **12+ diálogos** (2 en Unit 7, 1-2 en otras)
- **15+ reglas gramaticales** (2-3 por unidad)
- **6 quizzes** (1 por unidad)
- **Pronunciaciones IPA**: 60+

**Total en BD**: ~200+ registros base + JSON estructurado
