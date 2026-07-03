# Fix: Navbar - Texto se mueve hacia abajo

## Problema
El menú de navegación tenía elementos que se movían hacia abajo cuando el texto era largo, causando une apariencia desigual.

## Solución Aplicada

### 1. CSS - navbar.css
- **Navbar base**: Agregado `min-height: 60px` y `flex-wrap: nowrap`
- **Nav links**: Agregado `white-space: nowrap`, `display: flex`, `align-items: center`
- **Nav items**: Agregado `display: flex`, `align-items: center`
- **Theme toggle**: Reducido tamaño y mejorado `flex-shrink: 0`
- **Dropdown**: Agregado `min-width: 200px`

### 2. HTML - base.html
- Agregado `align-items-lg-center` al navbar-nav

## Archivos Modificados
- `app/static/css/components/navbar.css`
- `app/templates/base.html`

## Notas
Si el problema persiste en pantallas pequeñas, considera:
1. Reducir el número de elementos en el menú
2. Usar abreviaturas (ej: "Estudio" en lugar de "Estudio Intensivo")
3. Hacer que el menú sea colapsable en tablets
