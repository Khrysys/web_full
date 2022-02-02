pip install flask flask-socketio flask-sqlalchemy psutil
start "root" python main/root_domain.py
start "server" python server/server_subdomain.py
start "monitor" python system_monitor.py