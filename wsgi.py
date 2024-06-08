from flask import Flask, request
from asgiref.wsgi import WsgiToAsgi
import service as s

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return "It's working!"

@app.route("/make", methods=["PUT"])
def make():
    count = int(request.form['count']) if 'count' in request.form else s.DEFAULT_COUNT
    lang = request.form['lang'] if 'lang' in request.form else s.DEFAULT_LANG
    sep = request.form['sep'] if 'sep' in request.form else " "
    return s.make_password(count, lang, sep)

app = WsgiToAsgi(app)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3131)