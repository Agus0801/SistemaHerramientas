import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:

    # Obtener la URL de la base de datos desde las variables de entorno
    database_url = os.environ.get("DATABASE_URL")

    # Compatibilidad con Render
    if database_url and database_url.startswith("postgres://"):
        database_url = database_url.replace(
            "postgres://",
            "postgresql://",
            1
        )

    # Si existe DATABASE_URL usa PostgreSQL, si no usa SQLite
    SQLALCHEMY_DATABASE_URI = (
        database_url
        if database_url
        else "sqlite:///" + os.path.join(BASE_DIR, "database", "herramientas.db")
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = "herramientas-2026"