# Función: list() - Conversation

## Información General

| Campo | Valor |
|-------|-------|
| **Nombre** | list() |
| **Archivo** | app/routes/conversation.py |
| **Ruta** | app/routes/conversation.py |
| **Tipo** | Ruta Flask |

## Propósito

Muestra la lista de escenarios de conversación disponibles para practicar inglés.

## Flujo Lógico

1. Verifica usuario autenticado
2. Obtiene lista de conversaciones disponibles
3. Verifica progreso del usuario en cada una
4. Renderiza template con conversaciones

## Parámetros

| Parámetro | Tipo | Descripción |
|-----------|------|-------------|
| Ninguno | - | - |

## Tablas Utilizadas

- `conversations` - Catálogo de conversaciones
- `conversation_practice` - Progreso usuario

## Templates Relacionados

- `conversation/conversation_list.html` - Lista conversaciones
- `conversation/conversation_detail.html` - Practicar

## Datos Hardcodeados

El archivo contiene diccionario `conversations` con ~10 escenarios hardcodeados que deberían estar en la base de datos.

## Impacto si se Modifica

**Medio impacto** - Afecta:
- Práctica de conversación
- Escenarios disponibles
