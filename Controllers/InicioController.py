from main import app
from flask import render_template

@app.route("/inicio")
def Index():
    return render_template('Index.html')

@app.route("/modoEdicion")
def EditarCrear():
    return render_template('_EditarCrear.html')

@app.route("/modoVisualizacion")
def Detalle():
    return render_template('_Detalle.html')