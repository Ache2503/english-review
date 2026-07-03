# Problema: Conflicto con is_active en UserMixin

## Error Original

```
sqlalchemy.exc.ProgrammingError: no existe la columna users.account_active
```

## Causa

El modelo `User` heredaba de `UserMixin` que proporciona una propiedad `is_active`. Al agregar una columna `is_active` en el modelo, causaba un conflicto de nombres.

## Solución Aplicada

Se eliminó la columna `is_active` del modelo `User` y se utiliza la propiedad proporcionada por `UserMixin`.

### Código Anterior (problemático)
```python
class User(UserMixin, db.Model):
    is_active = db.Column(db.Boolean, default=True)  # CONFLICTO!
```

### Código Corregido
```python
class User(UserMixin, db.Model):
    # Nota: is_active viene de UserMixin
    is_admin = db.Column(db.Boolean, default=False)
```

## Alternativas Consideradas

1. **Renombrar columna**: Crear columna con otro nombre (`account_active`) - Requiere migración de BD
2. **Usar column_property**: Ignorar la propiedad de UserMixin - Más complejo
3. **Eliminar columna**: Usar la de UserMixin - Solución más simple

## Resultado

- ✅ Error de base de datos resuelto
- ⚠️ Warning LSP presente (no crítico): `RelationshipProperty[Any] is not iterable` en línea 112
  - Este warning es un false positive del LSP y no afecta la funcionalidad

## Archivos Modificados

- `app/models.py` - Eliminado `account_active`, ahora usa `is_active` de UserMixin
