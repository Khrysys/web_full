from config import DevelopmentConfig, ProductionConfig

from flask import Flask
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
socketio = SocketIO(app)
sqldb = SQLAlchemy

app.config.from_object(DevelopmentConfig)