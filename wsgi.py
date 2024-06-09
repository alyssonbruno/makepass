import os
from flask import Flask, request, render_template
from flask_cors import CORS
from asgiref.wsgi import WsgiToAsgi
import service as s

app = Flask(__name__)
CORS(app, origins=['http://casa:3131', 'http://localhost:5000', 'http://0.0.0.0:5000', 'http://proxy-reverso:3131'])

@app.route("/", methods=["GET"])
def index():
    api_url = os.getenv('API_URL', 'http://localhost:5000/make')
    return render_template('index.html', api_url=api_url)


@app.route("/make", methods=["PUT"])
def make():
    count = int(request.form['count']) if 'count' in request.form else s.DEFAULT_COUNT
    lang = request.form['lang'] if 'lang' in request.form else s.DEFAULT_LANG
    sep = request.form['sep'] if 'sep' in request.form else " "
    return s.make_password(count, lang, sep)

app = WsgiToAsgi(app)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)