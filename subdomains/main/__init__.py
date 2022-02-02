from flask import render_template
from AppContainer import app

def check_if_live():
    return True

@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index():
    return render_template('index.html')