from flask import render_template
from flask_socketio import emit
from AppContainer import app, socketio
from datetime import datetime
from os import getenv


@app.route('/')
@app.route('/viewport')
def viewport():
    return render_template('server/viewport.html')

@socketio.event('ping')
def on_ping(sec):
    sec=int(sec)
    this = int(datetime.now()[6:])
    emit(str(sec + this))

if __name__ == '__main__':
    host = "server" + getenv('HOST', "0.0.0.0")
    port = int(getenv("PORT", 377440))
    app.run(host=host, port=port)
