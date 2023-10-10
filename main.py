from flask import Flask, render_template, request
from werkzeug.utils import secure_filename


app = Flask (__name__)
app.secret_key = "trabalhinho"

@app.route("/")

def hello():
    return render_template("home.html")

def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return 'file uploaded successfully'
   return render_template("home.html")

app.run()