from flask import Flask
import os
from sqlalchemy import inspect
from flask_migrate import Migrate

from config import Config
from models import db

from routes.dashboard import dashboard_bp
from routes.herramientas import herramientas_bp
from routes.electricistas import electricistas_bp
from routes.prestamos import prestamos_bp
from routes.historial import historial_bp
from zoneinfo import ZoneInfo

app = Flask(__name__)
app.config.from_object(Config)

# Inicializar base de datos
db.init_app(app)
migrate = Migrate(app, db)

# Registrar Blueprints
app.register_blueprint(dashboard_bp)
app.register_blueprint(herramientas_bp)
app.register_blueprint(electricistas_bp)
app.register_blueprint(prestamos_bp)
app.register_blueprint(historial_bp)

# Crear tablas automáticamente (solo si no existen)
with app.app_context():
    db.create_all()

    inspector = inspect(db.engine)
    print("\n===== TABLAS EN LA BASE =====")
    print(inspector.get_table_names())
    print("=============================\n")

# Mostrar rutas registradas
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

@app.template_filter("argtime")
def argtime(fecha):
    if fecha is None:
        return ""

    return fecha.astimezone(
        ZoneInfo("America/Argentina/Buenos_Aires")
    )