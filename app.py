from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html", title="Hello")

@app.route("/hello")
def hello_world2():
    return 'Hello,World!'

@app.route("/name")
def hello_world1():
    return 'Bhavika!'

@app.route("/age")
def hello_world3():
    return '19...soon 20'