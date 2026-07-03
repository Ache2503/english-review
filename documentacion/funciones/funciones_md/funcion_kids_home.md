# Función: kids_home()

## Información General

| Campo | Valor |
|-------|-------|
| **Nombre** | kids_home() |
| **Archivo** | app/routes/kids.py |
| **Ruta** | app/routes/kids.py |
| **Tipo** | Ruta Flask |

## Propósito

Muestra la página principal de la zona infantil donde los niños pueden seleccionar su perfil y comenzar a aprender.

## Flujo Lógico

1. Verifica usuario autenticado y suscripción kids
2. Obtiene perfiles de niños asociados
3. Renderiza template para seleccionar perfil

## Decorador

```python
@login_required
@kids_zone_required  # custom decorator
```

## Parámetros

| Parámetro | Tipo | Descripción |
|-----------|------|-------------|
| Ninguno | - | - |

## Tablas Utilizadas

- `child_profiles` - Perfiles de niños
- `users` - Usuario padre
- `child_progress` - Progreso de cada niño

## Templates Relacionados

- `kids/select_profile.html` - Seleccionar perfil
- `kids/map.html` - Mapa de aprendizaje

## Restricciones

- Solo usuarios con `subscription_type = 'kids_pass'` o `'premium_all_access'`
- Edad del usuario padre debe ser mayor de 15 años

## Impacto si se Modifica

**Medio impacto** - Afecta:
- Zona infantil
- Perfiles de niños
- Progreso infantil
