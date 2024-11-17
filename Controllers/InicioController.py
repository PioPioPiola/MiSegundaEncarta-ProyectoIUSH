from main import app
from flask import render_template, request, jsonify, redirect, url_for
import cloudinary.uploader
import hashlib
from flask import request, render_template, redirect, url_for, flash
from Models.ServicioBd import AgregarSeccion, ObtenerSecciones, ObtenerSeccion, ModificarSeccion, EliminarSeccionTabla

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
    idSecciones = [] #Uso de la estructura de lista
    for seccion in secciones:
        idSecciones.append(seccion[0])

    secciones_ordenadas = sorted(idSecciones)
    arbol = construir_arbol_recursivo(secciones_ordenadas)

    return render_template('_Detalle.html', arbol=arbol)


@app.route('/ActualizarSeccion/<int:idSeccion>', methods=['POST'])
def ActualizarSeccion(idSeccion):
    nombre = request.form.get('nombre', '')
    contenido = request.form.get('contenido', '')

    if idSeccion == 0:
        AgregarSeccion(nombre, contenido)
        accion = 'creó'
    else:
        ModificarSeccion(idSeccion, nombre, contenido)
        accion = 'modificó'

    flash(f'Se {accion} la sección correctamente.')
    return redirect(url_for('DetalleEdicion')) 


@app.route('/EliminarSeccion/<int:idSeccion>', methods=['POST'])
def EliminarSeccion(idSeccion):
    EliminarSeccionTabla(idSeccion)
    flash('Se eliminó la sección correctamente')
    return redirect(url_for('DetalleEdicion')) 

@app.route('/upload_image', methods=['POST'])
def upload_image():
    file = request.files['upload']
    
    upload_result = cloudinary.uploader.upload(file, resource_type="auto")
    
    url = upload_result.get('secure_url')

    return jsonify({
        "uploaded": 1,
        "fileName": file.filename,
        "url": url
    })

def construir_arbol_recursivo(secciones_ordenadas, posicion=0): #Uso de la estructura de arbol y de algoritmo recursivo
    if posicion >= len(secciones_ordenadas):
        return None 

    idSeccion = secciones_ordenadas[posicion]
    infoSeccion = ObtenerSeccion(idSeccion)

    nodo_actual = {
        "consecutivo": infoSeccion[0],
        "titulo": infoSeccion[1],
        "contenido": infoSeccion[2].replace('"', '\\"'), #se hace el replace porque cuando el contenido tiene imágenes, ckaeditor guarda la información con estos caracteres y en el JSON.parse saca error.
        "hijo": construir_arbol_recursivo(secciones_ordenadas, posicion + 1)
    }

    return nodo_actual