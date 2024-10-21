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
    if secciones.count == 0:
        return render_template('_EditarCrear.html', idSeccion=0)
    else:
        return render_template('_DetalleEdicion.html', secciones=secciones, idSeccion=0)
    
@app.route("/Editar/<int:idSeccion>")
def EditarCrear(idSeccion):
    if idSeccion == 0:
        seccion_data = None
    else:
        seccion_data = ObtenerSeccion(idSeccion)
    
    return render_template('_EditarCrear.html', idSeccion=idSeccion, seccion_data=seccion_data)

@app.route("/modoVisualizacion")
def Detalle():
    secciones = ObtenerSecciones()
    return render_template('Visualizacion.html', secciones = secciones)

@app.route('/ActualizarSeccion/<int:idSeccion>', methods=['POST'])
def ActualizarSeccion(idSeccion):
    nombre = request.form.get('nombre', '')  
    contenido = request.form.get('contenido', '')  

    if idSeccion == 0:
        AgregarSeccion(nombre, contenido)
    else:
        ModificarSeccion(idSeccion, nombre, contenido)

    secciones = ObtenerSecciones()
    return render_template('_DetalleEdicion.html', secciones=secciones, message="Registro modificado correctamente.")

@app.route('/EliminarSeccion/<section_id>', methods=['DELETE'])
def EliminarSeccion(idSeccion):
    EliminarSeccion(idSeccion)
    secciones = ObtenerSecciones()
    return render_template('_EditarCrear.html', secciones = secciones)

@app.route('/upload', methods=['POST'])
def upload():
    try:
        if 'upload' not in request.files:

            return jsonify({'error': 'No file part'}), 400
        
        file = request.files['upload']
        
        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400
        
        if file:
            # Genera un hash para el nombre del archivo
            hash_filename = hashlib.md5(file.filename.encode()).hexdigest()[:10]
            result = cloudinary.uploader.upload(file, public_id=hash_filename)
            
            return jsonify({
                'url': result['secure_url'],
                'uploaded': 1,
                'fileName': result['original_filename']
            })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500
