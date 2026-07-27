from flask import Flask

from config import Config
from models import db

from routes.dashboard import dashboard_bp
from routes.herramientas import herramientas_bp
from routes.electricistas import electricistas_bp
from routes.prestamos import prestamos_bp
from routes.historial import historial_bp

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)

# Registrar Blueprints
app.register_blueprint(dashboard_bp)
app.register_blueprint(herramientas_bp)
app.register_blueprint(electricistas_bp)
app.register_blueprint(prestamos_bp)
app.register_blueprint(historial_bp)

if __name__ == "__main__":

    with app.app_context():
        db.create_all()

    app.run(debug=True)

