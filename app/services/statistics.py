"""
Servicio de estadísticas y analíticas para el dashboard.

Proporciona datos agregados para visualizaciones con Chart.js.
"""

from datetime import datetime, timedelta
from typing import Dict, List, Optional
from collections import defaultdict
from sqlalchemy import func, and_
from app.extensions import db


def get_activity_heatmap(user_id: int, days: int = 365) -> List[Dict]:
    """
    Genera datos para un heatmap de actividad estilo GitHub.
    
    Returns:
        Lista de diccionarios con fecha y cantidad de actividades
    """
    from app.models import (
        UserWritingSubmission, UserSentencePractice, 
        UserQuizSubmission, UserFlashcardReview,
        UserReadingSubmission, ConversationPractice
    )
    
    end_date = datetime.utcnow().date()
    start_date = end_date - timedelta(days=days)
    
    # Combinar actividades de todas las fuentes
    activity_counts = defaultdict(int)
    
    # Submissions de escritura
    writing = db.session.query(
        func.date(UserWritingSubmission.submitted_at).label('date'),
        func.count().label('count')
    ).filter(
        UserWritingSubmission.user_id == user_id,
        func.date(UserWritingSubmission.submitted_at) >= start_date
    ).group_by(func.date(UserWritingSubmission.submitted_at)).all()
    
    for date, count in writing:
        activity_counts[str(date)] += count
    
    # Prácticas de oraciones
    sentences = db.session.query(
        func.date(UserSentencePractice.created_at).label('date'),
        func.count().label('count')
    ).filter(
        UserSentencePractice.user_id == user_id,
        func.date(UserSentencePractice.created_at) >= start_date
    ).group_by(func.date(UserSentencePractice.created_at)).all()
    
    for date, count in sentences:
        activity_counts[str(date)] += count
    
    # Quizzes
    quizzes = db.session.query(
        func.date(UserQuizSubmission.submitted_at).label('date'),
        func.count().label('count')
    ).filter(
        UserQuizSubmission.user_id == user_id,
        func.date(UserQuizSubmission.submitted_at) >= start_date
    ).group_by(func.date(UserQuizSubmission.submitted_at)).all()
    
    for date, count in quizzes:
        activity_counts[str(date)] += count * 2  # Quiz vale más
    
    # Flashcards
    flashcards = db.session.query(
        func.date(UserFlashcardReview.reviewed_at).label('date'),
        func.count().label('count')
    ).filter(
        UserFlashcardReview.user_id == user_id,
        func.date(UserFlashcardReview.reviewed_at) >= start_date
    ).group_by(func.date(UserFlashcardReview.reviewed_at)).all()
    
    for date, count in flashcards:
        activity_counts[str(date)] += count
    
    # Lecturas
    readings = db.session.query(
        func.date(UserReadingSubmission.submitted_at).label('date'),
        func.count().label('count')
    ).filter(
        UserReadingSubmission.user_id == user_id,
        func.date(UserReadingSubmission.submitted_at) >= start_date
    ).group_by(func.date(UserReadingSubmission.submitted_at)).all()
    
    for date, count in readings:
        activity_counts[str(date)] += count * 2
    
    # Conversaciones
    convs = db.session.query(
        func.date(ConversationPractice.completed_at).label('date'),
        func.count().label('count')
    ).filter(
        ConversationPractice.user_id == user_id,
        func.date(ConversationPractice.completed_at) >= start_date
    ).group_by(func.date(ConversationPractice.completed_at)).all()
    
    for date, count in convs:
        activity_counts[str(date)] += count * 3
    
    # Construir lista ordenada
    result = []
    current = start_date
    while current <= end_date:
        date_str = str(current)
        result.append({
            'date': date_str,
            'count': activity_counts.get(date_str, 0)
        })
        current += timedelta(days=1)
    
    return result


def get_weekly_progress(user_id: int, weeks: int = 12) -> Dict:
    """
    Obtiene el progreso semanal del usuario.
    
    Returns:
        Diccionario con datos de progreso por semana
    """
    from app.models import (
        UserWritingSubmission, UserQuizSubmission,
        UserFlashcardReview, UserSentencePractice
    )
    
    end_date = datetime.utcnow()
    start_date = end_date - timedelta(weeks=weeks)
    
    weeks_data = []
    
    for week in range(weeks):
        week_start = end_date - timedelta(weeks=weeks-week)
        week_end = week_start + timedelta(days=7)
        
        # Contar actividades por tipo
        writing_count = UserWritingSubmission.query.filter(
            UserWritingSubmission.user_id == user_id,
            UserWritingSubmission.submitted_at >= week_start,
            UserWritingSubmission.submitted_at < week_end
        ).count()
        
        quiz_count = UserQuizSubmission.query.filter(
            UserQuizSubmission.user_id == user_id,
            UserQuizSubmission.submitted_at >= week_start,
            UserQuizSubmission.submitted_at < week_end
        ).count()
        
        flashcard_count = UserFlashcardReview.query.filter(
            UserFlashcardReview.user_id == user_id,
            UserFlashcardReview.reviewed_at >= week_start,
            UserFlashcardReview.reviewed_at < week_end
        ).count()
        
        sentence_count = UserSentencePractice.query.filter(
            UserSentencePractice.user_id == user_id,
            UserSentencePractice.created_at >= week_start,
            UserSentencePractice.created_at < week_end
        ).count()
        
        weeks_data.append({
            'week': week_start.strftime('%d/%m'),
            'writing': writing_count,
            'quizzes': quiz_count,
            'flashcards': flashcard_count,
            'sentences': sentence_count,
            'total': writing_count + quiz_count + flashcard_count + sentence_count
        })
    
    return {
        'weeks': weeks_data,
        'labels': [w['week'] for w in weeks_data]
    }


def get_performance_by_skill(user_id: int) -> Dict:
    """
    Calcula el rendimiento del usuario por habilidad.
    
    Returns:
        Diccionario con puntuaciones por área
    """
    from app.models import (
        UserWritingSubmission, UserQuizSubmission,
        UserFlashcardReview, UserReadingSubmission,
        ConversationPractice, UserSentenceExercise
    )
    
    skills = {}
    
    # Gramática (quizzes + ejercicios de oraciones)
    quiz_scores = db.session.query(func.avg(UserQuizSubmission.score)).filter(
        UserQuizSubmission.user_id == user_id
    ).scalar() or 0
    
    exercise_correct = UserSentenceExercise.query.filter(
        UserSentenceExercise.user_id == user_id,
        UserSentenceExercise.is_correct == True
    ).count()
    exercise_total = UserSentenceExercise.query.filter(
        UserSentenceExercise.user_id == user_id
    ).count()
    exercise_score = (exercise_correct / exercise_total * 100) if exercise_total > 0 else 0
    
    skills['grammar'] = round((quiz_scores + exercise_score) / 2, 1)
    
    # Vocabulario (flashcards)
    flash_correct = UserFlashcardReview.query.filter(
        UserFlashcardReview.user_id == user_id,
        UserFlashcardReview.is_correct == True
    ).count()
    flash_total = UserFlashcardReview.query.filter(
        UserFlashcardReview.user_id == user_id
    ).count()
    skills['vocabulary'] = round((flash_correct / flash_total * 100) if flash_total > 0 else 0, 1)
    
    # Escritura
    writing_avg = db.session.query(func.avg(UserWritingSubmission.score)).filter(
        UserWritingSubmission.user_id == user_id,
        UserWritingSubmission.score.isnot(None)
    ).scalar() or 0
    skills['writing'] = round(writing_avg, 1)
    
    # Lectura
    reading_avg = db.session.query(func.avg(UserReadingSubmission.score)).filter(
        UserReadingSubmission.user_id == user_id,
        UserReadingSubmission.score.isnot(None)
    ).scalar() or 0
    skills['reading'] = round(reading_avg, 1)
    
    # Conversación
    conv_avg = db.session.query(func.avg(ConversationPractice.final_score)).filter(
        ConversationPractice.user_id == user_id
    ).scalar() or 0
    skills['speaking'] = round(conv_avg, 1)
    
    return skills


def get_study_time_distribution(user_id: int, days: int = 30) -> Dict:
    """
    Analiza la distribución del tiempo de estudio por día de la semana.
    
    Returns:
        Diccionario con actividad por día de la semana
    """
    from app.models import (
        UserWritingSubmission, UserQuizSubmission,
        UserFlashcardReview, UserSentencePractice
    )
    
    end_date = datetime.utcnow()
    start_date = end_date - timedelta(days=days)
    
    # Nombres de días en español
    days_names = ['Lun', 'Mar', 'Mié', 'Jue', 'Vie', 'Sáb', 'Dom']
    day_counts = [0] * 7
    
    # Escribir
    for sub in UserWritingSubmission.query.filter(
        UserWritingSubmission.user_id == user_id,
        UserWritingSubmission.submitted_at >= start_date
    ).all():
        day_counts[sub.submitted_at.weekday()] += 1
    
    # Quizzes
    for sub in UserQuizSubmission.query.filter(
        UserQuizSubmission.user_id == user_id,
        UserQuizSubmission.submitted_at >= start_date
    ).all():
        day_counts[sub.submitted_at.weekday()] += 1
    
    # Flashcards
    for sub in UserFlashcardReview.query.filter(
        UserFlashcardReview.user_id == user_id,
        UserFlashcardReview.reviewed_at >= start_date
    ).all():
        day_counts[sub.reviewed_at.weekday()] += 1
    
    # Oraciones
    for sub in UserSentencePractice.query.filter(
        UserSentencePractice.user_id == user_id,
        UserSentencePractice.created_at >= start_date
    ).all():
        day_counts[sub.created_at.weekday()] += 1
    
    return {
        'labels': days_names,
        'data': day_counts
    }


def get_streak_history(user_id: int, days: int = 90) -> List[Dict]:
    """
    Obtiene el historial de rachas del usuario.
    """
    from app.models import UserStreak
    
    streak = UserStreak.query.filter_by(user_id=user_id).first()
    
    if not streak:
        return {
            'current': 0,
            'longest': 0,
            'last_activity': None
        }
    
    return {
        'current': streak.current_streak,
        'longest': streak.longest_streak,
        'last_activity': streak.last_activity_date.strftime('%d/%m/%Y') if streak.last_activity_date else None
    }


def get_unit_progress_breakdown(user_id: int) -> List[Dict]:
    """
    Obtiene el desglose de progreso por unidad.
    """
    from app.models import Unit, UserProgress
    
    units = Unit.query.order_by(Unit.unit_number).all()
    progress_map = {
        up.unit_id: up for up in UserProgress.query.filter_by(user_id=user_id).all()
    }
    
    result = []
    for unit in units:
        progress = progress_map.get(unit.id)
        result.append({
            'unit_number': unit.unit_number,
            'title': unit.title,
            'progress': progress.progress_percentage if progress else 0,
            'completed': progress.completed if progress else False
        })
    
    return result


def get_comprehensive_stats(user_id: int) -> Dict:
    """
    Obtiene todas las estadísticas consolidadas para el dashboard.
    """
    from app.models import (
        UserWritingSubmission, UserQuizSubmission,
        UserFlashcardReview, UserReadingSubmission,
        ConversationPractice, UserSentencePractice,
        UserProgress, Badge
    )
    
    # Conteos totales
    total_writings = UserWritingSubmission.query.filter_by(user_id=user_id).count()
    total_quizzes = UserQuizSubmission.query.filter_by(user_id=user_id).count()
    total_flashcards = UserFlashcardReview.query.filter_by(user_id=user_id).count()
    total_readings = UserReadingSubmission.query.filter_by(user_id=user_id).count()
    total_conversations = ConversationPractice.query.filter_by(user_id=user_id).count()
    total_sentences = UserSentencePractice.query.filter_by(user_id=user_id).count()
    
    # Promedios
    avg_quiz = db.session.query(func.avg(UserQuizSubmission.score)).filter(
        UserQuizSubmission.user_id == user_id
    ).scalar() or 0
    
    avg_writing = db.session.query(func.avg(UserWritingSubmission.score)).filter(
        UserWritingSubmission.user_id == user_id,
        UserWritingSubmission.score.isnot(None)
    ).scalar() or 0
    
    # Actividad reciente (últimos 7 días)
    week_ago = datetime.utcnow() - timedelta(days=7)
    recent_activity = (
        UserWritingSubmission.query.filter(
            UserWritingSubmission.user_id == user_id,
            UserWritingSubmission.submitted_at >= week_ago
        ).count() +
        UserQuizSubmission.query.filter(
            UserQuizSubmission.user_id == user_id,
            UserQuizSubmission.submitted_at >= week_ago
        ).count() +
        UserFlashcardReview.query.filter(
            UserFlashcardReview.user_id == user_id,
            UserFlashcardReview.reviewed_at >= week_ago
        ).count()
    )
    
    return {
        'totals': {
            'writings': total_writings,
            'quizzes': total_quizzes,
            'flashcards': total_flashcards,
            'readings': total_readings,
            'conversations': total_conversations,
            'sentences': total_sentences,
            'total_activities': (total_writings + total_quizzes + total_flashcards + 
                               total_readings + total_conversations + total_sentences)
        },
        'averages': {
            'quiz': round(avg_quiz, 1),
            'writing': round(avg_writing, 1)
        },
        'recent_activity': recent_activity,
        'skills': get_performance_by_skill(user_id),
        'weekly': get_weekly_progress(user_id, weeks=8),
        'study_days': get_study_time_distribution(user_id),
        'streak': get_streak_history(user_id),
        'unit_progress': get_unit_progress_breakdown(user_id)
    }
