# 📋 RECOMENDACIONES PARA MANTENER EL SISTEMA DE TEMA

## 🎯 Guía para Desarrolladores

### ✅ Lo que SÍ hacer

#### 1. Usar Variables CSS
```css
/* ✅ CORRECTO */
.mi-componente {
    background-color: var(--bg-card);
    color: var(--text-main);
    border-color: var(--border-color);
}
```

#### 2. Agregar Estilos Dark Mode en Nuevos Componentes
```css
/* ✅ CORRECTO */
.mi-componente {
    background: white;
    color: #333;
}

@media (prefers-color-scheme: dark) {
    .mi-componente {
        background: var(--bg-card);
        color: var(--text-main);
    }
}
```

#### 3. Usar Colores Funcionales Consistentes
```css
/* ✅ CORRECTO */
.mi-boton-exito {
    background-color: #22c55e;  /* Verde en dark mode */
}

.mi-boton-error {
    background-color: #ef4444;  /* Rojo en dark mode */
}
```

---

### ❌ Lo que NO hacer

#### 1. Hardcodear Colores
```css
/* ❌ INCORRECTO */
.mi-componente {
    background-color: #0f172a;  /* Solo funciona en claro */
    color: #ffffff;             /* Solo funciona en oscuro */
}
```

#### 2. Olvidar Dark Mode
```css
/* ❌ INCORRECTO - Falta soporte dark */
.mi-componente {
    background: white;
    color: #333;
}
```

#### 3. Usar Colores Muy Oscuros en Dark Mode
```css
/* ❌ INCORRECTO - Demasiado oscuro, no se lee */
@media (prefers-color-scheme: dark) {
    .mi-componente {
        background: #000000;  /* Negro puro no contrasta bien */
    }
}
```

#### 4. Ignorar el Contraste
```css
/* ❌ INCORRECTO - Bajo contraste */
@media (prefers-color-scheme: dark) {
    .mi-componente {
        background: #0a0e27;
        color: #404050;  /* Muy oscuro, apenas visible */
    }
}
```

---

## 🎨 Variables Disponibles

### Fondos
```css
--bg-body:     #f8fafc (claro) / #0a0e27 (oscuro)
--bg-card:     #ffffff (claro) / #141829 (oscuro)
--input-bg:    #ffffff (claro) / #1a2332 (oscuro)
--footer-bg:   #020617 (ambos)
```

### Textos
```css
--text-main:    #0f172a (claro) / #f0f4f8 (oscuro)
--text-muted:   #64748b (claro) / #a8b8cc (oscuro)
--text-primary: #0f172a (claro) / #f0f4f8 (oscuro)
--text-secondary: #475569 (claro) / #d4dce8 (oscuro)
--text-light:   #64748b (claro) / #a8b8cc (oscuro)
```

### Bordes y Colores
```css
--border-color:    #e2e8f0 (claro) / #2a3f5f (oscuro)
--primary-color:   #2563eb
--success-color:   #16a34a
--warning-color:   #f59e0b
--danger-color:    #dc2626
--info-color:      #0ea5e9
```

---

## 📐 Checklist para Nuevos Componentes

Cuando crees un nuevo componente, verifica:

- [ ] ¿Usa variables CSS en lugar de colores hardcodeados?
- [ ] ¿Tiene estilos para dark mode (@media prefers-color-scheme: dark)?
- [ ] ¿El contraste es >= 4.5:1 en ambos modos?
- [ ] ¿Probé en navegador con dark mode activado?
- [ ] ¿Todos los textos son legibles?
- [ ] ¿Los inputs tienen suficiente contraste?
- [ ] ¿Los botones son clickeables y visibles?
- [ ] ¿Las imágenes se ven bien?
- [ ] ¿Los iconos son visibles?
- [ ] ¿Las animaciones funcionan en ambos modos?

---

## 🧪 Pruebas Recomendadas

### Test de Contraste Automático
```bash
# Herramienta: Chrome DevTools
1. F12 → Elements
2. Selecciona elemento
3. Click en "Accessibility" tab
4. Busca "Contrast ratio"
5. Debe ser >= 4.5:1 (AA) o 7:1 (AAA)
```

### Test Manual en Dark Mode
```
Chrome DevTools:
1. F12 → Cmd+Shift+P (o Ctrl+Shift+P)
2. "Emulate CSS media feature prefers-color-scheme"
3. Selecciona "dark"
4. Recarga página
5. Verifica todos los elementos
```

### Test en Dispositivos Reales
```
iPhone/iPad:
Settings → Display & Brightness → Dark

Android:
Settings → Display → Dark theme

Windows:
Settings → Personalization → Colors → Dark

macOS:
System Preferences → General → Appearance → Dark
```

---

## 🚨 Problemas Comunes y Soluciones

### Problema: Texto invisible en dark mode
```css
/* ❌ Mal */
color: #333;

/* ✅ Bien */
color: var(--text-main);
```

### Problema: Fondo blanco permanente
```css
/* ❌ Mal */
background: white !important;

/* ✅ Bien */
background: var(--bg-card);
```

### Problema: Inputs difíciles de ver
```css
/* ❌ Mal */
input {
    background: #1a1a1a;
    color: #555;
}

/* ✅ Bien */
input {
    background: var(--input-bg);
    color: var(--text-main);
}
```

### Problema: Bordes invisibles
```css
/* ❌ Mal */
border: 1px solid #ddd;  /* Desaparece en dark */

/* ✅ Bien */
border: 1px solid var(--border-color);
```

### Problema: Badges sin contraste
```css
/* ❌ Mal */
.badge {
    background: #f0f0f0;
    color: #808080;  /* Invisible en dark */
}

/* ✅ Bien */
.badge {
    background: var(--primary-color);
    color: white;
}
```

---

## 🔧 Herramientas Útiles

### WebAIM Contrast Checker
https://webaim.org/resources/contrastchecker/
- Verifica contraste de dos colores
- Proporciona ratio WCAG

### Color Brewer
https://colorbrewer2.org/
- Paletas de colores accesibles
- Simulación de daltonismo

### Chrome DevTools
- Built-in contrast verification
- Color picker con live preview
- Accesibility audit

### Firefox DevTools
- Inspector de contraste
- Herramientas de accesibilidad

---

## 📚 Ejemplos de Buenas Prácticas

### Componente Card
```css
.card {
    background-color: var(--bg-card);
    border: 1px solid var(--border-color);
    color: var(--text-main);
}

.card-title {
    color: var(--text-primary);
    font-weight: 600;
}

.card-text {
    color: var(--text-main);
}

@media (prefers-color-scheme: dark) {
    .card {
        background: linear-gradient(135deg, #1a2f4f, #141829);
    }
    
    .card-title {
        color: #ffffff;
    }
}
```

### Componente Botón
```css
.btn-primary {
    background: var(--primary-color);
    border-color: var(--primary-color);
    color: white;
}

.btn-primary:hover {
    background: var(--primary-hover);
    border-color: var(--primary-hover);
}

@media (prefers-color-scheme: dark) {
    .btn-primary {
        background: #3b82f6;
    }
    
    .btn-primary:hover {
        background: #60a5fa;
    }
}
```

### Componente Input
```css
input {
    background: var(--input-bg);
    color: var(--text-main);
    border: 1px solid var(--border-color);
}

input::placeholder {
    color: var(--text-light);
}

input:focus {
    border-color: var(--primary-color);
    background: var(--input-bg);
    color: var(--text-main);
}

@media (prefers-color-scheme: dark) {
    input {
        background: #1a2332;
    }
    
    input::placeholder {
        color: #a8b8cc;
    }
}
```

---

## 🎓 Lectura Recomendada

1. **WCAG 2.1 Guidelines**
   https://www.w3.org/WAI/WCAG21/quickref/

2. **CSS prefers-color-scheme**
   https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme

3. **Accessible Colors**
   https://www.a11yrocks.com/web-colors-and-accessibility/

4. **Design Systems with Dark Mode**
   https://www.figma.com/blog/managing-color-in-design-systems/

---

## 🔄 Flujo de Desarrollo Recomendado

```
1. Crear componente en MODO CLARO
   ↓
2. Agregar variables CSS en lugar de colores hardcodeados
   ↓
3. Agregar @media (prefers-color-scheme: dark)
   ↓
4. Probar en DevTools con dark mode
   ↓
5. Verificar contraste (ratio >= 4.5:1)
   ↓
6. Probar en dispositivo real
   ↓
7. Commit & Push
```

---

## 📞 Contacto y Soporte

Si encuentras issues con el tema:

1. Revisa `TEMA_AUTOMATICO_GUIDE.md`
2. Ejecuta `python3 verify_theme_system.py`
3. Abre DevTools (F12)
4. Reporta el elemento afectado
5. Especifica navegador, SO y tema

---

**Último actualizado**: Febrero 6, 2026
**Mantenedor**: English Learning Platform
**Versión**: 1.0

