from flask import Blueprint, render_template
from models import Prestamo
from datetime import timedelta

historial_bp = Blueprint("historial", __name__)

@historial_bp.route("/historial")
def historial():

    prestamos = Prestamo.query.order_by(
        Prestamo.fecha_prestamo.desc()
    ).all()

    # Compensación de zona horaria (-3 horas)
    for p in prestamos:
        p.fecha_prestamo = p.fecha_prestamo - timedelta(hours=3)

        if p.fecha_devolucion:
            p.fecha_devolucion = p.fecha_devolucion - timedelta(hours=3)

    return render_template(
        "historial.html",
        prestamos=prestamos
    )