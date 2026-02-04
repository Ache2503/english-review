"""
Servicio de Spaced Repetition System (SRS) basado en el algoritmo SM-2.

El algoritmo SM-2 (SuperMemo 2) calcula intervalos óptimos de repaso
basándose en qué tan bien el usuario recuerda cada tarjeta.

Calificaciones (quality):
- 0: Olvido total - respuesta incorrecta
- 1: Incorrecto pero al ver la respuesta la recordó
- 2: Incorrecto pero cercano
- 3: Correcto con dificultad
- 4: Correcto con algo de duda
- 5: Correcto, respuesta perfecta
"""

from datetime import datetime, timedelta
from typing import Dict, Tuple, Optional
from app.extensions import db


def calculate_next_review(
    quality: int,
    repetitions: int = 0,
    ease_factor: float = 2.5,
    interval: int = 1
) -> Tuple[int, float, int]:
    """
    Calcula el próximo intervalo de repaso usando SM-2.
    
    Args:
        quality: Calificación del 0-5 (qué tan bien recordó)
        repetitions: Número de repeticiones exitosas consecutivas
        ease_factor: Factor de facilidad (2.5 por defecto)
        interval: Intervalo actual en días
    
    Returns:
        Tuple de (nuevo_intervalo, nuevo_ease_factor, nuevas_repeticiones)
    """
    # Mínimo ease_factor es 1.3
    MIN_EASE = 1.3
    
    if quality < 3:
        # Si la calidad es menor a 3, reiniciar repeticiones
        repetitions = 0
        interval = 1
    else:
        # Calcular nuevo intervalo
        if repetitions == 0:
            interval = 1
        elif repetitions == 1:
            interval = 6
        else:
            interval = round(interval * ease_factor)
        
        repetitions += 1
    
    # Calcular nuevo factor de facilidad
    # EF' = EF + (0.1 - (5 - q) * (0.08 + (5 - q) * 0.02))
    ease_factor = ease_factor + (0.1 - (5 - quality) * (0.08 + (5 - quality) * 0.02))
    
    # Asegurar que ease_factor no sea menor a MIN_EASE
    if ease_factor < MIN_EASE:
        ease_factor = MIN_EASE
    
    return interval, ease_factor, repetitions


def get_next_review_date(interval: int) -> datetime:
    """Calcula la fecha del próximo repaso."""
    return datetime.utcnow() + timedelta(days=interval)


def quality_from_response(is_correct: bool, response_time_seconds: Optional[int] = None) -> int:
    """
    Convierte una respuesta simple a una calificación SM-2.
    
    Args:
        is_correct: Si la respuesta fue correcta
        response_time_seconds: Tiempo de respuesta en segundos (opcional)
    
    Returns:
        Calificación del 0-5
    """
    if not is_correct:
        return 1  # Incorrecto pero vio la respuesta
    
    # Si fue correcta, determinar calidad basada en tiempo
    if response_time_seconds is None:
        return 4  # Correcto con algo de duda (por defecto)
    
    if response_time_seconds < 3:
        return 5  # Respuesta perfecta, muy rápida
    elif response_time_seconds < 8:
        return 4  # Correcto con algo de duda
    elif response_time_seconds < 15:
        return 3  # Correcto con dificultad
    else:
        return 3  # Correcto pero tardó mucho


def get_due_flashcards(user_id: int, unit_id: Optional[int] = None, limit: int = 20):
    """
    Obtiene las flashcards pendientes de repaso para un usuario.
    
    Retorna flashcards donde:
    1. next_review_date <= ahora (pendientes de repaso)
    2. Nunca han sido revisadas por el usuario (nuevas)
    
    Args:
        user_id: ID del usuario
        unit_id: ID de la unidad (opcional, para filtrar)
        limit: Máximo de tarjetas a retornar
    
    Returns:
        Lista de flashcards ordenadas por prioridad
    """
    from app.models import Flashcard, UserFlashcardSRS
    
    now = datetime.utcnow()
    
    # Flashcards con SRS que están pendientes
    due_query = db.session.query(Flashcard, UserFlashcardSRS)\
        .join(UserFlashcardSRS, 
              (Flashcard.id == UserFlashcardSRS.flashcard_id) & 
              (UserFlashcardSRS.user_id == user_id))\
        .filter(UserFlashcardSRS.next_review_date <= now)\
        .filter(Flashcard.is_active == True)
    
    if unit_id:
        due_query = due_query.filter(Flashcard.unit_id == unit_id)
    
    due_cards = due_query.order_by(UserFlashcardSRS.next_review_date).all()
    
    # Flashcards nuevas (sin registro SRS para este usuario)
    subquery = db.session.query(UserFlashcardSRS.flashcard_id)\
        .filter(UserFlashcardSRS.user_id == user_id)\
        .scalar_subquery()
    
    new_query = Flashcard.query\
        .filter(~Flashcard.id.in_(subquery))\
        .filter(Flashcard.is_active == True)
    
    if unit_id:
        new_query = new_query.filter(Flashcard.unit_id == unit_id)
    
    new_cards = new_query.order_by(Flashcard.order).all()
    
    # Combinar: primero las pendientes (más urgentes), luego nuevas
    result = []
    
    for flashcard, srs in due_cards:
        result.append({
            'flashcard': flashcard,
            'srs': srs,
            'is_new': False,
            'days_overdue': (now - srs.next_review_date).days
        })
    
    for flashcard in new_cards:
        result.append({
            'flashcard': flashcard,
            'srs': None,
            'is_new': True,
            'days_overdue': 0
        })
    
    return result[:limit]


def get_srs_stats(user_id: int, unit_id: Optional[int] = None) -> Dict:
    """
    Obtiene estadísticas del sistema SRS para un usuario.
    
    Returns:
        Diccionario con estadísticas de repaso
    """
    from app.models import Flashcard, UserFlashcardSRS
    
    now = datetime.utcnow()
    
    # Total de flashcards disponibles
    total_query = Flashcard.query.filter(Flashcard.is_active == True)
    if unit_id:
        total_query = total_query.filter(Flashcard.unit_id == unit_id)
    total_cards = total_query.count()
    
    # Flashcards con progreso SRS
    srs_query = UserFlashcardSRS.query.filter(UserFlashcardSRS.user_id == user_id)
    if unit_id:
        srs_query = srs_query.join(Flashcard).filter(Flashcard.unit_id == unit_id)
    
    srs_records = srs_query.all()
    
    # Calcular estadísticas
    learned = 0  # repetitions >= 3 y ease_factor > 2.0
    learning = 0  # repetitions > 0 y < 3
    new_cards = total_cards - len(srs_records)
    due_today = 0
    
    for srs in srs_records:
        if srs.next_review_date <= now:
            due_today += 1
        
        if srs.repetitions >= 3 and srs.ease_factor >= 2.0:
            learned += 1
        elif srs.repetitions > 0:
            learning += 1
    
    # Proyección de repasos para los próximos 7 días
    forecast = []
    for days in range(7):
        target_date = now + timedelta(days=days)
        next_day = target_date + timedelta(days=1)
        
        count = UserFlashcardSRS.query.filter(
            UserFlashcardSRS.user_id == user_id,
            UserFlashcardSRS.next_review_date >= target_date,
            UserFlashcardSRS.next_review_date < next_day
        ).count()
        
        forecast.append({
            'date': target_date.strftime('%a'),
            'count': count
        })
    
    return {
        'total': total_cards,
        'learned': learned,
        'learning': learning,
        'new': new_cards,
        'due_today': due_today,
        'forecast': forecast,
        'retention_rate': round((learned / total_cards * 100) if total_cards > 0 else 0, 1)
    }


def review_flashcard_srs(user_id: int, flashcard_id: int, quality: int) -> Dict:
    """
    Procesa una revisión de flashcard con SRS.
    
    Args:
        user_id: ID del usuario
        flashcard_id: ID de la flashcard
        quality: Calificación del 0-5
    
    Returns:
        Diccionario con la información actualizada del SRS
    """
    from app.models import UserFlashcardSRS, UserFlashcardReview
    
    # Buscar o crear registro SRS
    srs = UserFlashcardSRS.query.filter_by(
        user_id=user_id,
        flashcard_id=flashcard_id
    ).first()
    
    if srs is None:
        # Primera revisión
        srs = UserFlashcardSRS(
            user_id=user_id,
            flashcard_id=flashcard_id,
            ease_factor=2.5,
            interval=1,
            repetitions=0
        )
        db.session.add(srs)
    
    # Calcular nuevo intervalo
    new_interval, new_ease, new_reps = calculate_next_review(
        quality=quality,
        repetitions=srs.repetitions,
        ease_factor=srs.ease_factor,
        interval=srs.interval
    )
    
    # Actualizar SRS
    srs.interval = new_interval
    srs.ease_factor = new_ease
    srs.repetitions = new_reps
    srs.next_review_date = get_next_review_date(new_interval)
    srs.last_reviewed_at = datetime.utcnow()
    srs.total_reviews += 1
    
    if quality >= 3:
        srs.correct_reviews += 1
    
    # Crear registro de revisión (para historial)
    review = UserFlashcardReview(
        user_id=user_id,
        flashcard_id=flashcard_id,
        is_correct=(quality >= 3)
    )
    db.session.add(review)
    
    db.session.commit()
    
    return {
        'next_review_date': srs.next_review_date,
        'interval': new_interval,
        'ease_factor': round(new_ease, 2),
        'repetitions': new_reps,
        'is_correct': quality >= 3
    }
