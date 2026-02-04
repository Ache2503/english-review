"""
Sistema Avanzado de Repaso (Advanced Review System).

Este módulo implementa:
- Repaso espaciado inteligente (Spaced Repetition)
- Sesiones de repaso personalizadas
- Análisis de debilidades del usuario
- Recomendaciones de estudio
- Estadísticas de progreso
"""

from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple, Any
from dataclasses import dataclass
from enum import Enum
import random
from sqlalchemy import func, and_, or_

from app.extensions import db


class ReviewItemType(Enum):
    """Tipos de elementos para repasar."""
    FLASHCARD = "flashcard"
    VOCABULARY = "vocabulary"
    GRAMMAR = "grammar"
    IDIOM = "idiom"
    PHRASAL_VERB = "phrasal_verb"
    SENTENCE = "sentence"


class Difficulty(Enum):
    """Niveles de dificultad."""
    EASY = 1
    MEDIUM = 2
    HARD = 3


@dataclass
class ReviewItem:
    """Representa un elemento a repasar."""
    item_type: ReviewItemType
    item_id: int
    question: str
    answer: str
    hints: List[str]
    difficulty: Difficulty
    last_reviewed: Optional[datetime]
    times_correct: int
    times_wrong: int
    mastery_level: int  # 0-5
    priority: float  # Mayor = más urgente


@dataclass
class ReviewSession:
    """Representa una sesión de repaso."""
    session_id: str
    user_id: int
    items: List[ReviewItem]
    total_items: int
    current_index: int
    correct_count: int
    wrong_count: int
    started_at: datetime
    focus_areas: List[str]


class AdvancedReviewSystem:
    """Sistema avanzado de repaso con algoritmos inteligentes."""
    
    # Configuración del algoritmo de prioridad
    PRIORITY_WEIGHTS = {
        'overdue_days': 2.0,      # Días de retraso
        'error_rate': 1.5,        # Tasa de errores
        'low_mastery': 1.8,       # Bajo nivel de maestría
        'never_reviewed': 3.0,    # Nunca revisado
        'weakness': 2.5,          # Área débil detectada
    }
    
    # Intervalos de repaso óptimos (días)
    REVIEW_INTERVALS = {
        0: 1,      # Nuevo: revisar mañana
        1: 3,      # Primera revisión exitosa: 3 días
        2: 7,      # Segunda revisión: 1 semana
        3: 14,     # Tercera revisión: 2 semanas
        4: 30,     # Cuarta revisión: 1 mes
        5: 90,     # Dominado: 3 meses
    }
    
    def __init__(self, user_id: int):
        self.user_id = user_id
    
    def generate_session(self, 
                        item_count: int = 20,
                        focus_types: Optional[List[ReviewItemType]] = None,
                        focus_unit: Optional[int] = None,
                        include_new: bool = True) -> ReviewSession:
        """
        Genera una sesión de repaso personalizada.
        
        Args:
            item_count: Número de elementos a incluir
            focus_types: Tipos específicos a incluir
            focus_unit: Unidad específica a repasar
            include_new: Incluir elementos nuevos
            
        Returns:
            ReviewSession con los elementos seleccionados
        """
        all_items = []
        
        # 1. Obtener flashcards pendientes
        if not focus_types or ReviewItemType.FLASHCARD in focus_types:
            flashcard_items = self._get_flashcard_items(focus_unit)
            all_items.extend(flashcard_items)
        
        # 2. Obtener vocabulario pendiente
        if not focus_types or ReviewItemType.VOCABULARY in focus_types:
            vocab_items = self._get_vocabulary_items(focus_unit)
            all_items.extend(vocab_items)
        
        # 3. Obtener idioms pendientes
        if not focus_types or ReviewItemType.IDIOM in focus_types:
            idiom_items = self._get_idiom_items()
            all_items.extend(idiom_items)
        
        # 4. Obtener phrasal verbs pendientes
        if not focus_types or ReviewItemType.PHRASAL_VERB in focus_types:
            pv_items = self._get_phrasal_verb_items()
            all_items.extend(pv_items)
        
        # 5. Obtener reglas gramaticales débiles
        if not focus_types or ReviewItemType.GRAMMAR in focus_types:
            grammar_items = self._get_grammar_items(focus_unit)
            all_items.extend(grammar_items)
        
        # 6. Ordenar por prioridad y seleccionar
        all_items.sort(key=lambda x: x.priority, reverse=True)
        
        # Mezclar un poco para variedad (pero mantener prioridades altas)
        if len(all_items) > item_count:
            # Top 50% por prioridad + 50% aleatorio del resto
            top_items = all_items[:item_count // 2]
            rest_items = all_items[item_count // 2:]
            random.shuffle(rest_items)
            selected = top_items + rest_items[:item_count - len(top_items)]
        else:
            selected = all_items
        
        # Mezclar para evitar monotonía
        random.shuffle(selected)
        
        # Crear sesión
        import uuid
        session = ReviewSession(
            session_id=str(uuid.uuid4())[:8],
            user_id=self.user_id,
            items=selected[:item_count],
            total_items=len(selected[:item_count]),
            current_index=0,
            correct_count=0,
            wrong_count=0,
            started_at=datetime.utcnow(),
            focus_areas=self._identify_focus_areas(selected[:item_count])
        )
        
        return session
    
    def _get_flashcard_items(self, unit_id: Optional[int] = None) -> List[ReviewItem]:
        """Obtiene flashcards para repasar."""
        from app.models import Flashcard, UserFlashcardSRS
        
        items = []
        now = datetime.utcnow()
        
        # Flashcards pendientes de repaso
        query = db.session.query(Flashcard, UserFlashcardSRS).outerjoin(
            UserFlashcardSRS,
            and_(Flashcard.id == UserFlashcardSRS.flashcard_id,
                 UserFlashcardSRS.user_id == self.user_id)
        ).filter(Flashcard.is_active == True)
        
        if unit_id:
            query = query.filter(Flashcard.unit_id == unit_id)
        
        for flashcard, srs in query.limit(50).all():
            # Calcular prioridad
            if srs is None:
                priority = self.PRIORITY_WEIGHTS['never_reviewed']
                last_reviewed = None
                mastery = 0
                times_correct = 0
                times_wrong = 0
            else:
                days_overdue = (now - srs.next_review_date).days if srs.next_review_date < now else 0
                error_rate = srs.total_reviews - srs.correct_reviews if srs.total_reviews > 0 else 0
                
                priority = (
                    days_overdue * self.PRIORITY_WEIGHTS['overdue_days'] +
                    (5 - srs.repetitions) * self.PRIORITY_WEIGHTS['low_mastery'] +
                    error_rate * self.PRIORITY_WEIGHTS['error_rate']
                )
                last_reviewed = srs.last_reviewed_at
                mastery = min(5, srs.repetitions)
                times_correct = srs.correct_reviews
                times_wrong = srs.total_reviews - srs.correct_reviews
            
            item = ReviewItem(
                item_type=ReviewItemType.FLASHCARD,
                item_id=flashcard.id,
                question=flashcard.front,
                answer=flashcard.back,
                hints=[flashcard.example] if flashcard.example else [],
                difficulty=self._get_difficulty(mastery),
                last_reviewed=last_reviewed,
                times_correct=times_correct,
                times_wrong=times_wrong,
                mastery_level=mastery,
                priority=priority
            )
            items.append(item)
        
        return items
    
    def _get_vocabulary_items(self, unit_id: Optional[int] = None) -> List[ReviewItem]:
        """Obtiene vocabulario para repasar."""
        from app.models import VocabularyItem, VocabularyCategory, UserVocabularyProgress
        
        items = []
        
        query = db.session.query(VocabularyItem, UserVocabularyProgress).outerjoin(
            UserVocabularyProgress,
            and_(VocabularyItem.id == UserVocabularyProgress.vocabulary_id,
                 UserVocabularyProgress.user_id == self.user_id)
        )
        
        if unit_id:
            query = query.join(VocabularyCategory).filter(VocabularyCategory.unit_id == unit_id)
        
        for vocab, progress in query.limit(30).all():
            if progress:
                mastery = progress.mastery_level or 0
                priority = (5 - mastery) * self.PRIORITY_WEIGHTS['low_mastery']
                times_correct = progress.times_correct or 0
                times_wrong = (progress.times_reviewed or 0) - times_correct
                last_reviewed = progress.last_reviewed
            else:
                mastery = 0
                priority = self.PRIORITY_WEIGHTS['never_reviewed']
                times_correct = 0
                times_wrong = 0
                last_reviewed = None
            
            item = ReviewItem(
                item_type=ReviewItemType.VOCABULARY,
                item_id=vocab.id,
                question=f"¿Cuál es el significado de '{vocab.word}'?",
                answer=vocab.definition,
                hints=[vocab.example] if vocab.example else [],
                difficulty=self._get_difficulty(mastery),
                last_reviewed=last_reviewed,
                times_correct=times_correct,
                times_wrong=times_wrong,
                mastery_level=mastery,
                priority=priority
            )
            items.append(item)
        
        return items
    
    def _get_idiom_items(self) -> List[ReviewItem]:
        """Obtiene idioms para repasar."""
        from app.models import Idiom, UserIdiomProgress
        
        items = []
        
        query = db.session.query(Idiom, UserIdiomProgress).outerjoin(
            UserIdiomProgress,
            and_(Idiom.id == UserIdiomProgress.idiom_id,
                 UserIdiomProgress.user_id == self.user_id)
        )
        
        for idiom, progress in query.limit(20).all():
            if progress:
                mastery = progress.mastery_level or 0
                priority = (5 - mastery) * self.PRIORITY_WEIGHTS['low_mastery']
                times_correct = progress.correct_count or 0
                times_wrong = progress.incorrect_count or 0
                last_reviewed = progress.last_practiced
            else:
                mastery = 0
                priority = self.PRIORITY_WEIGHTS['never_reviewed']
                times_correct = 0
                times_wrong = 0
                last_reviewed = None
            
            item = ReviewItem(
                item_type=ReviewItemType.IDIOM,
                item_id=idiom.id,
                question=f"¿Qué significa '{idiom.phrase}'?",
                answer=idiom.meaning,
                hints=[idiom.spanish_equivalent] if idiom.spanish_equivalent else [],
                difficulty=self._get_difficulty(mastery),
                last_reviewed=last_reviewed,
                times_correct=times_correct,
                times_wrong=times_wrong,
                mastery_level=mastery,
                priority=priority
            )
            items.append(item)
        
        return items
    
    def _get_phrasal_verb_items(self) -> List[ReviewItem]:
        """Obtiene phrasal verbs para repasar."""
        from app.models import PhrasalVerb, UserPhrasalVerbProgress
        
        items = []
        
        query = db.session.query(PhrasalVerb, UserPhrasalVerbProgress).outerjoin(
            UserPhrasalVerbProgress,
            and_(PhrasalVerb.id == UserPhrasalVerbProgress.phrasal_verb_id,
                 UserPhrasalVerbProgress.user_id == self.user_id)
        )
        
        for pv, progress in query.limit(20).all():
            if progress:
                mastery = progress.mastery_level or 0
                priority = (5 - mastery) * self.PRIORITY_WEIGHTS['low_mastery']
                times_correct = progress.correct_count or 0
                times_wrong = progress.incorrect_count or 0
                last_reviewed = progress.last_practiced
            else:
                mastery = 0
                priority = self.PRIORITY_WEIGHTS['never_reviewed']
                times_correct = 0
                times_wrong = 0
                last_reviewed = None
            
            item = ReviewItem(
                item_type=ReviewItemType.PHRASAL_VERB,
                item_id=pv.id,
                question=f"¿Qué significa '{pv.full_form}'?",
                answer=pv.meaning,
                hints=[pv.spanish_translation] if pv.spanish_translation else [],
                difficulty=self._get_difficulty(mastery),
                last_reviewed=last_reviewed,
                times_correct=times_correct,
                times_wrong=times_wrong,
                mastery_level=mastery,
                priority=priority
            )
            items.append(item)
        
        return items
    
    def _get_grammar_items(self, unit_id: Optional[int] = None) -> List[ReviewItem]:
        """Obtiene ejercicios gramaticales basados en debilidades."""
        from app.models import SentenceExercise, UserSentenceExercise
        
        items = []
        
        # Buscar ejercicios donde el usuario falló o nunca intentó
        subquery = db.session.query(UserSentenceExercise.exercise_id).filter(
            UserSentenceExercise.user_id == self.user_id,
            UserSentenceExercise.is_correct == True
        ).scalar_subquery()
        
        query = SentenceExercise.query.filter(
            ~SentenceExercise.id.in_(subquery),
            SentenceExercise.is_active == True
        )
        
        if unit_id:
            query = query.filter(SentenceExercise.unit_id == unit_id)
        
        for exercise in query.limit(20).all():
            # Buscar intentos previos
            attempts = UserSentenceExercise.query.filter_by(
                user_id=self.user_id,
                exercise_id=exercise.id
            ).all()
            
            times_correct = sum(1 for a in attempts if a.is_correct)
            times_wrong = sum(1 for a in attempts if not a.is_correct)
            
            if times_wrong > times_correct:
                priority = self.PRIORITY_WEIGHTS['weakness']
            elif not attempts:
                priority = self.PRIORITY_WEIGHTS['never_reviewed']
            else:
                priority = 1.0
            
            item = ReviewItem(
                item_type=ReviewItemType.GRAMMAR,
                item_id=exercise.id,
                question=f"{exercise.instruction}\n{exercise.prompt}",
                answer=exercise.correct_answer,
                hints=exercise.alternative_answers or [],
                difficulty=Difficulty.MEDIUM if exercise.difficulty == 'intermediate' else Difficulty.EASY,
                last_reviewed=max([a.submitted_at for a in attempts], default=None) if attempts else None,
                times_correct=times_correct,
                times_wrong=times_wrong,
                mastery_level=min(5, times_correct),
                priority=priority
            )
            items.append(item)
        
        return items
    
    def _get_difficulty(self, mastery: int) -> Difficulty:
        """Determina la dificultad basada en el nivel de maestría."""
        if mastery >= 4:
            return Difficulty.EASY
        elif mastery >= 2:
            return Difficulty.MEDIUM
        return Difficulty.HARD
    
    def _identify_focus_areas(self, items: List[ReviewItem]) -> List[str]:
        """Identifica las áreas de enfoque de la sesión."""
        type_counts = {}
        for item in items:
            type_name = item.item_type.value
            type_counts[type_name] = type_counts.get(type_name, 0) + 1
        
        # Ordenar por cantidad
        sorted_types = sorted(type_counts.items(), key=lambda x: x[1], reverse=True)
        return [t[0] for t in sorted_types[:3]]
    
    def record_review(self, item: ReviewItem, is_correct: bool, 
                     response_time_seconds: Optional[int] = None) -> Dict:
        """
        Registra el resultado de un repaso y actualiza las métricas.
        
        Returns:
            Dict con información del próximo repaso
        """
        from app.models import (UserFlashcardSRS, UserVocabularyProgress, 
                               UserIdiomProgress, UserPhrasalVerbProgress,
                               UserSentenceExercise)
        
        result = {
            'item_id': item.item_id,
            'item_type': item.item_type.value,
            'is_correct': is_correct,
            'new_mastery': item.mastery_level,
            'next_review_days': 1
        }
        
        # Calcular nuevo nivel de maestría
        if is_correct:
            new_mastery = min(5, item.mastery_level + 1)
        else:
            new_mastery = max(0, item.mastery_level - 1)
        
        # Calcular próximo intervalo de repaso
        next_interval = self.REVIEW_INTERVALS.get(new_mastery, 1)
        next_review = datetime.utcnow() + timedelta(days=next_interval)
        
        # Actualizar según el tipo
        if item.item_type == ReviewItemType.FLASHCARD:
            self._update_flashcard_progress(item.item_id, is_correct, new_mastery, next_review)
        elif item.item_type == ReviewItemType.VOCABULARY:
            self._update_vocabulary_progress(item.item_id, is_correct, new_mastery, next_review)
        elif item.item_type == ReviewItemType.IDIOM:
            self._update_idiom_progress(item.item_id, is_correct, new_mastery, next_review)
        elif item.item_type == ReviewItemType.PHRASAL_VERB:
            self._update_pv_progress(item.item_id, is_correct, new_mastery, next_review)
        elif item.item_type == ReviewItemType.GRAMMAR:
            self._update_grammar_progress(item.item_id, is_correct)
        
        result['new_mastery'] = new_mastery
        result['next_review_days'] = next_interval
        result['next_review_date'] = next_review.strftime('%Y-%m-%d')
        
        return result
    
    def _update_flashcard_progress(self, flashcard_id: int, is_correct: bool, 
                                   mastery: int, next_review: datetime):
        """Actualiza progreso de flashcard."""
        from app.models import UserFlashcardSRS
        from app.services.srs import review_flashcard_srs, quality_from_response
        
        quality = quality_from_response(is_correct)
        review_flashcard_srs(self.user_id, flashcard_id, quality)
    
    def _update_vocabulary_progress(self, vocab_id: int, is_correct: bool,
                                   mastery: int, next_review: datetime):
        """Actualiza progreso de vocabulario."""
        from app.models import UserVocabularyProgress
        
        progress = UserVocabularyProgress.query.filter_by(
            user_id=self.user_id,
            vocabulary_id=vocab_id
        ).first()
        
        if not progress:
            progress = UserVocabularyProgress(
                user_id=self.user_id,
                vocabulary_id=vocab_id,
                mastery_level=0,
                correct_count=0,
                incorrect_count=0
            )
            db.session.add(progress)
        
        progress.mastery_level = mastery
        progress.last_practiced = datetime.utcnow()
        if is_correct:
            progress.correct_count = (progress.correct_count or 0) + 1
        else:
            progress.incorrect_count = (progress.incorrect_count or 0) + 1
        
        db.session.commit()
    
    def _update_idiom_progress(self, idiom_id: int, is_correct: bool,
                              mastery: int, next_review: datetime):
        """Actualiza progreso de idiom."""
        from app.models import UserIdiomProgress
        
        progress = UserIdiomProgress.query.filter_by(
            user_id=self.user_id,
            idiom_id=idiom_id
        ).first()
        
        if not progress:
            progress = UserIdiomProgress(
                user_id=self.user_id,
                idiom_id=idiom_id,
                mastery_level=0,
                correct_count=0,
                incorrect_count=0
            )
            db.session.add(progress)
        
        progress.mastery_level = mastery
        progress.last_practiced = datetime.utcnow()
        progress.next_review = next_review
        if is_correct:
            progress.correct_count = (progress.correct_count or 0) + 1
        else:
            progress.incorrect_count = (progress.incorrect_count or 0) + 1
        
        db.session.commit()
    
    def _update_pv_progress(self, pv_id: int, is_correct: bool,
                           mastery: int, next_review: datetime):
        """Actualiza progreso de phrasal verb."""
        from app.models import UserPhrasalVerbProgress
        
        progress = UserPhrasalVerbProgress.query.filter_by(
            user_id=self.user_id,
            phrasal_verb_id=pv_id
        ).first()
        
        if not progress:
            progress = UserPhrasalVerbProgress(
                user_id=self.user_id,
                phrasal_verb_id=pv_id,
                mastery_level=0,
                correct_count=0,
                incorrect_count=0
            )
            db.session.add(progress)
        
        progress.mastery_level = mastery
        progress.last_practiced = datetime.utcnow()
        progress.next_review = next_review
        if is_correct:
            progress.correct_count = (progress.correct_count or 0) + 1
        else:
            progress.incorrect_count = (progress.incorrect_count or 0) + 1
        
        db.session.commit()
    
    def _update_grammar_progress(self, exercise_id: int, is_correct: bool):
        """Registra intento de ejercicio gramatical."""
        from app.models import UserSentenceExercise
        
        submission = UserSentenceExercise(
            user_id=self.user_id,
            exercise_id=exercise_id,
            user_answer="[Review Session]",
            is_correct=is_correct,
            feedback="Revisado en sesión de repaso"
        )
        db.session.add(submission)
        db.session.commit()
    
    def get_statistics(self) -> Dict:
        """
        Obtiene estadísticas completas del sistema de repaso.
        """
        from app.models import (Flashcard, UserFlashcardSRS, VocabularyItem, 
                               UserVocabularyProgress, Idiom, UserIdiomProgress,
                               PhrasalVerb, UserPhrasalVerbProgress)
        
        now = datetime.utcnow()
        
        # Flashcards
        total_flashcards = Flashcard.query.filter_by(is_active=True).count()
        learned_flashcards = UserFlashcardSRS.query.filter(
            UserFlashcardSRS.user_id == self.user_id,
            UserFlashcardSRS.repetitions >= 3
        ).count()
        due_flashcards = UserFlashcardSRS.query.filter(
            UserFlashcardSRS.user_id == self.user_id,
            UserFlashcardSRS.next_review_date <= now
        ).count()
        
        # Vocabulario
        total_vocab = VocabularyItem.query.count()
        learned_vocab = UserVocabularyProgress.query.filter(
            UserVocabularyProgress.user_id == self.user_id,
            UserVocabularyProgress.mastery_level >= 3
        ).count()
        
        # Idioms
        total_idioms = Idiom.query.count()
        learned_idioms = UserIdiomProgress.query.filter(
            UserIdiomProgress.user_id == self.user_id,
            UserIdiomProgress.mastery_level.in_(['learned', 'mastered'])
        ).count()
        
        # Phrasal Verbs
        total_pvs = PhrasalVerb.query.count()
        learned_pvs = UserPhrasalVerbProgress.query.filter(
            UserPhrasalVerbProgress.user_id == self.user_id,
            UserPhrasalVerbProgress.mastery_level.in_(['learned', 'mastered'])
        ).count()
        
        # Calcular items pendientes de repaso hoy
        due_today = due_flashcards  # + otros tipos con next_review
        
        # Proyección de los próximos 7 días
        forecast = []
        for days in range(7):
            target_date = now + timedelta(days=days)
            next_day = target_date + timedelta(days=1)
            
            count = UserFlashcardSRS.query.filter(
                UserFlashcardSRS.user_id == self.user_id,
                UserFlashcardSRS.next_review_date >= target_date,
                UserFlashcardSRS.next_review_date < next_day
            ).count()
            
            forecast.append({
                'date': target_date.strftime('%a'),
                'full_date': target_date.strftime('%Y-%m-%d'),
                'count': count
            })
        
        return {
            'flashcards': {
                'total': total_flashcards,
                'learned': learned_flashcards,
                'due': due_flashcards,
                'progress': round(learned_flashcards / total_flashcards * 100, 1) if total_flashcards else 0
            },
            'vocabulary': {
                'total': total_vocab,
                'learned': learned_vocab,
                'progress': round(learned_vocab / total_vocab * 100, 1) if total_vocab else 0
            },
            'idioms': {
                'total': total_idioms,
                'learned': learned_idioms,
                'progress': round(learned_idioms / total_idioms * 100, 1) if total_idioms else 0
            },
            'phrasal_verbs': {
                'total': total_pvs,
                'learned': learned_pvs,
                'progress': round(learned_pvs / total_pvs * 100, 1) if total_pvs else 0
            },
            'due_today': due_today,
            'forecast': forecast,
            'overall_progress': round(
                (learned_flashcards + learned_vocab + learned_idioms + learned_pvs) /
                max(1, total_flashcards + total_vocab + total_idioms + total_pvs) * 100, 1
            )
        }
    
    def get_weak_areas(self) -> List[Dict]:
        """
        Identifica las áreas débiles del usuario.
        """
        from app.models import UserSentenceExercise, SentenceExercise, ErrorLog
        
        weak_areas = []
        
        # Analizar ejercicios con más errores
        error_counts = db.session.query(
            SentenceExercise.grammar_focus,
            func.count(UserSentenceExercise.id).label('total'),
            func.sum(func.cast(UserSentenceExercise.is_correct == False, db.Integer)).label('errors')
        ).join(
            SentenceExercise,
            UserSentenceExercise.exercise_id == SentenceExercise.id
        ).filter(
            UserSentenceExercise.user_id == self.user_id
        ).group_by(
            SentenceExercise.grammar_focus
        ).all()
        
        for grammar_focus, total, errors in error_counts:
            if total > 0:
                error_rate = (errors or 0) / total
                if error_rate > 0.3:  # Más del 30% de errores
                    weak_areas.append({
                        'area': grammar_focus,
                        'type': 'grammar',
                        'total_attempts': total,
                        'error_rate': round(error_rate * 100, 1),
                        'recommendation': f"Practica más ejercicios de {grammar_focus}"
                    })
        
        # Analizar errores de escritura
        recent_errors = ErrorLog.query.filter(
            ErrorLog.user_id == self.user_id,
            ErrorLog.created_at >= datetime.utcnow() - timedelta(days=30)
        ).all()
        
        error_categories = {}
        for error in recent_errors:
            category = error.rule or 'general'
            error_categories[category] = error_categories.get(category, 0) + 1
        
        for category, count in sorted(error_categories.items(), key=lambda x: x[1], reverse=True)[:5]:
            weak_areas.append({
                'area': category,
                'type': 'writing',
                'error_count': count,
                'recommendation': f"Revisa las reglas de {category}"
            })
        
        return weak_areas
    
    def get_recommendations(self) -> List[Dict]:
        """
        Genera recomendaciones personalizadas de estudio.
        """
        stats = self.get_statistics()
        weak_areas = self.get_weak_areas()
        recommendations = []
        
        # Recomendación por items pendientes
        if stats['due_today'] > 0:
            recommendations.append({
                'priority': 'high',
                'type': 'review',
                'title': f"Tienes {stats['due_today']} items pendientes de repaso",
                'description': "El repaso espaciado es más efectivo si no se acumulan pendientes",
                'action': 'Iniciar sesión de repaso',
                'action_url': '/review/start'
            })
        
        # Recomendación por áreas débiles
        if weak_areas:
            top_weak = weak_areas[0]
            recommendations.append({
                'priority': 'high',
                'type': 'practice',
                'title': f"Área a mejorar: {top_weak['area']}",
                'description': top_weak['recommendation'],
                'action': 'Practicar ahora',
                'action_url': f"/practice/{top_weak['type']}"
            })
        
        # Recomendación por progreso bajo
        if stats['flashcards']['progress'] < 50:
            recommendations.append({
                'priority': 'medium',
                'type': 'flashcards',
                'title': 'Aprende más vocabulario con flashcards',
                'description': f"Has aprendido {stats['flashcards']['learned']} de {stats['flashcards']['total']} flashcards",
                'action': 'Estudiar flashcards',
                'action_url': '/flashcards'
            })
        
        # Recomendación por idioms
        if stats['idioms']['progress'] < 30:
            recommendations.append({
                'priority': 'low',
                'type': 'idioms',
                'title': 'Expande tu conocimiento de expresiones',
                'description': 'Los idioms hacen que tu inglés suene más natural',
                'action': 'Ver idioms',
                'action_url': '/idioms'
            })
        
        return recommendations


def get_review_session(user_id: int, **kwargs) -> ReviewSession:
    """
    Función de conveniencia para obtener una sesión de repaso.
    """
    system = AdvancedReviewSystem(user_id)
    return system.generate_session(**kwargs)


def get_user_review_stats(user_id: int) -> Dict:
    """
    Función de conveniencia para obtener estadísticas de repaso.
    """
    system = AdvancedReviewSystem(user_id)
    return system.get_statistics()


def get_study_recommendations(user_id: int) -> List[Dict]:
    """
    Función de conveniencia para obtener recomendaciones.
    """
    system = AdvancedReviewSystem(user_id)
    return system.get_recommendations()
