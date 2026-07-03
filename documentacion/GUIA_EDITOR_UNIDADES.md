# Guía de Implementación: Editor de Unidades con Vista Previa en Tiempo Real

## Tabla de Contenidos
1. [Estructura de Archivos](#1-estructura-de-archivos)
2. [Backend - Rutas y API](#2-backend---rutas-y-api)
3. [Frontend - HTML y CSS](#3-frontend---html-y-css)
4. [Frontend - JavaScript](#4-frontend---javascript)
5. [Estrategia de Vista Previa](#5-estrategia-de-vista-previa)
6. [Seguridad](#6-seguridad)
7. [Flujo Paso a Paso](#7-flujo-paso-a-paso)

---

## 1. Estructura de Archivos

```
english-review/
├── app/
│   ├── routes/
│   │   └── admin.py              # NUEVO: Rutas de administración
│   ├── services/
│   │   └── unit_editor.py       # NUEVO: Lógica del editor
│   ├── templates/
│   │   └── admin/
│   │       └── edit_unit.html   # NUEVO: Template del editor
│   └── static/
│       └── js/
│           └── unit_editor.js   # NUEVO: JavaScript del editor
├── requirements.txt              # Actualizar si agregas dependencias
└── ...
```

---

## 2. Backend - Rutas y API

### 2.1 Archivo: `app/routes/admin.py`

```python
"""
Rutas de administración para el Editor de Unidades
Archivo: app/routes/admin.py
"""

from flask import Blueprint, render_template, request, jsonify, redirect, url_for, flash
from flask_login import login_required, current_user
from app.extensions import db
from app.models import Unit, Topic, UnitExtra
from app.services.unit_editor import UnitEditorService

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')


# =============================================================================
# DECORADORES DE SEGURIDAD
# =============================================================================

def admin_required(f):
    """Decorador para verificar que el usuario es administrador"""
    @login_required
    def decorated_function(*args, **kwargs):
        if not current_user.is_admin:
            flash('No tienes permiso para acceder a esta sección.', 'danger')
            return redirect(url_for('main.index'))
        return f(*args, **kwargs)
    decorated_function.__name__ = f.__name__
    return decorated_function


# =============================================================================
# RUTA PRINCIPAL DEL EDITOR
# =============================================================================

@admin_bp.route('/units/<int:unit_id>/edit')
@admin_required
def edit_unit(unit_id):
    """
    Muestra el editor de unidades con split view.
    URL: /admin/units/1/edit
    
    Args:
        unit_id: ID de la unidad a editar
    """
    unit = Unit.query.get_or_404(unit_id)
    topics = Topic.query.filter_by(unit_id=unit_id).order_by(Topic.order).all()
    
    return render_template(
        'admin/edit_unit.html',
        unit=unit,
        topics=topics
    )


# =============================================================================
# API: OBTENER DATOS DE UNIDAD
# =============================================================================

@admin_bp.route('/api/units/<int:unit_id>')
@admin_required
def get_unit_data(unit_id):
    """
    API para obtener los datos de una unidad en formato JSON.
    Método: GET
    URL: /admin/api/units/1
    
    Returns:
        JSON con todos los datos de la unidad y sus temas
    """
    unit = Unit.query.get_or_404(unit_id)
    topics = Topic.query.filter_by(unit_id=unit_id).order_by(Topic.order).all()
    extra = UnitExtra.query.filter_by(unit_id=unit_id).first()
    
    return jsonify({
        'success': True,
        'unit': {
            'id': unit.id,
            'unit_number': unit.unit_number,
            'title': unit.title,
            'description': unit.description,
            'detailed_explanation': unit.detailed_explanation,
            'overview': unit.overview,
            'learning_objectives': unit.learning_objectives or []
        },
        'topics': [
            {
                'id': topic.id,
                'title': topic.title,
                'description': topic.description,
                'detailed_explanation': topic.detailed_explanation,
                'key_concepts': topic.key_concepts or [],
                'common_mistakes': topic.common_mistakes or [],
                'tips': topic.tips or [],
                'examples': topic.examples or [],
                'order': topic.order
            }
            for topic in topics
        ],
        'extra': extra.data if extra and extra.data else {}
    })


# =============================================================================
# API: GUARDAR CAMBIOS DE UNIDAD
# =============================================================================

@admin_bp.route('/api/units/<int:unit_id>', methods=['POST'])
@admin_required
def save_unit(unit_id):
    """
    API para guardar los cambios de una unidad.
    Método: POST
    URL: /admin/api/units/1
    
    Body JSON:
    {
        "unit": {
            "title": "...",
            "description": "...",
            ...
        },
        "topics": [
            {"id": 1, "title": "...", ...},
            {"id": null, "title": "...", ...}  // Nuevo tema
        ],
        "topics_to_delete": [5, 10]  // IDs de temas a eliminar
    }
    
    Returns:
        JSON con éxito o error
    """
    try:
        data = request.get_json()
        service = UnitEditorService(unit_id)
        result = service.save_all(data)
        
        return jsonify({
            'success': True,
            'message': 'Cambios guardados correctamente',
            'data': result
        })
        
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400


# =============================================================================
# API: ELIMINAR UNIDAD
# =============================================================================

@admin_bp.route('/api/units/<int:unit_id>', methods=['DELETE'])
@admin_required
def delete_unit(unit_id):
    """Elimina una unidad y todos sus temas asociados"""
    unit = Unit.query.get_or_404(unit_id)
    
    try:
        db.session.delete(unit)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'Unidad eliminada correctamente'
        })
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400
```

---

### 2.2 Archivo: `app/services/unit_editor.py`

```python
"""
Servicio para la lógica del Editor de Unidades
Archivo: app/services/unit_editor.py
"""

from app.extensions import db
from app.models import Unit, Topic, UnitExtra
from datetime import datetime


class UnitEditorService:
    """Servicio para manejar la edición de unidades"""
    
    def __init__(self, unit_id):
        self.unit = Unit.query.get_or_404(unit_id)
        self.unit_id = unit_id
    
    def save_all(self, data):
        """
        Guarda todos los cambios de la unidad.
        
        Args:
            data: Dictionary con 'unit', 'topics' y opcionalmente 'topics_to_delete'
            
        Returns:
            Dictionary con resultados
        """
        # 1. Guardar datos de la unidad
        self._save_unit(data.get('unit', {}))
        
        # 2. Guardar temas
        topics_result = self._save_topics(data.get('topics', []))
        
        # 3. Eliminar temas marcados
        deleted_count = self._delete_topics(data.get('topics_to_delete', []))
        
        # 4. Guardar datos extra
        self._save_extra(data.get('extra', {}))
        
        db.session.commit()
        
        return {
            'unit_saved': True,
            'topics_saved': topics_result['saved'],
            'topics_updated': topics_result['updated'],
            'topics_deleted': deleted_count
        }
    
    def _save_unit(self, unit_data):
        """Actualiza los datos de la unidad"""
        if 'title' in unit_data:
            self.unit.title = unit_data['title']
        if 'description' in unit_data:
            self.unit.description = unit_data['description']
        if 'detailed_explanation' in unit_data:
            self.unit.detailed_explanation = unit_data['detailed_explanation']
        if 'overview' in unit_data:
            self.unit.overview = unit_data['overview']
        if 'learning_objectives' in unit_data:
            self.unit.learning_objectives = unit_data['learning_objectives']
        
        self.unit.updated_at = datetime.utcnow()
    
    def _save_topics(self, topics_data):
        """
        Guarda/actualiza los temas.
        
        Returns:
            {'saved': count, 'updated': count}
        """
        saved = 0
        updated = 0
        
        for index, topic_data in enumerate(topics_data):
            topic_id = topic_data.get('id')
            
            if topic_id:
                # Actualizar tema existente
                topic = Topic.query.get(topic_id)
                if topic and topic.unit_id == self.unit_id:
                    self._update_topic(topic, topic_data, index)
                    updated += 1
            else:
                # Crear nuevo tema
                self._create_topic(topic_data, index)
                saved += 1
        
        return {'saved': saved, 'updated': updated}
    
    def _create_topic(self, topic_data, order):
        """Crea un nuevo tema"""
        topic = Topic(
            unit_id=self.unit_id,
            title=topic_data.get('title', 'Nuevo Tema'),
            description=topic_data.get('description', ''),
            detailed_explanation=topic_data.get('detailed_explanation', ''),
            key_concepts=topic_data.get('key_concepts', []),
            common_mistakes=topic_data.get('common_mistakes', []),
            tips=topic_data.get('tips', []),
            examples=topic_data.get('examples', []),
            order=order
        )
        db.session.add(topic)
        return topic
    
    def _update_topic(self, topic, topic_data, order):
        """Actualiza un tema existente"""
        topic.title = topic_data.get('title', topic.title)
        topic.description = topic_data.get('description', topic.description)
        topic.detailed_explanation = topic_data.get('detailed_explanation', topic.detailed_explanation)
        topic.key_concepts = topic_data.get('key_concepts', topic.key_concepts)
        topic.common_mistakes = topic_data.get('common_mistakes', topic.common_mistakes)
        topic.tips = topic_data.get('tips', topic.tips)
        topic.examples = topic_data.get('examples', topic.examples)
        topic.order = order
    
    def _delete_topics(self, topic_ids):
        """Elimina los temas por ID"""
        if not topic_ids:
            return 0
        
        deleted = Topic.query.filter(
            Topic.id.in_(topic_ids),
            Topic.unit_id == self.unit_id
        ).delete(synchronize_session=False)
        
        return deleted
    
    def _save_extra(self, extra_data):
        """Guarda datos extra de la unidad"""
        extra = UnitExtra.query.filter_by(unit_id=self.unit_id).first()
        
        if not extra:
            extra = UnitExtra(unit_id=self.unit_id, data=extra_data)
            db.session.add(extra)
        else:
            extra.data = extra_data
```

---

### 2.3 Registrar el Blueprint

En `app/__init__.py`, agregar el import y registro:

```python
# En app/__init__.py, alrededor de la línea 98
from app.routes.admin import admin_bp
# ...
app.register_blueprint(admin_bp)
```

---

## 3. Frontend - HTML y CSS

### 3.1 Archivo: `app/templates/admin/edit_unit.html`

```html
{% extends "base.html" %}

{% block title %}Editar Unidad {{ unit.unit_number }} - Admin{% endblock %}

{% block extra_css %}
<link rel="stylesheet" href="{{ url_for('static', filename='css/admin/unit_editor.css') }}">
{% endblock %}

{% block content %}
<div class="unit-editor-container">
    <!-- Header -->
    <div class="editor-header">
        <div class="d-flex justify-content-between align-items-center">
            <div>
                <a href="{{ url_for('unit_challenge.units_overview') }}" class="btn btn-outline-secondary btn-sm">
                    <i class="fas fa-arrow-left"></i> Volver
                </a>
                <span class="ms-3">
                    <span class="badge bg-primary">Admin</span>
                    <strong>Editando: {{ unit.title }}</strong>
                </span>
            </div>
            <div>
                <button type="button" class="btn btn-secondary" id="btn-preview-toggle">
                    <i class="fas fa-eye"></i> Toggle Preview
                </button>
                <button type="button" class="btn btn-primary" id="btn-save">
                    <i class="fas fa-save"></i> Guardar Cambios
                </button>
            </div>
        </div>
    </div>

    <!-- Split View -->
    <div class="split-view" id="splitView">
        <!-- Panel Izquierdo: Editor -->
        <div class="editor-panel" id="editorPanel">
            <div class="panel-header">
                <h5><i class="fas fa-edit"></i> Editor</h5>
            </div>
            <div class="panel-content">
                <!-- Datos de la Unidad -->
                <div class="card mb-3">
                    <div class="card-header">
                        <h6 class="mb-0"><i class="fas fa-info-circle"></i> Datos de la Unidad</h6>
                    </div>
                    <div class="card-body">
                        <div class="mb-3">
                            <label class="form-label">Título de la Unidad</label>
                            <input type="text" class="form-control" id="unit-title" 
                                   placeholder="Ej: Unit 1: Introduction to English">
                        </div>
                        <div class="mb-3">
                            <label class="form-label">Descripción</label>
                            <textarea class="form-control" id="unit-description" rows="2"
                                      placeholder="Breve descripción..."></textarea>
                        </div>
                        <div class="mb-3">
                            <label class="form-label">Explicación Detallada</label>
                            <textarea class="form-control" id="unit-explanation" rows="3"
                                      placeholder="Explicación completa..."></textarea>
                        </div>
                        <div class="mb-3">
                            <label class="form-label">Resumen/Overview</label>
                            <textarea class="form-control" id="unit-overview" rows="2"
                                      placeholder="Resumen..."></textarea>
                        </div>
                    </div>
                </div>

                <!-- Lista de Temas -->
                <div class="card">
                    <div class="card-header d-flex justify-content-between align-items-center">
                        <h6 class="mb-0"><i class="fas fa-list"></i> Temas</h6>
                        <button type="button" class="btn btn-sm btn-success" id="btn-add-topic">
                            <i class="fas fa-plus"></i> Agregar Tema
                        </button>
                    </div>
                    <div class="card-body p-0">
                        <div class="topics-list" id="topicsList">
                            <!-- Temas se cargarán dinámicamente -->
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Panel Derecho: Vista Previa -->
        <div class="preview-panel" id="previewPanel">
            <div class="panel-header">
                <h5><i class="fas fa-eye"></i> Vista Previa</h5>
            </div>
            <div class="panel-content">
                <iframe id="previewFrame" 
                        src="{{ url_for('units.view_unit', unit_id=unit.id) }}"
                        class="preview-iframe"></iframe>
            </div>
        </div>
    </div>
</div>

<!-- Template para nuevo tema -->
<template id="topicTemplate">
    <div class="topic-item" data-topic-id="">
        <div class="topic-header">
            <span class="topic-number">#</span>
            <input type="text" class="form-control form-control-sm topic-title-input" 
                   placeholder="Título del tema">
            <div class="topic-actions">
                <button type="button" class="btn btn-sm btn-outline-secondary btn-move-up" title="Subir">
                    <i class="fas fa-arrow-up"></i>
                </button>
                <button type="button" class="btn btn-sm btn-outline-secondary btn-move-down" title="Bajar">
                    <i class="fas fa-arrow-down"></i>
                </button>
                <button type="button" class="btn btn-sm btn-outline-danger btn-delete-topic" title="Eliminar">
                    <i class="fas fa-trash"></i>
                </button>
            </div>
        </div>
        <div class="topic-details collapse show">
            <div class="mb-2">
                <input type="text" class="form-control form-control-sm topic-desc-input" 
                       placeholder="Descripción breve">
            </div>
            <div class="mb-2">
                <textarea class="form-control form-control-sm topic-explanation-input" rows="2"
                          placeholder="Explicación detallada..."></textarea>
            </div>
        </div>
    </div>
</template>

<!-- Toast para notificaciones -->
<div class="toast-container position-fixed bottom-0 end-0 p-3">
    <div id="saveToast" class="toast" role="alert">
        <div class="toast-body">
            <span class="toast-icon"></span>
            <span class="toast-message"></span>
        </div>
    </div>
</div>

{% endblock %}

{% block extra_js %}
<script src="{{ url_for('static', filename='js/unit_editor.js') }}"></script>
{% endblock %}
```

---

### 3.2 Archivo: `app/static/css/admin/unit_editor.css` (crear carpeta si no existe)

```css
/* ============================================================================
   UNIT EDITOR - Estilos del Editor de Unidades
   ============================================================================ */

:root {
    --editor-sidebar-width: 400px;
    --editor-header-height: 60px;
}

/* Container Principal */
.unit-editor-container {
    height: calc(100vh - var(--navbar-height, 60px));
    display: flex;
    flex-direction: column;
    overflow: hidden;
}

/* Header del Editor */
.editor-header {
    height: var(--editor-header-height);
    padding: 0.75rem 1rem;
    background: var(--bs-body-bg);
    border-bottom: 1px solid var(--bs-border-color);
    display: flex;
    align-items: center;
    flex-shrink: 0;
}

/* Split View */
.split-view {
    display: flex;
    flex: 1;
    overflow: hidden;
}

.editor-panel {
    width: var(--editor-sidebar-width);
    min-width: 350px;
    max-width: 600px;
    border-right: 1px solid var(--bs-border-color);
    display: flex;
    flex-direction: column;
    background: var(--bs-tertiary-bg);
    overflow: hidden;
}

.preview-panel {
    flex: 1;
    display: flex;
    flex-direction: column;
    background: var(--bs-body-bg);
    overflow: hidden;
}

/* Panel Header */
.panel-header {
    padding: 0.75rem 1rem;
    background: var(--bs-secondary-bg);
    border-bottom: 1px solid var(--bs-border-color);
    flex-shrink: 0;
}

.panel-header h5 {
    margin: 0;
    font-size: 1rem;
    font-weight: 600;
}

/* Panel Content */
.panel-content {
    flex: 1;
    overflow-y: auto;
    padding: 1rem;
}

/* Preview Iframe */
.preview-iframe {
    width: 100%;
    height: 100%;
    border: none;
    background: white;
    border-radius: var(--bs-border-radius);
}

/* Topics List */
.topics-list {
    max-height: 500px;
    overflow-y: auto;
}

/* Topic Item */
.topic-item {
    border-bottom: 1px solid var(--bs-border-color);
    padding: 0.75rem;
    background: var(--bs-body-bg);
    transition: background-color 0.2s;
}

.topic-item:hover {
    background: var(--bs-tertiary-bg);
}

.topic-item.new-topic {
    background: rgba(var(--bs-success-rgb), 0.1);
    border-left: 3px solid var(--bs-success);
}

.topic-item.deleted {
    opacity: 0.5;
    background: rgba(var(--bs-danger-rgb), 0.1);
}

.topic-header {
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.topic-number {
    font-weight: 600;
    color: var(--bs-primary);
    min-width: 25px;
}

.topic-title-input {
    flex: 1;
}

.topic-actions {
    display: flex;
    gap: 0.25rem;
}

.topic-details {
    margin-top: 0.5rem;
    padding-left: 2rem;
}

/* Toast */
.toast-container {
    z-index: 9999;
}

#saveToast {
    background: var(--bs-body-bg);
    border: 1px solid var(--bs-border-color);
    border-radius: var(--bs-border-radius);
}

#saveToast.show {
    animation: slideIn 0.3s ease;
}

.toast-body {
    padding: 0.75rem 1rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.toast-icon.success {
    color: var(--bs-success);
}

.toast-icon.error {
    color: var(--bs-danger);
}

/* Responsive */
@media (max-width: 1024px) {
    .split-view {
        flex-direction: column;
    }
    
    .editor-panel {
        width: 100%;
        max-width: none;
        height: 50%;
        border-right: none;
        border-bottom: 1px solid var(--bs-border-color);
    }
    
    .preview-panel {
        height: 50%;
    }
}

@keyframes slideIn {
    from {
        transform: translateX(100%);
        opacity: 0;
    }
    to {
        transform: translateX(0);
        opacity: 1;
    }
}
```

---

## 4. Frontend - JavaScript

### 4.1 Archivo: `app/static/js/unit_editor.js`

```javascript
/**
 * Unit Editor - JavaScript
 * Maneja la edición en tiempo real y la comunicación con el backend
 */

class UnitEditor {
    constructor(unitId) {
        this.unitId = unitId;
        this.unit = null;
        this.topics = [];
        this.topicsToDelete = [];
        this.isDirty = false;
        this.originalData = null;
        
        this.init();
    }
    
    async init() {
        await this.loadData();
        this.bindEvents();
        this.renderTopics();
        this.updatePreview();
    }
    
    // =========================================================================
    // CARGA DE DATOS
    // =========================================================================
    
    async loadData() {
        try {
            const response = await fetch(`/admin/api/units/${this.unitId}`);
            const data = await response.json();
            
            if (data.success) {
                this.unit = data.unit;
                this.topics = data.topics;
                this.originalData = JSON.stringify(data);
                this.populateForm();
            } else {
                this.showToast('Error al cargar datos', 'error');
            }
        } catch (error) {
            console.error('Error:', error);
            this.showToast('Error de conexión', 'error');
        }
    }
    
    populateForm() {
        // Llenar datos de la unidad
        document.getElementById('unit-title').value = this.unit.title || '';
        document.getElementById('unit-description').value = this.unit.description || '';
        document.getElementById('unit-explanation').value = this.unit.detailed_explanation || '';
        document.getElementById('unit-overview').value = this.unit.overview || '';
    }
    
    // =========================================================================
    // RENDERIZADO DE TEMAS
    // =========================================================================
    
    renderTopics() {
        const container = document.getElementById('topicsList');
        const template = document.getElementById('topicTemplate');
        
        container.innerHTML = '';
        
        this.topics.forEach((topic, index) => {
            const topicEl = this.createTopicElement(topic, index);
            container.appendChild(topicEl);
        });
        
        this.updateTopicNumbers();
    }
    
    createTopicElement(topic, index) {
        const template = document.getElementById('topicTemplate');
        const clone = template.content.cloneNode(true);
        const topicEl = clone.querySelector('.topic-item');
        
        topicEl.dataset.topicId = topic.id || '';
        topicEl.dataset.index = index;
        
        // Llenar datos
        const titleInput = topicEl.querySelector('.topic-title-input');
        titleInput.value = topic.title || '';
        titleInput.dataset.field = 'title';
        
        const descInput = topicEl.querySelector('.topic-desc-input');
        descInput.value = topic.description || '';
        descInput.dataset.field = 'description';
        
        const explanationInput = topicEl.querySelector('.topic-explanation-input');
        explanationInput.value = topic.detailed_explanation || '';
        explanationInput.dataset.field = 'detailed_explanation';
        
        // Si es nuevo tema, marcar
        if (!topic.id) {
            topicEl.classList.add('new-topic');
        }
        
        return topicEl;
    }
    
    updateTopicNumbers() {
        const items = document.querySelectorAll('.topic-item');
        items.forEach((item, index) => {
            const number = item.querySelector('.topic-number');
            number.textContent = `#${index + 1}`;
            item.dataset.index = index;
        });
    }
    
    // =========================================================================
    // EVENTOS
    // =========================================================================
    
    bindEvents() {
        // Inputs de unidad
        ['unit-title', 'unit-description', 'unit-explanation', 'unit-overview'].forEach(id => {
            document.getElementById(id)?.addEventListener('input', () => {
                this.markDirty();
                this.updatePreview();
            });
        });
        
        // Agregar tema
        document.getElementById('btn-add-topic').addEventListener('click', () => {
            this.addNewTopic();
        });
        
        // Delegar eventos en la lista de temas
        document.getElementById('topicsList').addEventListener('click', (e) => {
            const topicItem = e.target.closest('.topic-item');
            if (!topicItem) return;
            
            if (e.target.closest('.btn-move-up')) {
                this.moveTopicUp(topicItem);
            } else if (e.target.closest('.btn-move-down')) {
                this.moveTopicDown(topicItem);
            } else if (e.target.closest('.btn-delete-topic')) {
                this.deleteTopic(topicItem);
            }
        });
        
        // Eventos de input en temas
        document.getElementById('topicsList').addEventListener('input', (e) => {
            if (e.target.classList.contains('topic-title-input') ||
                e.target.classList.contains('topic-desc-input') ||
                e.target.classList.contains('topic-explanation-input')) {
                this.markDirty();
                this.updatePreview();
            }
        });
        
        // Toggle preview
        document.getElementById('btn-preview-toggle').addEventListener('click', () => {
            this.togglePreview();
        });
        
        // Guardar
        document.getElementById('btn-save').addEventListener('click', () => {
            this.save();
        });
    }
    
    // =========================================================================
    // OPERACIONES DE TEMAS
    // =========================================================================
    
    addNewTopic() {
        const newTopic = {
            id: null, // null indica nuevo tema
            title: '',
            description: '',
            detailed_explanation: '',
            key_concepts: [],
            common_mistakes: [],
            tips: [],
            examples: [],
            order: this.topics.length
        };
        
        this.topics.push(newTopic);
        this.renderTopics();
        this.markDirty();
        this.updatePreview();
        
        // Focus en el nuevo tema
        const lastTopic = document.querySelector('.topic-item:last-child');
        lastTopic.querySelector('.topic-title-input').focus();
    }
    
    moveTopicUp(topicItem) {
        const index = parseInt(topicItem.dataset.index);
        if (index > 0) {
            [this.topics[index - 1], this.topics[index]] = 
                [this.topics[index], this.topics[index - 1]];
            this.renderTopics();
            this.markDirty();
            this.updatePreview();
        }
    }
    
    moveTopicDown(topicItem) {
        const index = parseInt(topicItem.dataset.index);
        if (index < this.topics.length - 1) {
            [this.topics[index], this.topics[index + 1]] = 
                [this.topics[index + 1], this.topics[index]];
            this.renderTopics();
            this.markDirty();
            this.updatePreview();
        }
    }
    
    deleteTopic(topicItem) {
        const index = parseInt(topicItem.dataset.index);
        const topic = this.topics[index];
        
        if (topic.id) {
            // Marcar para eliminación (no es nuevo)
            this.topicsToDelete.push(topic.id);
        }
        
        // Remover del array
        this.topics.splice(index, 1);
        
        // Re-render
        this.renderTopics();
        this.markDirty();
        this.updatePreview();
    }
    
    // =========================================================================
    // GUARDADO
    // =========================================================================
    
    async save() {
        if (!this.validate()) return;
        
        const data = this.collectData();
        
        try {
            const response = await fetch(`/admin/api/units/${this.unitId}`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            });
            
            const result = await response.json();
            
            if (result.success) {
                this.showToast('Cambios guardados correctamente', 'success');
                this.isDirty = false;
                
                // Recargar datos para obtener IDs de nuevos temas
                await this.loadData();
                this.renderTopics();
                
                // Actualizar URL del iframe
                document.getElementById('previewFrame').src = 
                    `/units/${this.unitId}?t=${Date.now()}`;
            } else {
                this.showToast(result.error || 'Error al guardar', 'error');
            }
        } catch (error) {
            console.error('Error:', error);
            this.showToast('Error de conexión', 'error');
        }
    }
    
    collectData() {
        return {
            unit: {
                title: document.getElementById('unit-title').value,
                description: document.getElementById('unit-description').value,
                detailed_explanation: document.getElementById('unit-explanation').value,
                overview: document.getElementById('unit-overview').value
            },
            topics: this.topics.map((topic, index) => ({
                id: topic.id,
                title: topic.title,
                description: topic.description,
                detailed_explanation: topic.detailed_explanation,
                key_concepts: topic.key_concepts || [],
                common_mistakes: topic.common_mistakes || [],
                tips: topic.tips || [],
                examples: topic.examples || [],
                order: index
            })),
            topics_to_delete: this.topicsToDelete
        };
    }
    
    validate() {
        const title = document.getElementById('unit-title').value.trim();
        if (!title) {
            this.showToast('El título de la unidad es requerido', 'error');
            return false;
        }
        return true;
    }
    
    markDirty() {
        this.isDirty = true;
    }
    
    // =========================================================================
    // VISTA PREVIA
    // =========================================================================
    
    updatePreview() {
        // Opcional: actualizar preview via iframe con datos temporales
        // Para preview en tiempo real, ver sección 5 de la guía
        this.updatePreviewIframe();
    }
    
    updatePreviewIframe() {
        const iframe = document.getElementById('previewFrame');
        // Recargar iframe con cache busting
        const url = new URL(iframe.src);
        url.searchParams.set('preview', Date.now());
        iframe.src = url.toString();
    }
    
    togglePreview() {
        const previewPanel = document.getElementById('previewPanel');
        const editorPanel = document.getElementById('editorPanel');
        
        if (previewPanel.style.display === 'none') {
            previewPanel.style.display = 'flex';
            editorPanel.style.width = '';
        } else {
            previewPanel.style.display = 'none';
            editorPanel.style.width = '100%';
            editorPanel.style.maxWidth = '100%';
        }
    }
    
    // =========================================================================
    // UTILIDADES
    // =========================================================================
    
    showToast(message, type = 'success') {
        const toast = document.getElementById('saveToast');
        const icon = toast.querySelector('.toast-icon');
        const msg = toast.querySelector('.toast-message');
        
        icon.className = `toast-icon ${type}`;
        icon.innerHTML = type === 'success' 
            ? '<i class="fas fa-check-circle"></i>' 
            : '<i class="fas fa-exclamation-circle"></i>';
        
        msg.textContent = message;
        
        toast.classList.add('show');
        setTimeout(() => toast.classList.remove('show'), 3000);
    }
}

// Inicializar cuando el DOM esté listo
document.addEventListener('DOMContentLoaded', () => {
    // Obtener el unit_id del iframe o de data attribute
    const iframe = document.getElementById('previewFrame');
    const match = iframe?.src.match(/\/units\/(\d+)/);
    const unitId = match ? parseInt(match[1]) : 1;
    
    window.unitEditor = new UnitEditor(unitId);
});
```

---

## 5. Estrategia de Vista Previa

### Recomendación: **Opción B - Renderizado en Cliente**

Para este caso, la opción más sencilla y efectiva es **renderizar el HTML directamente en el cliente** usando el mismo JSON que se edita. Aquí está la implementación:

### 5.1 Modificar el JavaScript para Preview en Tiempo Real

```javascript
// En app/static/js/unit_editor.js, agregar método:

updatePreviewRealTime() {
    const previewContent = document.getElementById('previewContent');
    const unitTitle = document.getElementById('unit-title').value;
    const topicItems = document.querySelectorAll('.topic-item');
    
    // Generar HTML de la vista previa
    let html = `
        <div class="preview-unit">
            <h1 class="preview-unit-title">${this.escapeHtml(unitTitle)}</h1>
            <p class="preview-unit-desc">${this.escapeHtml(document.getElementById('unit-description').value)}</p>
            
            <h5>Temas</h5>
            <div class="preview-topics">
    `;
    
    topicItems.forEach((item, index) => {
        const title = item.querySelector('.topic-title-input').value;
        const desc = item.querySelector('.topic-desc-input').value;
        
        html += `
            <div class="preview-topic-item">
                <span class="preview-topic-number">${index + 1}</span>
                <div>
                    <strong>${this.escapeHtml(title)}</strong>
                    <p class="text-muted small">${this.escapeHtml(desc)}</p>
                </div>
            </div>
        `;
    });
    
    html += '</div></div>';
    
    previewContent.innerHTML = html;
}

escapeHtml(text) {
    if (!text) return '';
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}
```

### 5.2 Alternativa con Iframe (Opción A)

Si prefieres usar iframe, modifica la ruta existente para aceptar datos POST temporales:

```python
# En app/routes/units.py, agregar:

@units_bp.route('/preview/<int:unit_id>', methods=['POST'])
def preview_unit(unit_id):
    """Vista previa temporal de una unidad"""
    # Obtener datos del POST o de BD
    if request.method == 'POST':
        data = request.get_json()
        # Crear objetos temporales
        unit = type('Unit', (), data.get('unit', {}))()
        topics = [type('Topic', (), t) for t in data.get('topics', [])]
    else:
        unit = Unit.query.get_or_404(unit_id)
        topics = Topic.query.filter_by(unit_id=unit_id).all()
    
    return render_template('unit_preview.html', unit=unit, topics=topics)
```

---

## 6. Seguridad

### 6.1 Decorador `admin_required`

Ya incluido en el código del archivo `admin.py`. Asegura que solo usuarios con `is_admin=True` puedan acceder.

### 6.2 Agregar campo is_admin al modelo User

```python
# En app/models.py, en el modelo User:
is_admin = db.Column(db.Boolean, default=False)
```

### 6.3 Para crear un admin

```python
# En una shell Flask
from app import create_app
from app.models import User, db

app = create_app()
with app.app_context():
    admin = User.query.filter_by(email='admin@example.com').first()
    if admin:
        admin.is_admin = True
        db.session.commit()
        print("Usuario es ahora administrador")
```

---

## 7. Flujo Paso a Paso

### 7.1 El Administrador Navega al Editor

```
1. Admin hace clic en "Editar Unidad" (desde dashboard admin o desde la unidad)
   ↓
2. Navegador → GET /admin/units/1/edit
   ↓
3. Flask ejecuta edit_unit() en admin.py
   ↓
4. Busca la unidad en BD
   ↓
5. Renderiza admin/edit_unit.html con unit y topics
   ↓
6. Navegador carga la página
```

### 7.2 Carga de Datos

```
7. JavaScript ejecuta UnitEditor.init()
   ↓
8. loadData() → GET /admin/api/units/1
   ↓
9. Flask ejecuta get_unit_data() 
   ↓
10. Retorna JSON con unit y topics
   ↓
11. JavaScript pobla el formulario y renderiza topics
```

### 7.3 Edición en Tiempo Real

```
12. Admin modifica el título de la unidad
    ↓
13. Evento 'input' detecta el cambio
    ↓
14. markDirty() marca cambios sin guardar
    ↓
15. updatePreview() actualiza el preview
```

### 7.4 Guardado

```
16. Admin hace clic en "Guardar Cambios"
    ↓
17. collectData() recopila todos los datos del formulario
    ↓
18. save() → POST /admin/api/units/1
    ↓
19. Flask ejecuta save_unit()
    ↓
20. UnitEditorService.save_all() procesa los datos:
    - Actualiza la unidad
    - Crea nuevos temas (sin ID)
    - Actualiza temas existentes (con ID)
    - Elimina temas marcados
    ↓
21. db.session.commit() guarda todo
    ↓
22. Retorna JSON con éxito
    ↓
23. JavaScript muestra toast de éxito
    ↓
24. Recarga datos para obtener IDs de nuevos temas
```

### 7.5 Diagrama Completo

```
┌─────────────────────────────────────────────────────────────────────────┐
│                           NAVEGADOR                                     │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────────────────┐ │
│  │  edit_unit  │    │  unit_editor │    │     preview-iframe      │ │
│  │    .html     │    │     .js      │    │                        │ │
│  └──────┬──────┘    └──────┬──────┘    └───────────┬─────────────┘ │
│         │                    │                        │              │
│         │                    │ loadData()            │              │
│         │                    │ save()                 │              │
│         │                    │ updatePreview()        │              │
└─────────┼────────────────────┼────────────────────────┼──────────────┘
          │                    │                        │
          │  render_template()│                        │ src="/units/1"
          │                    │ fetch()                │
┌─────────▼────────────────────▼────────────────────────▼──────────────┐
│                           FLASK                                         │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │                      admin.py                                     │   │
│  │  ┌────────────────┐  ┌────────────────┐  ┌────────────────────┐ │   │
│  │  │ edit_unit()    │  │ get_unit_data()│  │ save_unit()       │ │   │
│  │  │ /admin/units   │  │ GET /api/units │  │ POST /api/units   │ │   │
│  │  │ /1/edit        │  │ /<id>          │  │ /<id>             │ │   │
│  │  └───────┬────────┘  └───────┬────────┘  └─────────┬──────────┘ │   │
│  └──────────┼───────────────────┼─────────────────────┼────────────┘   │
└─────────────┼───────────────────┼─────────────────────┼────────────────┘
              │                   │                     │
┌─────────────▼───────────────────▼─────────────────────▼────────────────┐
│                        BASE DE DATOS                                   │
│                    PostgreSQL (SQLAlchemy)                            │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────────┐   │
│  │      Unit        │  │     Topic       │  │      UnitExtra      │   │
│  │  (UPDATE/INSERT)│  │ (CRUD completo) │  │     (UPDATE)       │   │
│  └─────────────────┘  └─────────────────┘  └─────────────────────┘   │
└───────────────────────────────────────────────────────────────────────┘
```

---

## 8. Dependencias Opcionales

### 8.1 Drag & Drop (Opcional)

Si deseas agregar drag & drop para reordenar temas:

```html
<!-- En el template, agregar antes del cierre de </body> -->
<script src="https://cdn.jsdelivr.net/npm/sortablejs@1.15.0/Sortable.min.js"></script>

<script>
// En unit_editor.js, agregar:
new Sortable(document.getElementById('topicsList'), {
    animation: 150,
    handle: '.topic-header',
    onEnd: function(evt) {
        // Reordenar array de topics
        editor.reorderTopics(evt.oldIndex, evt.newIndex);
    }
});
</script>
```

---

## 9. Checklist de Implementación

- [ ] Crear `app/routes/admin.py`
- [ ] Crear `app/services/unit_editor.py`
- [ ] Crear `app/templates/admin/edit_unit.html`
- [ ] Crear `app/static/css/admin/unit_editor.css`
- [ ] Crear `app/static/js/unit_editor.js`
- [ ] Registrar `admin_bp` en `app/__init__.py`
- [ ] Agregar campo `is_admin` al modelo User (si no existe)
- [ ] Crear un usuario admin
- [ ] Probar el flujo completo
- [ ] Opcional: Implementar drag & drop

---

*Guía de implementación - Editor de Unidades*
