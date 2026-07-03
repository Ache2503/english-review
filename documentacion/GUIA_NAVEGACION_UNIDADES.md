# Guía Completa: Sistema de Navegación de Unidades y Temas

## Tabla de Contenidos
1. [Rutas en Flask](#1-rutas-en-flask)
2. [Lógica del Controlador](#2-lógica-del-controlador)
3. [Plantillas HTML](#3-plantillas-html)
4. [Estructura de Base de Datos](#4-estructura-de-base-de-datos)
5. [Flujo Completo Paso a Paso](#5-flujo-completo-paso-a-paso)

---

## 1. Rutas en Flask

### 1.1 Archivo: `app/routes/units.py`

#### Ruta Principal de Unidad
```python
# Línea 19-21
@units_bp.route('/<int:unit_id>')
@login_required
def view_unit(unit_id):
```

**URL resultante:** `/units/<unit_id>` (ej: `/units/7`)

#### Ruta de Detalle de Tema
```python
# Línea 240-242
@units_bp.route('/topic/<int:topic_id>')
@login_required
def topic_detail(topic_id):
```

**URL resultante:** `/units/topic/<topic_id>` (ej: `/units/topic/20`)

### 1.2 Blueprint Configuration
```python
# Línea 7
units_bp = Blueprint('units', __name__, url_prefix='/units')
```
- **Nombre del blueprint:** `units`
- **Prefijo de URL:** `/units`

---

## 2. Lógica del Controlador

### 2.1 Función: `view_unit()` - Líneas 19-55

```python
@units_bp.route('/<int:unit_id>')
@login_required
def view_unit(unit_id):
    """Ver detalles de una unidad"""
    
    # 1. Obtener la unidad por ID
    unit = Unit.query.get_or_404(unit_id)
    
    # 2. Verificar si la unidad está desbloqueada
    unlock_system = UnitUnlockSystem(current_user.id)
    is_unlocked = unlock_system.is_unit_unlocked(unit_id)
    
    if not is_unlocked:
        flash('🔒 Debes completar la unidad anterior primero.', 'warning')
        return redirect(url_for('unit_challenge.units_overview'))
    
    # 3. Obtener o crear progreso del usuario
    progress = UserProgress.query.filter_by(
        user_id=current_user.id,
        unit_id=unit_id
    ).first()
    
    if not progress:
        progress = UserProgress(user_id=current_user.id, unit_id=unit_id)
        db.session.add(progress)
        db.session.commit()
    
    # 4. Obtener info de desbloqueo para la siguiente unidad
    unit_status = unlock_system.get_unit_requirements(unit_id)
    
    # 5. Extra JSON activities/tips
    extra = UnitExtra.query.filter_by(unit_id=unit_id).first()
    activities = extra.data if extra and extra.data else {}

    return render_template('unit_detail.html',
                           unit=unit,
                           progress=progress,
                           activities=activities,
                           unit_status=unit_status)
```

**Datos que pasa al template:**
| Variable | Descripción |
|---------|-------------|
| `unit` | Objeto Unit con todos los datos |
| `progress` | Progreso del usuario en esa unidad |
| `activities` | Tips y actividades extra |
| `unit_status` | Estado de desbloqueo de secciones |

---

### 2.2 Función: `topic_detail()` - Líneas 240-266

```python
@units_bp.route('/topic/<int:topic_id>')
@login_required
def topic_detail(topic_id):
    """Ver detalles de un tema específico dentro de una unidad"""
    
    # 1. Obtener el tópico
    topic = Topic.query.get_or_404(topic_id)
    
    # 2. Verificar si la unidad a la que pertenece está desbloqueada
    unlock_system = UnitUnlockSystem(current_user.id)
    if not unlock_system.is_unit_unlocked(topic.unit_id):
        flash('🔒 Debes desbloquear esta unidad primero.', 'warning')
        return redirect(url_for('unit_challenge.units_overview'))

    # 3. Obtener explicaciones extra si existen
    explanations = topic.explanations.order_by(TopicExplanation.order).all()
    
    # 4. Buscar reglas gramaticales relacionadas
    grammar_rules = GrammarRule.query.filter_by(
        unit_id=topic.unit_id, 
        topic=topic.title 
    ).all()

    return render_template('units/topic_detail.html', 
                           topic=topic, 
                           explanations=explanations,
                           grammar_rules=grammar_rules)
```

---

### 2.3 Modelos Involucrados

#### Modelo: `Unit` - `app/models.py` (línea 117)
```python
class Unit(db.Model):
    """Modelo para cada unidad de estudio"""
    __tablename__ = 'units'
    
    id = db.Column(db.Integer, primary_key=True)
    unit_number = db.Column(db.Integer, unique=True, nullable=False, index=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    detailed_explanation = db.Column(db.Text)
    learning_objectives = db.Column(db.JSON)
    overview = db.Column(db.Text)
    
    # Relaciones
    topics = db.relationship('Topic', backref='unit', lazy='dynamic')
    grammar_rules = db.relationship('GrammarRule', backref='unit', lazy='dynamic')
```

#### Modelo: `Topic` - `app/models.py` (línea 146)
```python
class Topic(db.Model):
    """Modelo para tópicos dentro de cada unidad"""
    __tablename__ = 'topics'
    
    id = db.Column(db.Integer, primary_key=True)
    unit_id = db.Column(db.Integer, db.ForeignKey('units.id'), nullable=False, index=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    detailed_explanation = db.Column(db.Text)
    key_concepts = db.Column(db.JSON)
    common_mistakes = db.Column(db.JSON)
    tips = db.Column(db.JSON)
    examples = db.Column(db.JSON)
    order = db.Column(db.Integer, default=0)
    
    # Relaciones
    explanations = db.relationship('TopicExplanation', backref='topic', lazy='dynamic')
```

---

## 3. Plantillas HTML

### 3.1 Enlace a Unidad - `app/templates/unit_detail.html` (línea 12)
```html
<!-- Botón para ver progreso/desafío -->
<a href="{{ url_for('unit_challenge.unit_requirements', unit_id=unit.id) }}" 
   class="btn btn-sm btn-warning">
    <i class="fas fa-trophy"></i> Ver Progreso / Desafío
</a>
```

### 3.2 Enlace a Tema - `app/templates/unit_detail.html` (línea 154)
```html
<!-- Lista de temas de la unidad -->
{% for topic in unit.topics %}
<div class="col-12">
    <a href="{{ url_for('units.topic_detail', topic_id=topic.id) }}" 
       class="d-flex justify-content-between align-items-center p-2 rounded bg-light border">
        
        <div class="d-flex align-items-center">
            <span class="badge bg-primary me-2">{{ loop.index }}</span>
            <div>
                <div class="fw-bold text-dark">{{ topic.title }}</div>
                <small class="text-muted">{{ topic.description }}</small>
            </div>
        </div>
        
        <small class="text-primary">
            <i class="fas fa-chevron-right"></i>
        </small>
    </a>
</div>
{% endfor %}
```

### 3.3 Cómo se construye el href dinámicamente

| Ruta | url_for() | Resultado |
|------|-----------|-----------|
| Unidad | `url_for('unit_challenge.unit_requirements', unit_id=unit.id)` | `/challenge/unit/7` |
| Tema | `url_for('units.topic_detail', topic_id=topic.id)` | `/units/topic/20` |

---

## 4. Estructura de Base de Datos

### 4.1 Diagrama de Relaciones

```
┌─────────────────┐         ┌─────────────────┐
│     units       │         │     topics     │
├─────────────────┤         ├─────────────────┤
│ id (PK)         │◄───────┐│ id (PK)         │
│ unit_number     │        ││ unit_id (FK)    │
│ title           │        ││ title           │
│ description      │        ││ description      │
│ ...             │        ││ ...             │
└─────────────────┘        │└─────────────────┘
                           │
                           │ 1:N
                           └──────────────► (múltiples topics por unidad)
```

### 4.2 Clave Foránea

```sql
-- Tabla: topics
unit_id INTEGER REFERENCES units(id) NOT NULL
```

### 4.3 Acceso desde el modelo

```python
# En Topic, la relación inversa da acceso a la unidad:
topic = Topic.query.get(20)
unit = topic.unit  # Accede a la unidad padre

# En Unit, la relación da acceso a los temas:
unit = Unit.query.get(7)
topics = unit.topics.all()  # Lista de temas
```

---

## 5. Flujo Completo Paso a Paso

### 5.1 Flujo: Ver Unidad (`/units/7`)

```
USUARIO                          FLASK                           BASE DE DATOS
  │                                  │                                  │
  ├─► Clic en "Unit 7" ────────────►│                                  │
  │                                  ├─► GET /units/7                  │
  │                                  │                                  │
  │                                  ├─► Unit.query.get_or_404(7) ────►│ SELECT * FROM units WHERE id=7
  │                                  │◄────────────────────────────────│ (datos de unidad)
  │                                  │                                  │
  │                                  ├─► is_unit_unlocked(7)           │
  │                                  │                                  │
  │                                  ├─► UserProgress.query.filter...──►│ SELECT * FROM user_progress
  │                                  │                                  │
  │                                  ├─► UnitExtra.query.filter_by...──►│ SELECT * FROM unit_extras
  │                                  │                                  │
  │◄──◄ render_template(unit_detail.html)◄──◄│
  │                                  │                                  │
  ├─► Navegador muestra la página ──┤│                                  │
```

### 5.2 Flujo: Ver Tema (`/units/topic/20`)

```
USUARIO                          FLASK                           BASE DE DATOS
  │                                  │                                  │
  ├─► Clic en "Past Simple" ───────►│                                  │
  │                                  ├─► GET /units/topic/20            │
  │                                  │                                  │
  │                                  ├─► Topic.query.get_or_404(20) ──►│ SELECT * FROM topics WHERE id=20
  │                                  │◄────────────────────────────────│ (datos del tema)
  │                                  │                                  │
  │                                  ├─► topic.unit_id = 7             │
  │                                  │   is_unit_unlocked(7)           │
  │                                  │                                  │
  │                                  ├─► TopicExplanation.query.filter►│ SELECT * FROM topic_explanations
  │                                  │                                  │
  │                                  ├─► GrammarRule.query.filter_by──►│ SELECT * FROM grammar_rules
  │                                  │    (unit_id=7, topic=título)    │
  │                                  │                                  │
  │◄──◄ render_template(units/topic_detail.html)◄──◄│
  │                                  │                                  │
  ├─► Navegador muestra el tema ─────┤                                  │
```

---

## 6. Cómo Modificar/Agregar Unidades y Temas

### 6.1 Agregar una nueva unidad

1. **Insertar en base de datos:**
```python
# En una shell Flask o script
from app import create_app
from app.models import Unit

app = create_app()
with app.app_context():
    new_unit = Unit(
        unit_number=8,
        title="Unit 8: Present Perfect",
        description="Aprende el Present Perfect",
        overview="En esta unidad..."
    )
    db.session.add(new_unit)
    db.session.commit()
```

### 6.2 Agregar un nuevo tema

```python
# Continuando del ejemplo anterior
from app.models import Topic

new_topic = Topic(
    unit_id=8,  # Relacionado a Unit 8
    title="When did it happen?",
    description="Uso del Present Perfect con 'since' y 'for'",
    order=1
)
db.session.add(new_topic)
db.session.commit()
```

### 6.3 Modificar el enlace en templates

Si cambias el nombre de la función `topic_detail`, actualiza el template:

```html
<!-- ANTES -->
<a href="{{ url_for('units.topic_detail', topic_id=topic.id) }}">

<!-- DESPUÉS (si renombraste la función) -->
<a href="{{ url_for('units.nuevo_nombre', topic_id=topic.id) }}">
```

---

## 7. Referencias Rápidas

### Archivos Involvedos

| Archivo | Ubicación |
|---------|-----------|
| Rutas | `app/routes/units.py` |
| Modelos | `app/models.py` |
| Template Unidad | `app/templates/unit_detail.html` |
| Template Tema | `app/templates/units/topic_detail.html` |
| Servicio Unlock | `app/services/unit_unlock.py` |

### Nombres de Funciones y Rutas

| Función | Blueprint | URL |
|---------|----------|-----|
| `view_unit` | units | `/units/<int:unit_id>` |
| `topic_detail` | units | `/units/topic/<int:topic_id>` |

### Nombres de Modelos

| Modelo | Tabla | Relación |
|--------|-------|----------|
| `Unit` | `units` | 1:N → Topic |
| `Topic` | `topics` | N:1 ← Unit |
| `GrammarRule` | `grammar_rules` | N:1 ← Unit |

---

*Guía generada para English Learning Platform*
