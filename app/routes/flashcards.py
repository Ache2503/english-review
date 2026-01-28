from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app.extensions import db
from app.models import Flashcard, UserFlashcardReview, Unit
from app.services.streaks import update_user_streak

flashcards_bp = Blueprint('flashcards', __name__, url_prefix='/flashcards')


@flashcards_bp.route('/unit/<int:unit_id>')
@login_required
def unit_flashcards(unit_id):
    unit = Unit.query.get_or_404(unit_id)
    flashcards = Flashcard.query.filter_by(unit_id=unit_id, is_active=True).order_by(Flashcard.order).all()

    total = len(flashcards)
    reviewed = UserFlashcardReview.query.filter_by(user_id=current_user.id).join(Flashcard).filter(
        Flashcard.unit_id == unit_id
    ).count()

    return render_template('flashcards/unit_flashcards.html',
                           unit=unit,
                           flashcards=flashcards,
                           total=total,
                           reviewed=reviewed)


@flashcards_bp.route('/review/<int:flashcard_id>', methods=['POST'])
@login_required
def review_flashcard(flashcard_id):
    flashcard = Flashcard.query.get_or_404(flashcard_id)
    result = request.form.get('result', '').strip().lower()

    is_correct = result == 'known'

    review = UserFlashcardReview(
        user_id=current_user.id,
        flashcard_id=flashcard_id,
        is_correct=is_correct
    )
    db.session.add(review)
    db.session.commit()

    update_user_streak(current_user.id)

    if is_correct:
        flash('¡Bien! Marcaste como conocida.', 'success')
    else:
        flash('Marcada para repaso. ¡Sigue practicando!', 'warning')

    return redirect(url_for('flashcards.unit_flashcards', unit_id=flashcard.unit_id))
