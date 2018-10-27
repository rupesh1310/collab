from flask import Flask, request, send_file, render_template, redirect, url_for
from gevent.pywsgi import WSGIServer
import os

app = Flask(__name__, static_url_path="/static")

@app.route("/", methods=['GET'])
def home():
    return render_template("index.html")

@app.route("/", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        user = request.form.get("username")
        passwd = request.form.get("passwd")
        print(user, passwd)
        return "Check logs"
    elif request.method == 'GET':
        return render_template("login.html")


@app.route("/profile", methods=['GET'])
def profile():
    return render_template("profile.html")


@app.route("/rooms", methods=['GET'])
def rooms():
    return render_template("rooms.html")


@app.route("/transact", methods=['POST'])
def transact():
    # validate transaction
    return render_template("profile.html")


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    http_server = WSGIServer(('',port), app)
    http_server.serve_forever()

