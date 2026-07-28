from flask import Blueprint, render_template, request, redirect, url_for
from models import db, Herramienta, Electricista, Prestamo
from datetime import datetime
from zoneinfo import ZoneInfo

prestamos_bp = Blueprint("prestamos", __name__)


def ahora_argentina():
    return datetime.now(ZoneInfo("America/Argentina/Buenos_Aires"))


@prestamos_bp.route("/prestamos")
def listar():

    herramientas = Herramienta.query.filter_by(
        estado="Disponible"
    ).order_by(Herramienta.nombre).all()

    electricistas = Electricista.query.filter_by(
        estado="Activo"
    ).order_by(Electricista.nombre).all()

    prestamos = Prestamo.query.filter_by(
        fecha_devolucion=None
    ).all()

    return render_template(
        "prestamos.html",
        herramientas=herramientas,
        electricistas=electricistas,
        prestamos=prestamos
    )


@prestamos_bp.route("/prestamos/nuevo", methods=["POST"])
def nuevo():

    herramienta = Herramienta.query.get_or_404(
        request.form["herramienta"]
    )

    herramienta.estado = "Prestada"

    prestamo = Prestamo(
        herramienta_id=request.form["herramienta"],
        electricista_id=request.form["electricista"],
        fecha_prestamo=ahora_argentina()
    )

    db.session.add(prestamo)
    db.session.commit()

    return redirect(url_for("prestamos.listar"))


@prestamos_bp.route("/prestamos/devolver/<int:id>")
def devolver(id):

    prestamo = Prestamo.query.get_or_404(id)

    prestamo.fecha_devolucion = ahora_argentina()

    herramienta = Herramienta.query.get_or_404(
        prestamo.herramienta_id
    )

    herramienta.estado = "Disponible"

    db.session.commit()

    return redirect(url_for("prestamos.listar"))