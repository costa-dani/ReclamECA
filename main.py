from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

app = Flask (__name__)
app.secret_key = "trabalhinho"

@app.route("/", methods = ["POST", "GET"])

def hello():
   
   if request.method == 'POST':

      escolha = request.form.get("botao")

      if escolha == "signup":

         return render_template("cadastro.html")
       
      elif escolha == "login":

         return render_template("home.html")

   return render_template("login.html")

@app.route("/signup", methods = ["POST", "GET"])

def cadastro():

   if request.method == 'POST':

      escolha2 = request.form.get("botao")

      if escolha2 == "cadastrar":

         #colocar o nome e senha no banco de dados
         return render_template("home.html")
      
      elif escolha2 == "irlogin":

         return render_template("login.html")

   return render_template("cadastro.html")

@app.route("/home", methods = ["POST", "GET"])

def home():

   if request.method == 'POST':

      escolha3 = request.form.get("botao")

      if escolha3 == "home":

         return render_template("home.html")
       
      elif escolha3 == "reclamar":

         return render_template("reclamacao.html")
      
      elif escolha3 == "resolvido":

         return render_template("resolvidas.html")

   return render_template("home.html")

@app.route("/reclamacao", methods = ["POST", "GET"])

def reclamacao():

   if request.method == 'POST':
      
      escolha4 = request.form.get("botao")

      if escolha4 == "reclamou":

         return render_template("sucesso.html")
      
      elif escolha4 == "home":

         return render_template("home.html")

   return render_template("reclamacao.html")

@app.route("/sucesso", methods = ["POST", "GET"])

def sucesso():

   if request.method == 'POST':
      
      escolha5 = request.form.get("botao")

      if escolha5 == "outrarec":

         return render_template("reclamacao.html")
      
      elif escolha5 == "voltarhome":

         return render_template("home.html")

   return render_template("sucesso.html")

app.run()