# 🌐 Guía de Acceso a la Plataforma Enriquecida

## ✅ Estado Actual

Tu plataforma **está completamente enriquecida** y lista para usar:

```
✓ 6 Unidades completamente pobladas (Unit 7-12)
✓ 60 palabras de vocabulario con pronunciación IPA
✓ 13 ejercicios de escritura (3 niveles: beginner/intermediate/advanced)
✓ 16 reglas gramaticales detalladas
✓ 12 diálogos prácticos
✓ 6 quizzes generados
✓ Sistema de feedback automático funcionando
```

---

## 🚀 Cómo Iniciar

### Opción 1: Desde Terminal (Recomendado)

```bash
# 1. Navega al directorio
cd /home/axel-michael/Documentos/guia_estudio/english-learning-platform

# 2. Activa el entorno virtual
source .venv/bin/activate

# 3. Inicia la aplicación
python app.py

# O en background:
nohup python app.py > app.log 2>&1 &
```

### Opción 2: Desde VS Code

```bash
# Abre la carpeta en VS Code
code /home/axel-michael/Documentos/guia_estudio/english-learning-platform

# Luego presiona Ctrl+` para abrir terminal
# Y ejecuta: python app.py
```

### Opción 3: Ver Estado

```bash
# Verificar que el servidor está corriendo
curl http://127.0.0.1:5000

# Si ves HTML, ¡está corriendo!
```

---

## 🌍 Acceso Desde el Navegador

Una vez que la aplicación está corriendo:

### URL Principal
```
http://127.0.0.1:5000
http://localhost:5000
```

---

## 📚 Flujo de Uso

### 1️⃣ **Crear Cuenta**
- Ve a `/register` o click en "Register"
- Ingresa: nombre, email, contraseña
- Confirma contraseña
- Click "Create Account"

### 2️⃣ **Iniciar Sesión**
- Usa email y contraseña
- Eres redirigido a Dashboard

### 3️⃣ **Seleccionar Unidad**
- Ves 6 tarjetas de unidades:
  - Unit 7: MIND
  - Unit 8: ART
  - Unit 9: MONEY
  - Unit 10: SCIENCE AND TECHNOLOGY
  - Unit 11: NATURAL WORLD
  - Unit 12: MEDIA
- Click en una para verla

### 4️⃣ **Dentro de una Unidad**

Verás 5 secciones:

#### 📖 **Grammar**
- Reglas gramaticales (2-3 por unidad)
- Click para ver ejemplo
- Ejemplo incluye contexto y uso

#### 📚 **Vocabulary**
- Categorizado por tema
- Cada palabra tiene:
  - Palabra en inglés
  - Traducción al español
  - Pronunciación (IPA)
  - Ejemplo en contexto

#### ✍️ **Writing Practice**
- Ver todos los ejercicios disponibles
- Filtrar por dificultad
- Botones para practicar cada uno

#### 🗣️ **Dialogues**
- Conversaciones auténticas
- Múltiples situaciones
- Listos para practicar speaking

#### 📝 **Quiz**
- Preguntas sobre la unidad
- Respuestas múltiples
- Evaluación al completar

---

## ✍️ Completar un Ejercicio de Escritura

### Paso 1: Seleccionar Ejercicio
```
Ves una lista de ejercicios disponibles.
Haz click en uno.
```

### Paso 2: Ver Instrucciones
```
Título: "Past Habits Reflection"
Instrucciones: "Write 5-7 sentences about what you used to do..."
Ejemplo: "I used to think money was the only way to happiness..."
```

### Paso 3: Escribir tu Respuesta
```
Campo de texto grande
Escribe tu respuesta (mínimo de palabras según dificultad)
```

### Paso 4: Enviar
```
Click botón "Submit"
Sistema analiza tu texto
```

### Paso 5: Recibir Feedback
```
Ves:
- Puntuación (0-100)
- Análisis de texto
- Mensajes de feedback específicos
- Sugerencias de mejora
```

### Paso 6: Ver Historial
```
Todos tus intentos se guardan
Puedes revisarlos y mejorar
```

---

## 🎯 Rutas de la Aplicación

| Ruta | Descripción |
|------|-------------|
| `/` | Página principal |
| `/register` | Crear nueva cuenta |
| `/login` | Iniciar sesión |
| `/logout` | Cerrar sesión |
| `/dashboard` | Panel principal (unidades) |
| `/unit/<numero>` | Ver unidad (p.ej., `/unit/7`) |
| `/unit/<numero>/grammar` | Ver gramática de unidad |
| `/unit/<numero>/vocabulary` | Ver vocabulario |
| `/unit/<numero>/writing_practice` | Ejercicios de escritura |
| `/unit/<numero>/sentence_practice` | Práctica de oraciones |
| `/unit/<numero>/quiz` | Quiz de la unidad |
| `/practice/writing` | Nueva práctica de escritura |
| `/practice/sentence` | Nueva práctica de oración |
| `/api/analyze` | API para análisis (POST) |

---

## 🔧 Endpoints API Disponibles

### Analizar Escritura (POST)

**URL**: `/api/analyze`

**Request**:
```json
{
  "text": "I used to think money was important...",
  "unit_number": 7
}
```

**Response**:
```json
{
  "score": 85,
  "messages": [
    "Great use of 'used to' for past habits!",
    "Your text is well-structured and clear."
  ],
  "metrics": {
    "word_count": 45,
    "concepts_found": ["used to", "happiness"]
  }
}
```

---

## 💾 Base de Datos - Contenido Almacenado

### Por Cada Unidad (6 total)

**Vocabulario**:
- 2 categorías
- 5 palabras por categoría
- Cada palabra: traducción, pronunciación IPA, ejemplo

**Gramática**:
- 2-3 reglas principales
- Ejemplo y contexto para cada una

**Ejercicios**:
- 2-3 ejercicios por unidad
- Diferentes niveles: beginner, intermediate, advanced
- Cada uno con instrucciones y ejemplo

**Diálogos**:
- 1-2 conversaciones por unidad
- 3-4 líneas por diálogo
- Situaciones realistas

---

## 🎓 Recomendaciones de Estudio

### Para Máximos Resultados:

**Plan Semanal Recomendado**:
```
Lunes:    Unit 7 - Vocabulario + Gramática
Martes:   Unit 7 - Diálogos + Ejercicios
Miércoles: Unit 8 - Vocabulario + Gramática
Jueves:   Unit 8 - Diálogos + Ejercicios
Viernes:  Unit 9 - Vocabulario + Gramática
Sábado:   Unit 9 - Diálogos + Ejercicios
Domingo:  Repaso + Quizzes
```

**Por Cada Unidad (Tiempo Estimado)**:
- Vocabulario: 15-20 minutos
- Gramática: 15-20 minutos
- Diálogos: 15-20 minutos
- Ejercicios: 30-45 minutos (3-4 ejercicios)
- Quiz: 15-20 minutos
- **Total: 90-120 minutos por unidad**

---

## 🐛 Solucionar Problemas

### Problema: "Puerto 5000 en uso"

```bash
# Encuentra qué proceso está usando el puerto
lsof -i :5000

# Detén el proceso
kill -9 <PID>

# O usa otro puerto
FLASK_ENV=development FLASK_APP=app.py flask run --port 5001
```

### Problema: "Error de conexión a BD"

```bash
# Verifica que PostgreSQL está corriendo
sudo systemctl status postgresql

# Si no, inicia
sudo systemctl start postgresql
```

### Problema: "No ve los cambios en vocabulario"

```bash
# Limpiar cache del navegador
Ctrl + Shift + R (hard refresh)

# O
Ctrl + Shift + Delete (abrir historial)
```

---

## 📊 Dashboard - Lo que Ves

```
┌─────────────────────────────────────────┐
│  English Learning Platform              │
│  Welcome, [Tu Nombre]!                  │
├─────────────────────────────────────────┤
│                                         │
│  Unit 7: MIND               [Start]    │
│  "Exploring topics about happiness..."  │
│                                         │
│  Unit 8: ART                [Start]    │
│  "Discover art, music, and creative..." │
│                                         │
│  Unit 9: MONEY              [Start]    │
│  "Understanding money, finance..."      │
│                                         │
│  Unit 10: SCIENCE           [Start]    │
│  "Exploring technology, innovation..."  │
│                                         │
│  Unit 11: NATURE            [Start]    │
│  "Understanding nature, environment..."│
│                                         │
│  Unit 12: MEDIA             [Start]    │
│  "Understanding media, information..."  │
│                                         │
└─────────────────────────────────────────┘
```

---

## 🎯 Próximos Pasos

Ahora que tu plataforma está **completamente enriquecida**, puedes:

1. ✅ **Usar la plataforma** - Comienza a aprender
2. ✅ **Compartir con amigos** - Invita a otros estudiantes
3. ✅ **Monitorear progreso** - Ve cómo mejoran los usuarios
4. 🔮 **Agregar más unidades** - Expande a Unit 13+
5. 🔮 **Mejorar UI** - Personaliza la apariencia
6. 🔮 **Agregar audio** - Pronunciación con grabaciones
7. 🔮 **Quiz avanzados** - Más preguntas variadas

---

## 📧 Soporte Rápido

**Si algo no funciona**:

1. Verifica que la app está corriendo (`python app.py`)
2. Verifica que PostgreSQL está conectada
3. Revisa los logs de error en terminal
4. Intenta `python verify_enrichment.py` para diagnóstico

---

¡**Tu plataforma está lista!** 🚀 Comienza a aprender inglés ahora.

**URL**: http://127.0.0.1:5000

