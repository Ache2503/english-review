from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app.extensions import db
from app.models import Quiz, QuizQuestion, QuizOption, UserQuizSubmission, Unit
from app.services.streaks import update_user_streak

quiz_bp = Blueprint('quiz', __name__, url_prefix='/quiz')

@quiz_bp.route('/unit/<int:unit_id>')
@login_required
def list_quizzes(unit_id):
    unit = Unit.query.get_or_404(unit_id)
    quizzes = Quiz.query.filter_by(unit_id=unit_id).all()
    return render_template('quizz/quiz_list.html', unit=unit, quizzes=quizzes)

@quiz_bp.route('/take/<int:quiz_id>', methods=['GET', 'POST'])
@login_required
def take_quiz(quiz_id):
    quiz = Quiz.query.get_or_404(quiz_id)
    questions = QuizQuestion.query.filter_by(quiz_id=quiz_id).order_by(QuizQuestion.order).all()

    if request.method == 'POST':
        # Grade the quiz
        total = len(questions)
        correct = 0
        for q in questions:
            selected = request.form.get(f'q_{q.id}')
            if selected:
                opt = QuizOption.query.get(int(selected))
                if opt and opt.is_correct:
                    correct += 1
        score = (correct / total * 100) if total else 0

        submission = UserQuizSubmission(user_id=current_user.id, quiz_id=quiz_id, score=score)
        db.session.add(submission)
        db.session.commit()
        update_user_streak(current_user.id)

        flash(f'Has completado el quiz con {score:.0f}%.', 'success')
        return redirect(url_for('quiz.result', submission_id=submission.id))

    return render_template('quizz/quiz_take.html', quiz=quiz, questions=questions)

@quiz_bp.route('/result/<int:submission_id>')
@login_required
def result(submission_id):
    submission = UserQuizSubmission.query.get_or_404(submission_id)
    # ensure ownership
    if submission.user_id != current_user.id and not current_user.is_admin:
        flash('No tienes permiso para ver este resultado.', 'danger')
        return redirect(url_for('dashboard.index'))
    quiz = Quiz.query.get(submission.quiz_id)
    return render_template('quizz/quiz_result.html', submission=submission, quiz=quiz)
