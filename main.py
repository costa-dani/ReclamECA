from flask import Flask, render_template, request

app = Flask (__name__)
app.secret_key = "trabalhinho"

@app.route("/")

def hello():
    return render_template("login.html")