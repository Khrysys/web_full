from os import getenv

from flask import Flask
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy

from config import DevelopmentConfig, ProductionConfig

app = Flask(__name__)
socketio = SocketIO(app)
sqldb = SQLAlchemy

app.config.from_object(DevelopmentConfig)
#app.config.from_object(ProductionConfig)

def runFlask():
    socketio.run(app, host=getenv("HOST", "0.0.0.0"), port=int(getenv("PORT", 5000)))
