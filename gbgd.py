from app.models import *

c = init_client()
db = c["databases"]
usuarios = db["post"]
data = {"nome" : "Carlos Antonio"}
p = usuarios.find(data)
for i in p:
    print(i)