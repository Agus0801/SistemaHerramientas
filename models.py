from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from zoneinfo import ZoneInfo

def ahora_argentina():
    return datetime.now(ZoneInfo("America/Argentina/Buenos_Aires"))
db = SQLAlchemy()

class Herramienta(db.Model):

    __tablename__ = "herramientas"

    id = db.Column(db.Integer, primary_key=True)

    nombre = db.Column(
        db.String(100),
        nullable=False
    )

    marca = db.Column(
        db.String(100),
        nullable=False
    )

    modelo = db.Column(
        db.String(100)
    )

    estado = db.Column(
        db.String(30),
        default="Disponible",
        nullable=False
    )

    observaciones = db.Column(
        db.Text
    )


class Electricista(db.Model):

    __tablename__ = "electricistas"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    nombre = db.Column(
        db.String(100),
        nullable=False
    )

    cuadrilla = db.Column(
        db.String(20),
        nullable=False
    )

    estado = db.Column(
        db.String(20),
        default="Activo",
        nullable=False
    )


class Prestamo(db.Model):

    __tablename__ = "prestamos"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    herramienta_id = db.Column(
        db.Integer,
        db.ForeignKey("herramientas.id"),
        nullable=False
    )

    electricista_id = db.Column(
        db.Integer,
        db.ForeignKey("electricistas.id"),
        nullable=False
    )

    fecha_prestamo = db.Column(
        db.DateTime(timezone=True),
        default=ahora_argentina,
        nullable=False
    )

    fecha_devolucion = db.Column(
        db.DateTime(timezone=True),
        nullable=True
    )

    herramienta = db.relationship(
        "Herramienta",
        backref="prestamos"
    )

    electricista = db.relationship(
        "Electricista",
        backref="prestamos"
    )