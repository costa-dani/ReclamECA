from app import app
from flask import Flask, render_template, request, redirect, flash
from app.models import *



app.secret_key = "trabalhinho"
@app.route("/", methods = ["POST", "GET"])
def hello():
    
    if request.method == 'POST':
        escolha = request.form.get("botao")
        if escolha == "irsignup":

            return redirect("/signup")
        
        elif escolha == "login":
            nome = request.form.get("nome")
            dre = request.form.get("dre")
            password = request.form.get("password")
            email = request.form.get("email")
            use = User(dre=dre, password=password, nome = nome, email=email)
            aut, msg = use.autenticar()
            if aut:
                c = init_client()
                db = c["databases"]
                usuarios = db["usuarios"]
                data = {'dre' : dre}
                global u
                u = usuarios.find_one(data)

                return redirect("/home")
            else:
                flash(msg)
                #enviar mensagem de dados errados
                return redirect("/")

    return render_template("login.html")

@app.route("/signup", methods = ["POST", "GET"])
def cadastro():

    if request.method == 'POST':

        escolha2 = request.form.get("botao")

        if escolha2 == "cadastrar":
            nome = request.form.get("nome")
            dre = request.form.get("dre")
            email = request.form.get("email")
            password = request.form.get("password")

            use = User(nome, dre, email, password)
            use.cadastrar()
           
            return redirect("/")
    
        elif escolha2 == "irlogin":
            
            return redirect("/")

    return render_template("cadastro.html")

@app.route("/home", methods = ["POST", "GET"])
def home():
    l = mostrar()
    if request.method == 'POST':

        escolha3 = request.form.get("botao")

        if escolha3 == "home":

            return redirect("/home")
        
        elif escolha3 == "reclamar":

            return redirect("/reclamacao")
        
        elif escolha3 == "resolvido":

            return redirect("/resolvidas")

    return render_template("home.html", post = l, name = u["nome"])

@app.route("/reclamacao", methods = ["POST", "GET"])
def reclamacao():

    if request.method == 'POST':
        
        escolha4 = request.form.get("botao")

        if escolha4 == "reclamou":
            andar = request.form.get("andar")
            bloco = request.form.get("bloco")
            onde = request.form.get("onde")
            texto = request.form.get("corpo")
            local = f"{onde} do Bloco {bloco} no {andar} andar"
            nome = u['nome']
            p = Post(local = local, corpo = texto, nome = nome)
            p.cadastrar()
            #r  = request.form.get("")
            #if r:
            destino = achar_email(bloco)
            enviar_email(destino = destino, lugar= local, corpo= texto, dre=u["dre"], emaili=u['email'], nome=u['nome'] )
            return redirect("/sucesso")
        
        elif escolha4 == "home":

            return redirect("/home")
        
        elif escolha4 == "reclamar":

            return redirect("/reclamacao")
        
        elif escolha4 == "resolvido":

            return redirect("/resolvidas")

    return render_template("reclamacao.html", name = u["nome"])

@app.route("/sucesso", methods = ["POST", "GET"])
def sucesso():

    if request.method == 'POST':
        
        escolha5 = request.form.get("botao")

        if escolha5 == "outrarec":

            return redirect("/reclamacao")
        
        elif escolha5 == "voltarhome":

            return redirect("/home")

    return render_template("sucesso.html", name = u["nome"])


@app.route("/resolvidas", methods = ["POST", "GET"])
def resolvidas():
    if request.method == 'POST':
        
        escolha4 = request.form.get("botao")
        
        if escolha4 == "home":

            return redirect("/home")
        
        elif escolha4 == "reclamar":

            return redirect("/reclamacao")
        
        elif escolha4 == "resolvido":

            return redirect("/resolvidas")

    return render_template("resolvidas.html", name = u["nome"])
