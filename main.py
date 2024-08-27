from flask import Flask

app = Flask(__name__)

from Controllers.InicioController import *

if __name__ == '__main__':
   app.run(debug = True)