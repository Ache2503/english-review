# Conversational Practice Feature

Esta guía te explica cómo agregar una sección de práctica de inglés conversacional a tu plataforma. El objetivo es que los usuarios puedan elegir entre diferentes escenarios (tienda, buscar direcciones, saludos, etc.) y practicar conversaciones.

## 1. Crear la Ruta Backend
- Ubicación: `app/routes/conversation.py`
- Define una ruta para mostrar la lista de escenarios y otra para mostrar la conversación seleccionada.
- Ejemplo:
  - `/conversation` (lista de escenarios)
  - `/conversation/<scenario>` (detalle de la conversación)

## 2. Crear la Plantilla HTML
- Ubicación: `app/templates/conversation_list.html` y `app/templates/conversation_detail.html`
- `conversation_list.html`: muestra los escenarios disponibles.
- `conversation_detail.html`: muestra la conversación seleccionada.

## 3. Datos de Conversaciones
- Puedes definir los escenarios y diálogos en el mismo archivo de ruta como una lista/diccionario, o en un archivo JSON para mayor escalabilidad.
- Ejemplo de estructura:
  ```python
  conversations = {
      'tienda': {
          'title': 'En la tienda',
          'dialogue': [
              {'speaker': 'Cliente', 'text': 'Hola, ¿tienen pan fresco?'},
              {'speaker': 'Vendedor', 'text': 'Sí, aquí está.'},
              # ...
          ]
      },
      # ...otros escenarios
  }
  ```

## 4. Enlazar en el Menú
- Agrega un enlace en el menú principal o dashboard para acceder a la nueva sección.
- Ejemplo:
  ```html
  <a href="{{ url_for('conversation.list') }}">Práctica Conversacional</a>
  ```

## 5. (Opcional) Mejoras Futuras
- Guardar el progreso del usuario.
- Permitir que el usuario agregue sus propias conversaciones.
- Integrar audio para escuchar la pronunciación.

## 6. Resumen de Archivos a Crear/Editar
- `app/routes/conversation.py` (nuevo)
- `app/templates/conversation_list.html` (nuevo)
- `app/templates/conversation_detail.html` (nuevo)
- Editar menú en `base.html` o `dashboard.html`
- (Opcional) Crear `app/data/conversations.json`

---
Sigue estos pasos y tendrás una sección funcional de práctica conversacional. Si necesitas el código base para cada archivo, pídelo y te lo genero.