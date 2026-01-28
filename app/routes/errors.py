from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from app.extensions import db
from app.models import ErrorLog

errors_bp = Blueprint('errors', __name__, url_prefix='/errors')


@errors_bp.route('/my-errors')
@login_required
def my_errors():
    logs = ErrorLog.query.filter_by(user_id=current_user.id).order_by(ErrorLog.created_at.desc()).all()
    return render_template('errors/my_errors.html', logs=logs)


@errors_bp.route('/clear')
@login_required
def clear_errors():
    deleted = ErrorLog.query.filter_by(user_id=current_user.id).delete()
    db.session.commit()
    flash(f'Se eliminaron {deleted} errores registrados.', 'success')
    return redirect(url_for('errors.my_errors'))
