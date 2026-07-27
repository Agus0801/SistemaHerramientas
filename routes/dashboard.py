from flask import Blueprint, render_template

from models import Herramienta, Electricista, Prestamo

dashboard_bp = Blueprint("dashboard", __name__)


@dashboard_bp.route("/")
def dashboard():

    total_herramientas = Herramienta.query.count()

    disponibles = Herramienta.query.filter_by(
        estado="Disponible"
    ).count()

    prestamos_activos = Prestamo.query.filter_by(
        fecha_devolucion=None
    ).count()

    electricistas_activos = Electricista.query.filter_by(
        estado="Activo"
    ).count()

    electricistas_inactivos = Electricista.query.filter_by(
        estado="Inactivo"
    ).count()

    return render_template(
        "dashboard.html",
        total_herramientas=total_herramientas,
        disponibles=disponibles,
        prestamos_activos=prestamos_activos,
        electricistas_activos=electricistas_activos,
        electricistas_inactivos=electricistas_inactivos
    )