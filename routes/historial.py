from flask import Blueprint, render_template
from models import Prestamo

historial_bp = Blueprint("historial", __name__)

@historial_bp.route("/historial")
def historial():

    prestamos = Prestamo.query.order_by(
        Prestamo.fecha_prestamo.desc()
    ).all()

    return render_template(
        "historial.html",
        prestamos=prestamos
    )