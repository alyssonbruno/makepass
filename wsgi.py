import os
from flask import Flask, request, render_template
from flask_cors import CORS
from asgiref.wsgi import WsgiToAsgi
from service import make_password, LangNotFound, DEFAULT_LANG, DEFAULT_COUNT

app = Flask(__name__)
CORS(app, origins=['http://localhost:5000'])


@app.route("/", methods=["GET"])
def index():
    api_url = os.getenv('API_URL', 'http://localhost:5000/make')
    return render_template('index.html', api_url=api_url)


@app.route("/make", methods=["PUT"])
def make():
    count = request.form['count'] if 'count' in request.form else DEFAULT_COUNT
    lang = request.form['lang'] if 'lang' in request.form else DEFAULT_LANG
    sep = request.form['sep'] if 'sep' in request.form else " "
    try:
        return make_password(int(count), lang, sep)
    except LangNotFound:
        return "Lang not found", 404
    except ValueError:
        return "Invalid count", 400


app = WsgiToAsgi(app)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=5000)
