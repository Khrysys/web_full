from subdomains import main
from subdomains import server

from os import getenv
from AppContainer import app, socketio, live_emit
from datetime import datetime

if __name__ == '__main__' and main.check_if_live() and server.check_if_live():
    host = getenv('HOST', "0.0.0.0")
    port = int(getenv("PORT", 377440))
    app.run(host=host, port=port)
