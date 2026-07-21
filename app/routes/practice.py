from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user
from app.extensions import db
from app.models import (WritingPractice, UserWritingSubmission, Unit, UserSentencePractice, 
                        UnitExtra, GrammarRule, SentenceExercise, UserSentenceExercise, ErrorLog)

practice_bp = Blueprint('practice', __name__, url_prefix='/practice')

@practice_bp.route('/writing/<int:practice_id>', methods=['GET', 'POST'])
@login_required
def writing_practice(practice_id):
    """Ejercicio de escritura interactivo"""
    practice = WritingPractice.query.get_or_404(practice_id)
    
    if request.method == 'POST':
        text = request.form.get('text', '').strip()
        
        if not text:
            flash('Por favor escribe algo antes de enviar.', 'warning')
        else:
            submission = UserWritingSubmission(
                user_id=current_user.id,
                practice_id=practice_id,
                text=text
            )
            db.session.add(submission)
            db.session.flush()

            # Generar feedback automático basado en la unidad
            try:
                from app.services.feedback import analyze_text, check_grammar_errors
                from app.services.streaks import update_user_streak
                grammar_titles = [gr.topic for gr in GrammarRule.query.filter_by(unit_id=practice.unit_id).order_by(GrammarRule.order).all()]
                feedback_result = analyze_text(text, practice.unit.unit_number, grammar_titles)
                submission.feedback = "\n".join(feedback_result.get('messages', []))
                submission.score = feedback_result.get('score', None)
                update_user_streak(current_user.id)
                grammar_check = check_grammar_errors(text)
                if grammar_check.get('available') and grammar_check.get('error_count', 0) > 0:
                    for err in grammar_check.get('errors', [])[:5]:
                        db.session.add(ErrorLog(
                            user_id=current_user.id,
                            unit_id=practice.unit_id,
                            source='writing',
                            message=err.get('message', 'Error gramatical'),
                            context=err.get('context'),
                            rule=err.get('rule')
                        ))
            except Exception:
                # No bloquear en caso de error del analizador
                submission.feedback = submission.feedback or ''

            db.session.commit()

            flash('¡Tu ejercicio ha sido guardado con feedback!', 'success')
            return redirect(url_for('practice.view_submission', submission_id=submission.id))
    
    # Obtener envío anterior si existe
    previous_submission = UserWritingSubmission.query.filter_by(
        user_id=current_user.id,
        practice_id=practice_id
    ).order_by(UserWritingSubmission.submitted_at.desc()).first()
    
    return render_template('writing/writing_exercise.html',
                           practice=practice,
                           previous_submission=previous_submission)


@practice_bp.route('/submission/<int:submission_id>')
@login_required
def view_submission(submission_id):
    """Ver envío guardado"""
    submission = UserWritingSubmission.query.get_or_404(submission_id)
    
    # Verificar que el usuario sea el dueño del envío
    if submission.user_id != current_user.id and not current_user.is_admin:
        flash('No tienes permiso para ver este envío.', 'danger')
        return redirect(url_for('dashboard.index'))
    
    return render_template('submission_view.html', submission=submission)


@practice_bp.route('/sentence/<int:unit_id>', methods=['GET', 'POST'])
@login_required
def sentence_practice(unit_id):
    unit = Unit.query.get_or_404(unit_id)

    if request.method == 'POST':
        sentence = request.form.get('sentence', '').strip()

        if not sentence:
            flash('Escribe una oración antes de guardar.', 'warning')
        else:
            sp = UserSentencePractice(
                user_id=current_user.id,
                unit_id=unit_id,
                sentence=sentence
            )
            db.session.add(sp)
            db.session.flush()

            try:
                from app.services.feedback import analyze_text, check_grammar_errors
                from app.services.streaks import update_user_streak
                grammar_titles = [gr.topic for gr in GrammarRule.query.filter_by(unit_id=unit_id).order_by(GrammarRule.order).all()]
                result = analyze_text(sentence, unit.unit_number, grammar_titles)
                sp.feedback = "\n".join(result.get('messages', []))
                sp.score = result.get('score')
                update_user_streak(current_user.id)
                grammar_check = check_grammar_errors(sentence)
                if grammar_check.get('available') and grammar_check.get('error_count', 0) > 0:
                    for err in grammar_check.get('errors', [])[:3]:
                        db.session.add(ErrorLog(
                            user_id=current_user.id,
                            unit_id=unit_id,
                            source='sentence',
                            message=err.get('message', 'Error gramatical'),
                            context=err.get('context'),
                            rule=err.get('rule')
                        ))
            except Exception:
                pass

            db.session.commit()
            flash('Oración guardada con feedback.', 'success')
            return redirect(url_for('practice.sentence_practice', unit_id=unit_id))

    submissions = UserSentencePractice.query.filter_by(
        user_id=current_user.id,
        unit_id=unit_id
    ).order_by(UserSentencePractice.created_at.desc()).all()

    extra = UnitExtra.query.filter_by(unit_id=unit_id).first()
    activities = extra.data if extra and extra.data else {}

    return render_template('sentences/sentence_practice.html', unit=unit, submissions=submissions, activities=activities)


@practice_bp.route('/sentence-exercises/<int:unit_id>')
@login_required
def sentence_exercises(unit_id):
    """Ejercicios estructurados de oraciones por unidad"""
    unit = Unit.query.get_or_404(unit_id)
    
    # Obtener ejercicios de la unidad agrupados por gramática
    exercises = SentenceExercise.query.filter_by(
        unit_id=unit_id,
        is_active=True
    ).order_by(SentenceExercise.order).all()
    
    # Obtener reglas gramaticales de la unidad
    grammar_rules = GrammarRule.query.filter_by(unit_id=unit_id).order_by(GrammarRule.order).all()
    
    # Agrupar ejercicios por gramática
    exercises_by_grammar = {}
    for exercise in exercises:
        grammar = exercise.grammar_focus or "General"
        if grammar not in exercises_by_grammar:
            exercises_by_grammar[grammar] = []
        exercises_by_grammar[grammar].append(exercise)
    
    # Obtener respuestas previas del usuario
    user_submissions = UserSentenceExercise.query.filter_by(
        user_id=current_user.id
    ).join(SentenceExercise).filter(
        SentenceExercise.unit_id == unit_id
    ).all()
    
    # Crear diccionario de respuestas previas
    previous_answers = {sub.exercise_id: sub for sub in user_submissions}
    
    return render_template('sentences/sentence_exercises.html',
                           unit=unit,
                           exercises_by_grammar=exercises_by_grammar,
                           grammar_rules=grammar_rules,
                           previous_answers=previous_answers,
                           total_exercises=len(exercises))


@practice_bp.route('/submit-exercise/<int:exercise_id>', methods=['POST'])
@login_required
def submit_exercise(exercise_id):
    """Enviar respuesta de ejercicio con verificación mejorada"""
    exercise = SentenceExercise.query.get_or_404(exercise_id)
    user_answer = request.form.get('answer', '').strip()
    
    if not user_answer:
        flash('Por favor escribe una respuesta.', 'warning')
        return redirect(url_for('practice.sentence_exercises', unit_id=exercise.unit_id))
    
    # Obtener todas las respuestas correctas (principal + alternativas)
    correct_answers = exercise.get_all_correct_answers()
    
    # Usar el nuevo sistema de verificación con similitud
    from app.services.feedback import check_answer_similarity, check_grammar_errors
    from app.services.streaks import update_user_streak
    
    is_correct, matched_answer, similarity = check_answer_similarity(user_answer, correct_answers, threshold=0.85)
    
    # Verificar errores gramaticales
    grammar_check = check_grammar_errors(user_answer)
    
    # Generar feedback detallado
    feedback_parts = []
    
    if is_correct:
        if similarity == 1.0:
            feedback_parts.append("✅ ¡Perfecto! Respuesta exacta.")
        else:
            feedback_parts.append(f"✅ ¡Correcto! Tu respuesta es válida (similitud: {int(similarity * 100)}%).")
        
        # Mostrar respuesta esperada si no fue exacta
        if similarity < 1.0:
            feedback_parts.append(f"💡 Respuesta esperada: '{matched_answer}'")
    else:
        feedback_parts.append(f"❌ Incorrecto (similitud: {int(similarity * 100)}%).")
        feedback_parts.append(f"✏️ La respuesta correcta es: '{exercise.correct_answer}'")
        
        # Mostrar alternativas si existen
        if exercise.alternative_answers:
            alt_text = "', '".join(exercise.alternative_answers)
            feedback_parts.append(f"📝 También se aceptan: '{alt_text}'")
    
    # Agregar análisis gramatical si hay errores
    if grammar_check["available"] and grammar_check["error_count"] > 0:
        feedback_parts.append(f"\n⚠️ Errores gramaticales detectados ({grammar_check['error_count']}):")
        for error in grammar_check["errors"][:3]:  # Mostrar hasta 3 errores
            error_msg = error["message"]
            replacements = error.get("replacements", [])
            if replacements:
                feedback_parts.append(f"  • {error_msg} → Intenta: '{replacements[0]}'")
            else:
                feedback_parts.append(f"  • {error_msg}")
            db.session.add(ErrorLog(
                user_id=current_user.id,
                unit_id=exercise.unit_id,
                source='exercise',
                message=error_msg,
                context=error.get('context'),
                rule=error.get('rule')
            ))
    elif grammar_check["available"] and is_correct:
        feedback_parts.append("\n✨ Sin errores gramaticales detectados.")

    update_user_streak(current_user.id)
    
    feedback = "\n".join(feedback_parts)
    
    # Guardar respuesta
    submission = UserSentenceExercise(
        user_id=current_user.id,
        exercise_id=exercise_id,
        user_answer=user_answer,
        is_correct=is_correct,
        feedback=feedback
    )
    db.session.add(submission)
    db.session.commit()
    
    if is_correct:
        flash('¡Respuesta correcta! 🎉', 'success')
    else:
        flash('Respuesta incorrecta. Revisa el feedback.', 'warning')
    
    return redirect(url_for('practice.sentence_exercises', unit_id=exercise.unit_id))


@practice_bp.route('/api/analyze', methods=['POST'])
@login_required
def api_analyze():
    data = request.get_json(silent=True) or {}
    text = (data.get('text') or '').strip()
    unit_number = int(data.get('unit_number') or 0)

    if not text or not unit_number:
        return jsonify({
            'ok': False,
            'error': 'Texto o unidad inválidos.'
        }), 400

    from app.services.feedback import analyze_text
    unit = Unit.query.filter_by(unit_number=unit_number).first()
    grammar_titles = []
    if unit:
        grammar_titles = [gr.topic for gr in GrammarRule.query.filter_by(unit_id=unit.id).order_by(GrammarRule.order).all()]
    result = analyze_text(text, unit_number, grammar_titles)

    metrics = {
        'word_count': len(text.split()),
        'char_count': len(text)
    }

    return jsonify({
        'ok': True,
        'messages': result.get('messages', []),
        'score': result.get('score', 0),
        'metrics': metrics
    })


@practice_bp.route('/api/submit-exercise/<int:exercise_id>', methods=['POST'])
@login_required
def api_submit_exercise(exercise_id):
    """API para enviar respuesta de ejercicio sin recargar página"""
    exercise = SentenceExercise.query.get_or_404(exercise_id)
    data = request.get_json(silent=True) or {}
    user_answer = (data.get('answer') or '').strip()
    
    if not user_answer:
        return jsonify({'ok': False, 'error': 'Por favor escribe una respuesta.'}), 400
    
    # Obtener todas las respuestas correctas (principal + alternativas)
    correct_answers = exercise.get_all_correct_answers()
    
    # Usar el sistema de verificación con similitud
    from app.services.feedback import check_answer_similarity, check_grammar_errors
    from app.services.streaks import update_user_streak
    
    is_correct, matched_answer, similarity = check_answer_similarity(user_answer, correct_answers, threshold=0.85)
    
    # Verificar errores gramaticales
    grammar_check = check_grammar_errors(user_answer)
    
    # Generar feedback detallado
    feedback_parts = []
    
    if is_correct:
        if similarity == 1.0:
            feedback_parts.append("✅ ¡Perfecto! Respuesta exacta.")
        else:
            feedback_parts.append(f"✅ ¡Correcto! Tu respuesta es válida (similitud: {int(similarity * 100)}%).")
        
        if similarity < 1.0:
            feedback_parts.append(f"💡 Respuesta esperada: '{matched_answer}'")
    else:
        feedback_parts.append(f"❌ Incorrecto (similitud: {int(similarity * 100)}%).")
        feedback_parts.append(f"✏️ La respuesta correcta es: '{exercise.correct_answer}'")
        
        if exercise.alternative_answers:
            alt_text = "', '".join(exercise.alternative_answers)
            feedback_parts.append(f"📝 También se aceptan: '{alt_text}'")
    
    # Agregar análisis gramatical si hay errores
    if grammar_check["available"] and grammar_check["error_count"] > 0:
        feedback_parts.append(f"\n⚠️ Errores gramaticales detectados ({grammar_check['error_count']}):")
        for error in grammar_check["errors"][:3]:
            error_msg = error["message"]
            replacements = error.get("replacements", [])
            if replacements:
                feedback_parts.append(f"  • {error_msg} → Intenta: '{replacements[0]}'")
            else:
                feedback_parts.append(f"  • {error_msg}")
            db.session.add(ErrorLog(
                user_id=current_user.id,
                unit_id=exercise.unit_id,
                source='exercise',
                message=error_msg,
                context=error.get('context'),
                rule=error.get('rule')
            ))
    elif grammar_check["available"] and is_correct:
        feedback_parts.append("\n✨ Sin errores gramaticales detectados.")

    update_user_streak(current_user.id)
    
    feedback = "\n".join(feedback_parts)
    
    # Guardar respuesta
    submission = UserSentenceExercise(
        user_id=current_user.id,
        exercise_id=exercise_id,
        user_answer=user_answer,
        is_correct=is_correct,
        feedback=feedback
    )
    db.session.add(submission)
    db.session.commit()
    
    return jsonify({
        'ok': True,
        'is_correct': is_correct,
        'feedback': feedback,
        'similarity': int(similarity * 100)
    })
