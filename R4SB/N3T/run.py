import os, logging
from flask import Flask, render_template, Markup, request

app = Flask(__name__)
app.config.from_pyfile('settings.py')
cache = {}
logger = logging.getLogger(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/robots')
def automated():
    return render_template('awx.html')

    
if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
app.run(debug=True,host='0.0.0.0', port=port)

