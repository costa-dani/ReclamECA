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

         #checar se o nome e senha estao no banco de dados
         return 1

   return render_template("login.html")

@app.route("/signup", methods = ["POST", "GET"])

def cadastro():

   if request.method == 'POST':

      escolha = request.form.get("botao")

      if escolha == "cadastrar":

         #colocar o nome e senha no banco de dados
         return 1
      
      elif escolha == "irlogin":

         return render_template("login.html")

   return render_template("cadastro.html")

app.run()