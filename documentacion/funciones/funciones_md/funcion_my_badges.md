# Función: index() - Badges

## Información General

| Campo | Valor |
|-------|-------|
| **Nombre** | my_badges() |
| **Archivo** | app/routes/badges.py |
| **Ruta** | app/routes/badges.py |
| **Tipo** | Ruta Flask |

## Propósito

Muestra los logros (badges) obtenidos por el usuario y los disponibles por ganar.

## Flujo Lógico

1. Verifica usuario autenticado
2. Obtiene badges del usuario
3. Obtiene todos los badges disponibles
4. Marca cuáles tiene el usuario
5. Renderiza template

## Parámetros

| Parámetro | Tipo | Descripción |
|-----------|------|-------------|
| Ninguno | - | - |

## Tablas Utilizadas

- `badges` - Catálogo de badges
- `user_badges` - Badges obtenidos

## Templates Relacionados

- `badges/my_badges.html` - Mis logros
- `badges/all_badges.html` - Todos los logros

## Tipos de Badges

- Completar unidades
- Racha de días
- Puntuación alta en juegos
- Vocabulario aprendido
- Gramática dominada
- Y más...

## Impacto si se Modifica

**Bajo impacto** - Afecta:
- Vista de logros
- Gamificación
