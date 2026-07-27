from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Herramienta(db.Model):

    __tablename__ = "herramientas"

    id = db.Column(db.Integer, primary_key=True)

    nombre = db.Column(db.String(100), nullable=False)

    marca = db.Column(db.String(100), nullable=False)

    modelo = db.Column(db.String(100))

    estado = db.Column(
        db.String(30),
        default="Disponible"
    )

    observaciones = db.Column(db.Text)
class Electricista(db.Model):

    __tablename__ = "electricistas"

    id = db.Column(db.Integer, primary_key=True)

    nombre = db.Column(db.String(100), nullable=False)

    cuadrilla = db.Column(db.String(20), nullable=False)

    estado = db.Column(
        db.String(20),
        default="Activo"
    )

from datetime import datetime


class Prestamo(db.Model):

    __tablename__ = "prestamos"

    id = db.Column(db.Integer, primary_key=True)

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
        db.DateTime,
        default=datetime.utcnow
    )

    fecha_devolucion = db.Column(
        db.DateTime,
        nullable=True
    )

    herramienta = db.relationship("Herramienta")

    electricista = db.relationship("Electricista")