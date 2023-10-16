import pymongo

def init_client():
    client = pymongo.MongoClient("localhost", 27017)
    return client

class User:
    def __init__(self, nome, dre, email, password):
        self.nome = nome                                                                                
        self.email = email
        self.password = password
        self.dre = dre
                                                                                                
    def cadastrar(self):
        c = init_client()
        db = c["databases"]
        usuarios = db["usuarios"]
        u = {"nome" :  self.nome, "dre" : self.dre, "email" : self.email, "password": self.password}
        usuarios.insert_one(u)
        c.close()
    
    def autenticar(self):
        c = init_client()
        db = c["databases"]
        usuarios = db['usuarios']
        data = {'dre' : self.dre}
        es = usuarios.find_one(data)
        if es != None:
            if es['password'] == self.password:
                c.close()
                return True
            
        c.close()
        return False


class Post:
    def _init_(self, local, corpo, img=0):
        self.local = local
        self.corpo = corpo
        self.img = img

    def cadastrar(self):
        c = init_client()
        db= c["databases"]
        post = db["post"]
        p = {"local" : self.local, "corpo" : self.corpo, "img" : self.img}
        post.insert_one(p)
        c.close()

#c = init_client()
#db = c["databases"]
#usuarios = db["usuarios"]
#data = {"dre" : "1234"}
#p = usuarios.find_one(data)
#print(p)
#print(p['password'])