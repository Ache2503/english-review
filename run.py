from app import create_app, db
import os

app = create_app(os.environ.get('FLASK_ENV', 'development'))

@app.shell_context_processor
def make_shell_context():
    """Contexto de shell interactivo"""
    return {'db': db}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
