from main import app
from flask import render_template

@app.route("/inicio")
def Index():
    return render_template('Index.html')