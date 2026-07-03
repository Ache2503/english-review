# Función: check_grammar_errors()

## Información General

| Campo | Valor |
|-------|-------|
| **Nombre** | check_grammar_errors() |
| **Archivo** | app/services/feedback.py |
| **Ruta** | app/services/feedback.py |
| **Tipo** | Servicio (Lógica de negocio) |

## Propósito

Utiliza LanguageTool API para verificar errores gramaticales y ortográficos en el texto del usuario.

## Flujo Lógico

1. Recibe texto a verificar
2. Envía solicitud a LanguageTool API
3. Procesa respuesta con errores
4. Retorna lista de errores encontrados

## Parámetros

| Parámetro | Tipo | Descripción |
|-----------|------|-------------|
| text | str | Texto a verificar |

## Retorna

```python
{
    'matches': [
        {
            'message': 'Error description',
            'context': 'Text with error',
            'offset': int,
            'length': int,
            'rule': 'ruleId'
        }
    ]
}
```

## Dependencias Externas

- **LanguageTool API** - Servicio externo de verificación

## Tablas Utilizadas

- Ninguna 直接 (usa API externa)

## Archivos Relacionados

- `app/routes/practice.py` - api_analyze()
- `app/routes/writing.py` - analyze_text()

## Manejo de Errores

```python
try:
    response = requests.post(LANGUAGETOOL_API, json={'text': text})
    return response.json()
except Exception as e:
    return {'matches': [], 'error': str(e)}
```

## Impacto si se Modifica

**Alto impacto** - Afecta:
- Verificación de gramática
- Análisis de escritura
- Feedback al usuario
