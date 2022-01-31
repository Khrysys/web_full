from flask import Flask
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy

__app__ = Flask(__name__)
__socketio__ = SocketIO(__app__)
__sqldb__ = SQLAlchemy

def getApp():
    return __app__

def getSocketIO():
    return __socketio__

def getDB():
    return __sqldb__