from datetime import date
from app.extensions import db
from app.models import UserStreak


def update_user_streak(user_id: int) -> UserStreak:
    """Actualiza la racha del usuario según la fecha actual."""
    today = date.today()

    streak = UserStreak.query.filter_by(user_id=user_id).first()
    if not streak:
        streak = UserStreak(user_id=user_id, current_streak=1, longest_streak=1, last_activity_date=today)
        db.session.add(streak)
        return streak

    # Si ya registró actividad hoy, no cambia
    if streak.last_activity_date == today:
        return streak

    # Si fue ayer, incrementa
    if streak.last_activity_date and (today - streak.last_activity_date).days == 1:
        streak.current_streak += 1
    else:
        streak.current_streak = 1

    if streak.current_streak > streak.longest_streak:
        streak.longest_streak = streak.current_streak

    streak.last_activity_date = today
    db.session.add(streak)
    return streak
