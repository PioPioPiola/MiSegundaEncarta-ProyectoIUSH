from flask import Flask
from flask_ckeditor import CKEditor
from flask import Flask
from Models.database import close_connection
from Models.ServicioBd import crearTablaBd
import cloudinary
import cloudinary.uploader

app = Flask(__name__)

#Se crea la tabla que almacenará la información en Bd
with app.app_context():
    crearTablaBd()

# Cerrar conexión a db
def close_db_connection(exception):
    close_connection(exception)

# Configuración para Cloudinary
cloudinary.config(
  cloud_name="db840ls20",
  api_key="759334777182378",
  api_secret="4HBuNNhkOVx8BgQ5F9aE7cVZz78"
)

# Configuración para CKEditor
ckeditor = CKEditor(app)

from Controllers.InicioController import *

if __name__ == '__main__':
    app.run(debug=True)
