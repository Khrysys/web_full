import os 
from flask import Flask, render_template
from datetime import datetime
from flask_moment import Moment

app = Flask(__name__) 

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == '__main__':
    host = os.getenv('IP', '0.0.0.0')
    port = int(os.getenv('PORT', 5000))
    app.debug = True 
    app.run (host=host, port=port)
    print()

@app.route('/About/')
def index():
    return render_template("/About/index.html")

@app.route('/About/Bio/')
def index():
    return render_template("/About/Bio.html")