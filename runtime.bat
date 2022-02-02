@ECHO off

pip install flask flask-socketio flask-sqlalchemy psutil
start "root" python main.py
start "server_monitor" python system_monitor.py