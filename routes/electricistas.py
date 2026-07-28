from flask import Blueprint, render_template, request, redirect, url_for

from models import db, Electricista

electricistas_bp = Blueprint("electricistas", __name__)


# ==========================
# LISTAR ELECTRICISTAS
# ==========================
@electricistas_bp.route("/electricistas")
def listar():

    lista = Electricista.query.order_by(Electricista.nombre).all()

    return render_template(
        "electricistas.html",
        electricistas=lista
    )


# ==========================
# NUEVO ELECTRICISTA
# ==========================
@electricistas_bp.route("/electricistas/nuevo", methods=["GET", "POST"])
def nuevo():

    if request.method == "POST":

        electricista = Electricista(
            nombre=request.form["nombre"],
            cuadrilla=request.form["cuadrilla"],
            estado=request.form["estado"]
        )

        db.session.add(electricista)
        db.session.commit()

        return redirect(url_for("electricistas.listar"))

    return render_template("nuevo_electricista.html")


# ==========================
# EDITAR ELECTRICISTA
# ==========================
@electricistas_bp.route("/electricistas/editar/<int:id>", methods=["GET", "POST"])
def editar(id):

    electricista = Electricista.query.get_or_404(id)

    if request.method == "POST":

        electricista.nombre = request.form["nombre"]
        electricista.cuadrilla = request.form["cuadrilla"]
        electricista.estado = request.form["estado"]

        db.session.commit()

        return redirect(url_for("electricistas.listar"))

    return render_template(
        "editar_electricista.html",
        electricista=electricista
    )


# ==========================
# ELIMINAR ELECTRICISTA
# ==========================
@electricistas_bp.route("/electricistas/eliminar/<int:id>")
def eliminar(id):

    electricista = Electricista.query.get_or_404(id)

    db.session.delete(electricista)
    db.session.commit()

    return redirect(url_for("electricistas.listar"))