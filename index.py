from flask import Flask, render_template, request

app = Flask(__name__)#建立FLASK　物件


@app.route("/")
def index():
    return render_template("index.html")



