from flask import Flask
import os
from sqlalchemy import inspect

from config import Config
from models import db, Herramienta, Electricista, Prestamo

from routes.dashboard import dashboard_bp
from routes.herramientas import herramientas_bp
from routes.electricistas import electricistas_bp
from routes.prestamos import prestamos_bp
from routes.historial import historial_bp
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)

# Registrar Blueprints
app.register_blueprint(dashboard_bp)
app.register_blueprint(herramientas_bp)
app.register_blueprint(electricistas_bp)
app.register_blueprint(prestamos_bp)
app.register_blueprint(historial_bp)

print("\n===== RUTAS REGISTRADAS =====")

for regla in app.url_map.iter_rules():
    print(f"{regla.endpoint:35} {regla}")

print("=============================\n")

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        debug=False
    )