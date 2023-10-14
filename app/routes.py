from app import app
from flask import Flask, render_template, request, redirect


app.secret_key = "trabalhinho"
@app.route("/", methods = ["POST", "GET"])
def hello():
    
    if request.method == 'POST':
        escolha = request.form.get("botao")
        if escolha == "signup":
            return redirect("/signup")
        
        elif escolha == "login":

            #checar se o nome e senha estão no banco de dados
            return redirect("/home")

    return render_template("login.html")

@app.route("/signup", methods = ["POST", "GET"])
def cadastro():

    if request.method == 'POST':

        escolha2 = request.form.get("botao")

        if escolha2 == "cadastrar":

            #colocar o nome e senha no banco de dados
            return redirect("/home")
    
        elif escolha2 == "irlogin":
            #
            return render_template("login.html")

    return render_template("cadastro.html")

@app.route("/home", methods = ["POST", "GET"])
def home():

    if request.method == 'POST':

        escolha3 = request.form.get("botao")

        if escolha3 == "home":

            return redirect("/home")
        
        elif escolha3 == "reclamar":

            return redirect("/reclamacao")
        
        elif escolha3 == "resolvido":

            return render_template("resolvidas.html")

    return render_template("home.html")

@app.route("/reclamacao", methods = ["POST", "GET"])
def reclamacao():

    if request.method == 'POST':
        
        escolha4 = request.form.get("botao")

        if escolha4 == "reclamou":

            return redirect("/sucesso")
        
        elif escolha4 == "home":

            return redirect("/home")
        
        elif escolha4 == "reclamar":

            return redirect("/reclamacao")
        
        elif escolha4 == "resolvido":

            return redirect("/resolvidas")

    return render_template("reclamacao.html")

@app.route("/sucesso", methods = ["POST", "GET"])
def sucesso():

    if request.method == 'POST':
        
        escolha5 = request.form.get("botao")

        if escolha5 == "outrarec":

            return redirect("/reclamacao")
        
        elif escolha5 == "voltarhome":

            return redirect("/home")

    return render_template("sucesso.html")


@app.route("/resolvidas", methods = ["POST", "GET"])
def resolvidas():

    return render_template("resolvidas.html")
