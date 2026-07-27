from flask import Blueprint, render_template, request, redirect, url_for

from models import db, Herramienta

herramientas_bp = Blueprint("herramientas", __name__)


@herramientas_bp.route("/herramientas")
def listar():

    herramientas = Herramienta.query.order_by(Herramienta.nombre).all()

    return render_template(
        "herramientas.html",
        herramientas=herramientas
    )


@herramientas_bp.route("/herramientas/nueva", methods=["GET", "POST"])
def nueva():

    if request.method == "POST":

        nueva_h = Herramienta(

            nombre=request.form["nombre"],

            marca=request.form["marca"],

            modelo=request.form["modelo"],

            observaciones=request.form["observaciones"]

        )

        db.session.add(nueva_h)

        db.session.commit()

        return redirect(url_for("herramientas.listar"))

    return render_template("nueva_herramienta.html")

@herramientas_bp.route("/herramientas/editar/<int:id>", methods=["GET", "POST"])
def editar(id):

    herramienta = Herramienta.query.get_or_404(id)

    if request.method == "POST":

        herramienta.nombre = request.form["nombre"]
        herramienta.marca = request.form["marca"]
        herramienta.modelo = request.form["modelo"]
        herramienta.observaciones = request.form["observaciones"]

        db.session.commit()

        return redirect(url_for("herramientas.listar"))

    return render_template(
        "editar_herramienta.html",
        herramienta=herramienta
    )

@herramientas_bp.route("/herramientas/eliminar/<int:id>")
def eliminar(id):

    herramienta = Herramienta.query.get_or_404(id)

    db.session.delete(herramienta)

    db.session.commit()

    return redirect(url_for("herramientas.listar"))