from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = "wsedfAIUBOLKyfskyeasefo87324twregqia"
socketio = SocketIO(app)

@app.route('/')
def index():
    return "rendering index"

if __name__ == '__main__':
    website_url = 'khrysaoros.dev'
    app.config['SERVER_NAME'] = website_url
    app.config['DEBUG'] = False
    socketio.run(app)