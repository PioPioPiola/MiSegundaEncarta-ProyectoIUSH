from main import app
from flask import render_template, request, jsonify, redirect, url_for
import cloudinary.uploader
import hashlib
from flask import request, render_template, redirect, url_for
from Models.ServicioBd import AgregarSeccion, ObtenerSecciones, ObtenerSeccion, ModificarSeccion, EliminarSeccion

@app.route("/inicio")
def Index():
    return render_template('Index.html')


@app.route("/modoEdicion")
def DetalleEdicion():

    secciones = ObtenerSecciones()
    return render_template('_DetalleEdicion.html', secciones=secciones, idSeccion=0)


@app.route("/Editar/<int:idSeccion>")
def EditarCrear(idSeccion):
    seccion = None
    if idSeccion != 0:
        seccion = ObtenerSeccion(idSeccion)
    return render_template('_EditarCrear.html', idSeccion=idSeccion, seccion=seccion)


@app.route("/modoVisualizacion")
def Detalle():
    secciones = ObtenerSecciones()
    return render_template('_Detalle.html', secciones=secciones)


@app.route('/ActualizarSeccion/<int:idSeccion>', methods=['POST'])
def ActualizarSeccion(idSeccion):
    nombre = request.form.get('nombre', '')
    contenido = request.form.get('contenido', '')

    if idSeccion == 0:
        AgregarSeccion(nombre, contenido)
    else:
        ModificarSeccion(idSeccion, nombre, contenido)

    secciones = ObtenerSecciones()
    return redirect(url_for('DetalleEdicion')) 


@app.route('/EliminarSeccion/<int:idSeccion>', methods=['POST'])
def EliminarSeccion(idSeccion):
    EliminarSeccion(idSeccion)
    secciones = ObtenerSecciones()
    return redirect(url_for('DetalleEdicion'))
