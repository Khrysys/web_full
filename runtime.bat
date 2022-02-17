@ECHO off

call remove_old.bat

pip install flask flask-socketio flask-sqlalchemy psutil numpy ffmpeg
start "technomancy server" python main.py
