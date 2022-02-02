from flask import render_template
from AppContainer import app
from os import getenv

@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index():
    return render_template('index.html')