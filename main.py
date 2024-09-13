from flask import Flask
from flask_ckeditor import CKEditor
import cloudinary
import cloudinary.uploader

app = Flask(__name__)

#Info del hosting en la nube para cargar imágenes y videos
cloudinary.config(
  cloud_name = "db840ls20",
  api_key = "759334777182378",
  api_secret = "4HBuNNhkOVx8BgQ5F9aE7cVZz78"
)

# Se agrega CKEditor para editor de texto
ckeditor = CKEditor(app)

from Controllers.InicioController import *

if __name__ == '__main__':
    app.run(debug=True)
