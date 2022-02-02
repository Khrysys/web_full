from flask import render_template
from flask_socketio import emit
from AppContainer import app, socketio
from datetime import datetime

def check_if_live():
    return True

@app.route('/', subdomain="server")
@app.route('/viewport', subdomain="server")
def viewport():
    return render_template('server/viewport.html')

@socketio.event('ping')
def on_ping(sec):
    sec=int(sec)
    this = int(datetime.now()[6:])
    emit(str(sec + this))