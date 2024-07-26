from flask import Flask, request, send_file, render_template
from datetime import datetime
import socket
from waitress import serve
import logging

app = Flask(__name__, template_folder=".")
logger = logging.getLogger("doms")
logging.basicConfig(filename="example.log", level=logging.INFO)
logging.getLogger('werkzeug').disabled = True

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/map")
def map():
    return render_template('static/html/map.html')

@app.route("/demo")
def demo():
    return render_template('static/html/demo.html', host_name=IPAddr)

@app.route("/founder")
def founder():
    return render_template('static/html/founder.html', host_name=IPAddr)

if __name__ == "__main__":
    print("Starting server!")
    #app.run(host="127.0.0.1", port=8080, debug=True)
    serve(app, host="0.0.0.0", port=80)