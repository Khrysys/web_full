from flask import render_template
from AppContainer import app
from os import getenv

@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    host = getenv('HOST', "0.0.0.0")
    port = int(getenv("PORT", 377440))
    app.run(host=host, port=port)
