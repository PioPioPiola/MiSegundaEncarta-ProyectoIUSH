from main import app
from flask import render_template, request, jsonify, redirect, url_for
import cloudinary.uploader
import hashlib

# Inicializa la estructura global para almacenar secciones
secciones = {}

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
    return render_template('Visualizacion.html')

@app.route('/ActualizarSeccion', methods=['POST'])
def ActualizarSeccion():
    nombreSeccion = request.form.get('nombre-seccion')
    editorContent = request.form.get('editor')
    videos = request.form.get('videos', '').split('\n')  # Asumiendo que los videos están separados por nuevas líneas

    # Guardar los datos en la estructura
    secciones[nombreSeccion] = {
        'content': editorContent,
        'videos': videos
    }

    return redirect(url_for('EditarCrear', nombreSeccion=nombreSeccion, message="Registro modificado correctamente."))

@app.route('/get_secciones')
def get_secciones():
    return jsonify(secciones)

@app.route('/delete_section/<section_id>', methods=['DELETE'])
def delete_section(section_id):
    if section_id in secciones:
        del secciones[section_id]
        return jsonify(success=True)
    return jsonify(success=False)

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
