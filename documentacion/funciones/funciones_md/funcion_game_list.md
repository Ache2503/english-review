# Función: game_list()

## Información General

| Campo | Valor |
|-------|-------|
| **Nombre** | game_list() |
| **Archivo** | app/routes/games.py |
| **Ruta** | app/routes/games.py |
| **Tipo** | Ruta Flask |

## Propósito

Muestra la lista de juegos educativos disponibles para practicar inglés.

## Flujo Lógico

1. Verifica usuario autenticado
2. Obtiene lista de juegos disponibles
3. Obtiene mejores puntuaciones del usuario
4. Renderiza template con juegos

## Juegos Disponibles

| Juego | Descripción |
|-------|-------------|
| Word Scramble | Ordenar letras |
| Hangman | Ahorcado |
| Memory | Memoria de palabras |
| Fill Gaps | Completar espacios |
| Quick Quiz | Quiz rápido |
| Speed Typing | Mecanografía |

## Parámetros

| Parámetro | Tipo | Descripción |
|-----------|------|-------------|
| Ninguno | - | - |

## Tablas Utilizadas

- `mini_games` - Catálogo de juegos
- `user_game_scores` - Puntuaciones usuario

## Templates Relacionados

- `games/list.html` - Lista de juegos

## Impacto si se Modifica

**Bajo impacto** - Afecta:
- Lista de juegos
- Acceso a juegos
