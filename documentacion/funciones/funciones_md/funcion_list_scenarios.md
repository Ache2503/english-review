# Función: list_scenarios()

## Información General

| Campo | Valor |
|-------|-------|
| **Nombre** | list_scenarios() |
| **Archivo** | app/routes/scenarios.py |
| **Ruta** | app/routes/scenarios.py |
| **Tipo** | Ruta Flask |

## Propósito

Muestra la lista de escenarios temáticos disponibles para compra o suscripción.

## Flujo Lógico

1. Verifica usuario autenticado
2. Obtiene lista de escenarios
3. Verifica cuáles están desbloqueados para el usuario
4. Muestra precio para los bloqueados
5. Renderiza template

## Parámetros

| Parámetro | Tipo | Descripción |
|-----------|------|-------------|
| Ninguno | - | - |

## Tablas Utilizadas

- `thematic_scenarios` - Catálogo de escenarios
- `user_unlocked_scenarios` - Escenarios desbloqueados

## Templates Relacionados

- `scenarios/list.html` - Lista escenarios
- `scenarios/preview.html` - Preview
- `scenarios/dashboard.html` - Dashboard

## Tipos de Escenario

- Restaurante
- Hotel
- Aeropuerto
- Tienda
- Oficina
- Hospital
- Y más...

## Sistema de Compra

- Comprar a la carta con puntos
- Desbloqueado con suscripción premium

## Impacto si se Modifica

**Medio impacto** - Afecta:
- Escenarios disponibles
- Monetización
