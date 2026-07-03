# Función: analyze_text() - Writing

## Información General

| Campo | Valor |
|-------|-------|
| **Nombre** | analyze_text() |
| **Archivo** | app/routes/writing.py |
| **Ruta** | app/routes/writing.py |
| **Tipo** | Ruta Flask |

## Propósito

Analiza el texto escrito por el usuario verificando gramática, ortografía y estilo.

## Flujo Lógico

1. Recibe texto del formulario
2. Envía texto al servicio de análisis
3. Obtiene errores y sugerencias
4. Guarda análisis en log
5. Retorna resultados

## Parámetros

| Parámetro | Tipo | Descripción |
|-----------|------|-------------|
| text | str | Texto a analizar |

## Tablas Utilizadas

- `writing_analysis_logs` - Guarda análisis

## Templates Relacionados

- `writing/analyze.html` - Resultados

## Archivos Relacionados

- `app/services/writing_analysis.py` - Lógica de análisis

## Impacto si se Modifica

**Medio impacto** - Afecta:
- Análisis de escritura
- Feedback al usuario
