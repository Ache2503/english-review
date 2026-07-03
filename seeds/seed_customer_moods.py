"""
Seed para CustomerMood - Estados de ánimo del cliente en roleplay
==================================================================
Puebla la tabla customer_moods con los 4 estados de ánimo usados
por el simulador de roleplay.
"""

import sys
sys.path.insert(0, '.')

from app import create_app
from app.extensions import db
from app.models import CustomerMood

app = create_app()

MOODS = [
    {
        'name': 'happy',
        'display_name': 'Happy',
        'icon': '😊',
        'color': 'success',
        'mood_score': 100
    },
    {
        'name': 'neutral',
        'display_name': 'Neutral',
        'icon': '😐',
        'color': 'secondary',
        'mood_score': 75
    },
    {
        'name': 'annoyed',
        'display_name': 'Annoyed',
        'icon': '😒',
        'color': 'warning',
        'mood_score': 50
    },
    {
        'name': 'angry',
        'display_name': 'Angry',
        'icon': '😠',
        'color': 'danger',
        'mood_score': 25
    },
]


def seed():
    """Insertar o actualizar los moods en la base de datos"""
    print("\n🎭 Poblando CustomerMood...")
    created = 0
    updated = 0

    for mood_data in MOODS:
        existing = CustomerMood.query.filter_by(name=mood_data['name']).first()
        if existing:
            for key, value in mood_data.items():
                setattr(existing, key, value)
            updated += 1
        else:
            mood = CustomerMood(**mood_data)
            db.session.add(mood)
            created += 1

    db.session.commit()
    total = CustomerMood.query.count()
    print(f"   ✅ Creados: {created} | Actualizados: {updated} | Total: {total}")
    return total


def main():
    with app.app_context():
        print("=" * 80)
        print("🌱 SEED: CustomerMood - Estados de ánimo del roleplay")
        print("=" * 80)
        count = seed()
        print(f"\n📊 Total en DB: {count}")
        print("✅ Seed completado")


if __name__ == '__main__':
    main()
