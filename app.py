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

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

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

# Crear tablas y mostrar cuáles existen
with app.app_context():
    print(">>> Creando tablas...")
    db.create_all()
    print(">>> Tablas existentes:", inspect(db.engine).get_table_names())

if __name__ == "__main__":
    print("\n=== RUTAS REGISTRADAS ===")

    for regla in app.url_map.iter_rules():
        print(regla)

    print("=========================\n")
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        debug=False
    )