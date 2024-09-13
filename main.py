from flask import Flask
from flask_ckeditor import CKEditor
import cloudinary
import cloudinary.uploader
import json
import os

app = Flask(__name__)

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
