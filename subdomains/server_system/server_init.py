from re import TEMPLATE
from flask import render_template
from AppContainer import app

SUBDOMAIN=""
TEMPLATES=""
STATIC=""


def init(subdomain='server', templates='templates/server_system/', static='static/server_system/'):
    global SUBDOMAIN, TEMPLATES, STATIC
    SUBDOMAIN=subdomain
    TEMPLATES=templates
    STATIC=static
    return True

@app.route('/', subdomain=SUBDOMAIN)
def server_index():
    return render_template(TEMPLATES + 'server_viewpoint.html')