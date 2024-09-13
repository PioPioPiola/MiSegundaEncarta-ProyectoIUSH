from main import app
from flask import render_template
from flask import request, jsonify, redirect, url_for
import cloudinary.uploader
import hashlib

#Organizar acciones y encarpetado para que no todo se centre en el inicio controller sino en los controller que correspondan :D
@app.route("/inicio")
def Index():
    return render_template('Index.html')

@app.route("/modoEdicion")
def EditarCrear():
    nombreSeccion = request.args.get('nombreSeccion', '')
    message = request.args.get('message', '')
    return render_template('_EditarCrear.html', nombreSeccion=nombreSeccion, message=message)

@app.route("/modoVisualizacion")
def Detalle():
    return render_template('_Detalle.html')

@app.route('/ActualizarSeccion', methods=['POST'])
def ActualizarSeccion():
    nombreSeccion = request.form.get('nombre-seccion')
    editorContent = request.form.get('editor')

    return redirect(url_for('EditarCrear', nombreSeccion=nombreSeccion, message="Registro modificado correctamente."))

@app.route('/upload', methods=['POST'])
def upload():

    file = request.files['upload']
    hash_filename = hashlib.md5(file.filename.encode()).hexdigest()[:10] #TODo:Cambiar por el método de la clase NM3, para usar hashmaps y generar el hash manual

    result = cloudinary.uploader.upload(file, public_id=hash_filename)

    return jsonify({
        'url': result['secure_url'],
        'uploaded': 1,
        'fileName': result['original_filename']
    })