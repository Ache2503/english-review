# Función: start_exam()

## Información General

| Campo | Valor |
|-------|-------|
| **Nombre** | start_exam() |
| **Archivo** | app/routes/exams.py |
| **Ruta** | app/routes/exams.py |
| **Tipo** | Ruta Flask |

## Propósito

Inicia un examen simulado (TOEFL, IELTS, Cambridge) mostrando la primera sección.

## Flujo Lógico

1. Verifica usuario autenticado
2. Obtiene examen por ID
3. Verifica validez del examen
4. Crea intento de examen (UserExamAttempt)
5. Renderiza template con preguntas

## Parámetros

| Parámetro | Tipo | Descripción |
|-----------|------|-------------|
| exam_id | int | ID del examen |

## Tablas Utilizadas

- `exam_simulators` - Consulta examen
- `exam_sections` - Secciones del examen
- `user_exam_attempts` - Crear intento

## Templates Relacionados

- `exams/take.html` - Tomar examen

## Tipos de Examen Soportados

- TOEFL
- IELTS
- Cambridge

## Impacto si se Modifica

**Medio impacto** - Afecta:
- Exámenes simulados
- Historial de intentos
- Certificaciones
