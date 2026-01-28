# 📱 GUÍA DE RESPONSIVIDAD PARA DESARROLLADORES

## 📖 Tabla de Contenidos
1. [Principios Fundamentales](#principios-fundamentales)
2. [Estructura Básica](#estructura-básica)
3. [CSS Responsivo](#css-responsivo)
4. [Componentes Comunes](#componentes-comunes)
5. [Testing](#testing)
6. [Mejores Prácticas](#mejores-prácticas)
7. [Troubleshooting](#troubleshooting)

---

## 🎯 Principios Fundamentales

### Mobile First
Siempre empieza con estilos para móviles y agrega complejidad conforme crece el viewport.

```css
/* ❌ EVITAR: Desktop first */
.card { display: grid; grid-template-columns: repeat(4, 1fr); }
@media (max-width: 768px) { .card { grid-template-columns: 1fr; } }

/* ✅ USAR: Mobile first */
.card { display: block; }
@media (min-width: 768px) { .card { display: grid; grid-template-columns: repeat(2, 1fr); } }
```

### Tipografía Fluida
Usa `clamp()` para que los tamaños de fuente se adapten automáticamente.

```css
/* ❌ EVITAR: Tamaño fijo */
h1 { font-size: 2.5rem; }
@media (max-width: 768px) { h1 { font-size: 1.75rem; } }

/* ✅ USAR: Tamaño fluido */
h1 { font-size: clamp(1.75rem, 5vw, 2.5rem); }
```

### Unidades Relativas
Usa `rem`, `em`, `%`, `vw` en lugar de `px` fijo.

```css
/* ❌ EVITAR */
padding: 20px;
margin: 10px;
width: 500px;

/* ✅ USAR */
padding: 1.25rem;      /* 20px en base 16px */
margin: 0.625rem;      /* 10px en base 16px */
width: 100%;           /* Ancho flexible */
```

---

## 🏗️ Estructura Básica

### Herencia del Base.html
Todos los templates heredan de `base.html` que incluye:

```html
<!-- ✅ Todos los templates ya heredan esto -->
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- ... más meta tags ... -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
</head>
<body>
    <!-- Navbar con hamburger menu -->
    <!-- Contenido heredado -->
</body>
</html>
```

### Template Heredado
```html
{% extends "base.html" %}

{% block title %}Mi Página - English Learning{% endblock %}

{% block content %}
<div class="container">
    <div class="row">
        <div class="col-md-6 col-lg-4">
            <!-- El grid se adapta automáticamente -->
            <div class="card">
                <img src="..." class="card-img-top img-fluid" alt="...">
                <div class="card-body">
                    <h5 class="card-title">Título</h5>
                    <p class="card-text">Descripción</p>
                </div>
            </div>
        </div>
    </div>
</div>
{% endblock %}
```

---

## 🎨 CSS Responsivo

### Breakpoints Bootstrap Integrados

```css
/* 576px and up */
@media (min-width: 576px) { }

/* 768px and up */
@media (min-width: 768px) { }

/* 992px and up */
@media (min-width: 992px) { }

/* 1200px and up */
@media (min-width: 1200px) { }

/* 1400px and up */
@media (min-width: 1400px) { }
```

### Tipografía Responsiva
```css
/* Headings - tamaño automático según viewport */
h1 { font-size: clamp(1.75rem, 5vw, 2.5rem); }    /* min, preferido, max */
h2 { font-size: clamp(1.5rem, 4vw, 2rem); }
h3 { font-size: clamp(1.25rem, 3vw, 1.5rem); }

/* Body text - siempre legible */
body { font-size: clamp(0.9rem, 1.5vw, 1.1rem); }

/* Labels de formulario */
label { font-size: clamp(0.85rem, 1.2vw, 1rem); }
```

### Espaciado Responsivo
```css
/* Padding/Margin fluido */
.section-padding { padding: clamp(1rem, 3vw, 2rem); }

/* Gap en flexbox/grid */
.grid-gap { gap: clamp(0.5rem, 2vw, 1.5rem); }

/* Container padding */
.container { padding: 0 clamp(1rem, 3vw, 1.5rem); }
```

### Layouts Flexbox

```css
/* Centrado automático */
.flex-center {
    display: flex;
    align-items: center;
    justify-content: center;
}

/* Espaciado entre items */
.flex-between {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

/* Wrap automático en móviles */
.flex-wrap {
    display: flex;
    flex-wrap: wrap;
    gap: 1rem;
}
```

### Grid Responsivo

```css
/* Auto-fit: rellena columnas automáticamente */
.grid-auto {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1.5rem;
}

/* Auto-fill: crea columnas vacías si es necesario */
.grid-fill {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 1rem;
}

/* Manual: control total */
.grid-manual {
    display: grid;
    grid-template-columns: 1fr;
}

@media (min-width: 768px) {
    .grid-manual { grid-template-columns: repeat(2, 1fr); }
}

@media (min-width: 992px) {
    .grid-manual { grid-template-columns: repeat(3, 1fr); }
}
```

---

## 🧩 Componentes Comunes

### Navbar Responsivo
```html
<nav class="navbar navbar-expand-lg navbar-dark">
    <div class="container">
        <a class="navbar-brand" href="/">English Learning</a>
        <!-- Hamburger toggler aparece automáticamente en móviles -->
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav ms-auto">
                <li class="nav-item"><a class="nav-link" href="#">Home</a></li>
                <li class="nav-item"><a class="nav-link" href="#">About</a></li>
            </ul>
        </div>
    </div>
</nav>
```

### Grid de Tarjetas
```html
<div class="container">
    <div class="row g-3">
        <!-- Las columnas se adaptan automáticamente -->
        <div class="col-12 col-sm-6 col-md-4 col-lg-3">
            <div class="card">
                <img src="..." class="card-img-top img-fluid" alt="...">
                <div class="card-body">
                    <h5 class="card-title">Título</h5>
                    <p class="card-text">Descripción</p>
                </div>
            </div>
        </div>
    </div>
</div>
```

Clases Bootstrap responsivas:
- `col-12`: 100% en móviles (< 576px)
- `col-sm-6`: 50% en tablets pequeños (≥ 576px)
- `col-md-4`: 33.33% en tablets (≥ 768px)
- `col-lg-3`: 25% en desktops (≥ 992px)

### Tabla Responsiva
```html
<div class="table-responsive">
    <table class="table">
        <thead>
            <tr>
                <th>Columna 1</th>
                <th>Columna 2</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Data 1</td>
                <td>Data 2</td>
            </tr>
        </tbody>
    </table>
</div>
```

### Formulario Responsivo
```html
<form>
    <div class="mb-3">
        <label for="email" class="form-label">Email</label>
        <input type="email" class="form-control" id="email">
    </div>
    
    <div class="row">
        <div class="col-md-6 mb-3">
            <label for="firstName" class="form-label">Nombre</label>
            <input type="text" class="form-control" id="firstName">
        </div>
        <div class="col-md-6 mb-3">
            <label for="lastName" class="form-label">Apellido</label>
            <input type="text" class="form-control" id="lastName">
        </div>
    </div>
    
    <button type="submit" class="btn btn-primary">Enviar</button>
</form>
```

### Hero Section Responsivo
```html
<section class="hero-section py-5">
    <div class="container">
        <div class="row align-items-center">
            <div class="col-lg-6">
                <h1 class="display-4">Título Principal</h1>
                <p class="lead">Descripción atractiva</p>
                <a href="#" class="btn btn-primary btn-lg">Acción</a>
            </div>
            <div class="col-lg-6">
                <img src="..." class="img-fluid" alt="...">
            </div>
        </div>
    </div>
</section>

<style>
    .hero-section {
        padding: clamp(2rem, 5vw, 4rem) 0;
    }
    
    .hero-section h1 {
        font-size: clamp(2rem, 6vw, 3.5rem);
        margin-bottom: 1rem;
    }
</style>
```

---

## 🧪 Testing

### Chrome DevTools
1. Abre DevTools (F12 o Ctrl+Shift+I)
2. Click en "Toggle device toolbar" (Ctrl+Shift+M)
3. Selecciona diferentes dispositivos del dropdown
4. Verifica que todo se ve correcto

### Dispositivos a Probar Manualmente

**Mobile (320px - 479px)**
```
☐ Navbar con hamburger menu
☐ Texto legible sin zoom
☐ Botones clickeables
☐ Sin scroll horizontal
☐ Imágenes escaladas correctamente
```

**Tablet (480px - 767px)**
```
☐ Navbar parcialmente expandido
☐ 2 columnas de contenido
☐ Imágenes balanceadas
☐ Spacing adecuado
☐ Tablas con scroll
```

**Desktop (768px+)**
```
☐ Navbar completamente expandido
☐ Layout multi-columna
☐ Hover effects funcionando
☐ Máxima velocidad
☐ Responsive dentro de max-width
```

### Herramientas Automáticas

**Google Mobile-Friendly Test**
```
URL: https://search.google.com/test/mobile-friendly
Verifica: Responsividad básica de Google
```

**PageSpeed Insights**
```
URL: https://pagespeed.web.dev/
Verifica: Performance + responsividad
```

**Responsive Design Checker**
```
URL: https://responsivedesignchecker.com/
Verifica: Múltiples resoluciones simultáneamente
```

### Script de Testing (Python)
```bash
# Ejecutar análisis de responsividad
python check_responsiveness.py

# Ejecutar test visual
python test_responsiveness_visual.py
```

---

## 💡 Mejores Prácticas

### ✅ DO (Hacer)

1. **Usar unidades relativas**
```css
/* ✅ Bien */
padding: 1rem;
font-size: 1.1rem;
width: 100%;
```

2. **Usar clamp() para fluidez**
```css
/* ✅ Bien */
font-size: clamp(1rem, 2vw, 1.5rem);
padding: clamp(1rem, 3vw, 2rem);
```

3. **Mobile first**
```css
/* ✅ Bien */
.card { display: block; }
@media (min-width: 768px) { .card { display: grid; } }
```

4. **Imágenes responsive**
```html
<!-- ✅ Bien -->
<img src="..." class="img-fluid" alt="...">
<img src="..." style="max-width: 100%; height: auto;" alt="...">
```

5. **Viewport meta tag**
```html
<!-- ✅ Bien -->
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

### ❌ DON'T (No hacer)

1. **No usar px fijo**
```css
/* ❌ Evitar */
padding: 20px;
font-size: 16px;
```

2. **No usar overflow-x hidden indiscriminadamente**
```css
/* ❌ Evitar */
body { overflow-x: hidden; }
```

3. **No usar números mágicos**
```css
/* ❌ Evitar */
.sidebar { width: 300px; }
.card { width: 400px; }

/* ✅ Usar */
.sidebar { width: clamp(250px, 30%, 350px); }
.card { width: 100%; max-width: 400px; }
```

4. **No depender de breakpoints fijos**
```css
/* ❌ Evitar */
@media (max-width: 768px) { } /* Qué pasa en 769px? */

/* ✅ Usar */
@media (max-width: 767px) { } /* Clear boundary */
@media (min-width: 768px) { } /* Clear boundary */
```

5. **No olvidar testing en móviles reales**
```
❌ Evitar: Solo probar en DevTools
✅ Hacer: Probar también en dispositivos reales
```

---

## 🔧 Troubleshooting

### Problema: Navbar no colapsa en móvil
```html
<!-- ✅ Asegúrate que tiene navbar-expand-lg -->
<nav class="navbar navbar-expand-lg navbar-dark">
    <button class="navbar-toggler" ...></button>
</nav>
```

### Problema: Imágenes desbordan el contenedor
```html
<!-- ✅ Agrega img-fluid -->
<img src="..." class="img-fluid" alt="...">

<!-- O CSS -->
<img src="..." style="max-width: 100%; height: auto;" alt="...">
```

### Problema: Texto muy pequeño en móvil
```css
/* ✅ Usa clamp() en lugar de media queries */
body { font-size: clamp(0.9rem, 2vw, 1.1rem); }

/* O establece tamaño mínimo */
body { font-size: 16px; } /* Mínimo para evitar zoom automático */
```

### Problema: Botones no clickeables en móvil
```css
/* ✅ Asegúrate que tienen altura mínima de 44px */
.btn { min-height: 44px; }
```

### Problema: Layout se rompe en ciertas resoluciones
```css
/* ✅ Usa breakpoints correctos */
@media (min-width: 768px) { }  /* Cambio en ≥768px */
@media (min-width: 992px) { }  /* Cambio en ≥992px */
@media (min-width: 1200px) { } /* Cambio en ≥1200px */
```

### Problema: Scroll horizontal inesperado
```css
/* ✅ Verifica overflow */
* { box-sizing: border-box; } /* Siempre incluye esto */

body {
    overflow-x: hidden;        /* Solo si es necesario */
}

/* ✅ Verifica max-width */
.container { max-width: 100vw; } /* Mal */
.container { max-width: 100%; }  /* Bien */
```

---

## 📊 Referencias Rápidas

### Clases Bootstrap Responsivas
```html
<!-- Columnas adaptables -->
<div class="col-sm-6 col-md-4 col-lg-3"></div>

<!-- Display responsivo -->
<div class="d-none d-md-block"></div>  <!-- Oculto en móvil, visible en md+ -->
<div class="d-md-none"></div>          <!-- Visible en móvil, oculto en md+ -->

<!-- Texto responsivo -->
<p class="fs-1"></p>  <!-- Tamaño 1 (grande) -->
<p class="fs-5"></p>  <!-- Tamaño 5 (normal) -->
<p class="fs-6"></p>  <!-- Tamaño 6 (pequeño) -->

<!-- Spacing responsivo -->
<div class="p-2 p-md-4 p-lg-5"></div>  <!-- Padding adaptable -->
<div class="m-2 m-md-4 m-lg-5"></div>  <!-- Margin adaptable -->
```

### Media Query Helpers
```css
/* Devices comunes */
@media (min-width: 576px) { }   /* sm: tablets pequeños */
@media (min-width: 768px) { }   /* md: tablets */
@media (min-width: 992px) { }   /* lg: desktops */
@media (min-width: 1200px) { }  /* xl: desktops grandes */
@media (min-width: 1400px) { }  /* xxl: ultra-wide */

/* Orientación */
@media (orientation: portrait) { }  /* Vertical */
@media (orientation: landscape) { } /* Horizontal */

/* Touch devices */
@media (hover: none) and (pointer: coarse) { }

/* Print */
@media print { }

/* Dark mode */
@media (prefers-color-scheme: dark) { }

/* Reduced motion */
@media (prefers-reduced-motion: reduce) { }
```

---

## 📞 Recursos Útiles

- **MDN - Responsive Design**: https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Responsive_Design
- **Bootstrap Documentation**: https://getbootstrap.com/docs/5.3/
- **CSS Tricks - A Complete Guide to Grid**: https://css-tricks.com/snippets/css/complete-guide-grid/
- **CSS Tricks - A Complete Guide to Flexbox**: https://css-tricks.com/snippets/css/a-guide-to-flexbox/
- **Web.dev - Responsive Web Design Basics**: https://web.dev/responsive-web-design-basics/

---

**Última actualización:** 27/01/2026  
**Mantener responsividad:** Estos principios son fundamentales para la experiencia del usuario
