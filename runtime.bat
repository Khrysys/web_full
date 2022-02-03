@ECHO off

pip install flask flask-socketio flask-sqlalchemy psutil
start "technomancy server" python main.py