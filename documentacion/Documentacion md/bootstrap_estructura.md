# Estructura de Bootstrap en el Proyecto

## 1. Resumen del Uso de Bootstrap

**Versión**: Bootstrap 5.3.0
**Carga**: CDN jsdelivr (`https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css`)

---

## 2. Clases Bootstrap Utilizadas

### 2.1 Grid System

| Clase | Elemento | Función |
|-------|----------|---------|
| `.container` | div | Contenedor con ancho fijo |
| `.container-fluid` | div | Contenedor ancho completo |
| `.row` | div | Fila del grid |
| `.col-*` | div | Columna (1-12) |
| `.col-md-4` | div | Columna media (4/12) |
| `.col-md-6` | div | Columna media (6/12) |
| `.col-md-8` | div | Columna media (8/12) |
| `.col-md-12` | div | Columna completa |
| `.text-md-center` | div | Alineación texto en desktop |
| `.text-md-end` | div | Alineación derecha desktop |

**Ejemplo en templates**:
```html
<div class="container">
    <div class="row">
        <div class="col-md-4">Sidebar</div>
        <div class="col-md-8">Contenido principal</div>
    </div>
</div>
```

---

### 2.2 Navbar (Barra de Navegación)

| Clase | Elemento | Función |
|-------|----------|---------|
| `.navbar` | nav | Contenedor navbar |
| `.navbar-expand-lg` | nav | Expansión en large |
| `.navbar-brand` | a | Logo/marca |
| `.navbar-toggler` | button | Botón colapso móvil |
| `.navbar-collapse` | div | Contenedor colapsable |
| `.navbar-nav` | ul | Lista de navegación |
| `.nav-item` | li | Elemento de navegación |
| `.nav-link` | a | Enlace de navegación |

**Ejemplo en base.html**:
```html
<nav class="navbar navbar-expand-lg">
    <div class="container">
        <a class="navbar-brand" href="/">
            <i class="fas fa-book"></i> English Learning
        </a>
        <button class="navbar-toggler" data-bs-toggle="collapse" data-bs-target="#navbarNav">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav ms-auto">
                <li class="nav-item">
                    <a class="nav-link" href="/dashboard">Dashboard</a>
                </li>
            </ul>
        </div>
    </div>
</nav>
```

---

### 2.3 Buttons (Botones)

| Clase | Elemento | Función |
|-------|----------|---------|
| `.btn` | button/a | Botón base |
| `.btn-primary` | button/a | Botón primario (azul) |
| `.btn-secondary` | button/a | Botón secundario |
| `.btn-success` | button/a | Botón éxito (verde) |
| `.btn-danger` | button/a | Botón peligro (rojo) |
| `.btn-warning` | button/a | Botón advertencia |
| `.btn-info` | button/a | Botón info (azul claro) |
| `.btn-outline-*` | button/a | Botón outline |
| `.btn-sm` | button/a | Botón pequeño |
| `.btn-lg` | button/a | Botón grande |
| `.rounded-pill` | button/a | Bordes redondeados |
| `.rounded-circle` | button/a | Circular |

**Ejemplos**:
```html
<button class="btn btn-primary">Primary</button>
<button class="btn btn-outline-success rounded-pill">Success Outline</button>
<a href="/..." class="btn btn-sm btn-info">Small Info</a>
```

---

### 2.4 Forms (Formularios)

| Clase | Elemento | Función |
|-------|----------|---------|
| `.form-control` | input/select/textarea | Campo de formulario |
| `.form-label` | label | Etiqueta de formulario |
| `.form-text` | small | Texto de ayuda |
| `.form-check` | div | Contenedor checkbox/radio |
| `.form-check-input` | input | Checkbox/radio |
| `.form-check-label` | label | Etiqueta checkbox |
| `.input-group` | div | Grupo de inputs |
| `.input-group-text` | span | Texto en grupo |

**Ejemplo**:
```html
<form>
    <div class="mb-3">
        <label class="form-label">Email</label>
        <input type="email" class="form-control" placeholder="email@example.com">
        <div class="form-text">Nunca compartiremos tu email.</div>
    </div>
    <div class="mb-3 form-check">
        <input type="checkbox" class="form-check-input" id="remember">
        <label class="form-check-label" for="remember">Recordarme</label>
    </div>
    <button type="submit" class="btn btn-primary">Enviar</button>
</form>
```

---

### 2.5 Cards (Tarjetas)

| Clase | Elemento | Función |
|-------|----------|---------|
| `.card` | div | Contenedor tarjeta |
| `.card-body` | div | Cuerpo de tarjeta |
| `.card-title` | h* | Título tarjeta |
| `.card-text` | p | Texto tarjeta |
| `.card-img-top` | img | Imagen superior |
| `.card-header` | div | Encabezado tarjeta |
| `.card-footer` | div | Pie de tarjeta |

**Ejemplo**:
```html
<div class="card">
    <img src="/img.jpg" class="card-img-top" alt="...">
    <div class="card-body">
        <h5 class="card-title">Título</h5>
        <p class="card-text">Contenido...</p>
        <a href="#" class="btn btn-primary">Ir somewhere</a>
    </div>
</div>
```

---

### 2.6 Alerts (Alertas)

| Clase | Elemento | Función |
|-------|----------|---------|
| `.alert` | div | Alerta base |
| `.alert-primary` | div | Alerta primaria |
| `.alert-success` | div | Alerta éxito |
| `.alert-danger` | div | Alerta peligro |
| `.alert-warning` | div | Alerta advertencia |
| `.alert-info` | div | Alerta info |
| `.alert-dismissible` | div | Alerta cerrable |
| `.fade` | div | Transición fade |
| `.show` | div | Visible |

**Ejemplo en base.html (Flash Messages)**:
```html
{% with messages = get_flashed_messages(with_categories=true) %}
    {% if messages %}
        {% for category, message in messages %}
            <div class="alert alert-{{ category }} alert-dismissible fade show" role="alert">
                {{ message }}
                <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
            </div>
        {% endfor %}
    {% endif %}
{% endwith %}
```

---

### 2.7 Modals (Ventanas Modales)

| Clase | Elemento | Función |
|-------|----------|---------|
| `.modal` | div | Contenedor modal |
| `.modal-dialog` | div | Diálogo modal |
| `.modal-content` | div | Contenido modal |
| `.modal-header` | div | Encabezado |
| `.modal-body` | div | Cuerpo |
| `.modal-footer` | div | Pie |
| `.modal-title` | h* | Título |
| `.modal-lg` | div | Modal grande |
| `.modal-sm` | div | Modal pequeño |

**Atributos data-bs-**:
```html
<button data-bs-toggle="modal" data-bs-target="#myModal">Abrir</button>
<div class="modal fade" id="myModal">
    <div class="modal-dialog">
        <div class="modal-content">
            <!-- header, body, footer -->
        </div>
    </div>
</div>
```

---

### 2.8 Progress (Barras de Progreso)

| Clase | Elemento | Función |
|-------|----------|---------|
| `.progress` | div | Contenedor barra |
| `.progress-bar` | div | Barra de progreso |
| `.progress-bar-striped` | div | Barra rayada |
| `.progress-bar-animated` | div | Animada |

**Ejemplo**:
```html
<div class="progress">
    <div class="progress-bar" role="progressbar" style="width: 75%">75%</div>
</div>
```

---

### 2.9 Dropdowns (Menús Desplegables)

| Clase | Elemento | Función |
|-------|----------|---------|
| `.dropdown` | div | Contenedor dropdown |
| `.dropdown-toggle` | button/a | Botón toggle |
| `.dropdown-menu` | ul | Menú desplegable |
| `.dropdown-item` | a | Elemento menú |
| `.dropdown-divider` | hr | Separador |
| `.dropdown-menu-end` | ul | Alineación derecha |

**Ejemplo en base.html**:
```html
<li class="nav-item dropdown">
    <a class="nav-link dropdown-toggle" href="#" data-bs-toggle="dropdown">
        Usuario
    </a>
    <ul class="dropdown-menu dropdown-menu-end">
        <li><a class="dropdown-item" href="/profile">Perfil</a></li>
        <li><hr class="dropdown-divider"></li>
        <li><a class="dropdown-item" href="/logout">Cerrar</a></li>
    </ul>
</li>
```

---

### 2.10 Utilidades de Espaciado

| Clase | Función |
|-------|---------|
| `.m-0` | margin: 0 |
| `.mt-3` | margin-top: 1rem |
| `.mb-3` | margin-bottom: 1rem |
| `.ms-auto` | margin-left: auto |
| `.me-2` | margin-right: 0.5rem |
| `.p-3` | padding: 1rem |
| `.px-4` | padding-x: 1.5rem |
| `.py-2` | padding-y: 0.5rem |

---

### 2.11 Utilidades de Texto

| Clase | Función |
|-------|---------|
| `.text-center` | text-align: center |
| `.text-start` | text-align: left |
| `.text-end` | text-align: right |
| `.text-white` | color: white |
| `.text-white-50` | color: rgba(255,255,255,0.5) |
| `.text-primary` | color: primary |
| `.text-success` | color: success |
| `.text-danger` | color: danger |
| `.text-muted` | color: muted |
| `.fw-bold` | font-weight: bold |
| `.fst-italic` | font-style: italic |

---

### 2.12 Utilidades de Visualización

| Clase | Función |
|-------|---------|
| `.d-none` | display: none |
| `.d-block` | display: block |
| `.d-inline` | display: inline |
| `.d-flex` | display: flex |
| `.d-inline-block` | display: inline-block |
| `.d-md-block` | display block en medium+ |
| `.d-lg-none` | hide en large+ |

---

### 2.13 Badges y Tags

| Clase | Elemento | Función |
|-------|----------|---------|
| `.badge` | span | Badge base |
| `.bg-primary` | span | Badge primario |
| `.rounded-pill` | span | Redondeado |

---

### 2.14 Tablas

| Clase | Elemento | Función |
|-------|----------|---------|
| `.table` | table | Tabla base |
| `.table-striped` | table | Filas alternas |
| `.table-bordered` | table | Bordes |
| `.table-hover` | table | Hover filas |
| `.table-dark` | table | Estilo oscuro |

---

### 2.15 Breadcrumbs

| Clase | Elemento | Función |
|-------|----------|---------|
| `.breadcrumb` | ol | Breadcrumb base |
| `.breadcrumb-item` | li | Elemento |

---

### 2.16 Pagination

| Clase | Elemento | Función |
|-------|----------|---------|
| `.pagination` | ul | Paginación base |
| `.page-item` | li | Elemento página |
| `.page-link` | a | Enlace página |
| `.active` | li | Página activa |
| `.disabled` | li | Deshabilitado |

---

### 2.17 Accordion

| Clase | Elemento | Función |
|-------|----------|---------|
| `.accordion` | div | Accordion base |
| `.accordion-item` | div | Item |
| `.accordion-header` | div | Encabezado |
| `.accordion-button` | button | Botón colapsable |
| `.accordion-collapse` | div | Contenido colapsable |
| `.accordion-body` | div | Cuerpo |

---

### 2.18 Tabs

| Clase | Elemento | Función |
|-------|----------|---------|
| `.nav-tabs` | ul | Tabs navegación |
| `.nav-pills` | ul | Pills navegación |
| `.nav-link` | a | Enlace tab |
| `.active` | a | Tab activa |
| `.tab-content` | div | Contenido tabs |
| `.tab-pane` | div | Panel tab |
| `.fade` | div | Transición |

---

## 3. Componentes Personalizados

El proyecto complementa Bootstrap con CSS personalizado en:

- `app/static/css/components/` (18 archivos)
- `app/static/css/modules/` (15 archivos)

### Componentes personalizados destacados:
- `buttons.css` - Estilos adicionales para botones
- `navbar.css` - Personalización del navbar
- `cards.css` - Variantes de tarjetas
- `modal.css` - Modales custom
- `forms.css` - Formularios estilizados
- `loading.css` - Animaciones de carga

---

## 4. Theme Support (Light/Dark)

El proyecto implementa theme toggle usando data-bs-theme:

```html
<html data-bs-theme="light">
    <!-- o "dark" -->
</html>
```

Con soporte en `theme-detector.js` que detecta preferencia del sistema.

---

*Documento de uso de Bootstrap - English Learning Platform*