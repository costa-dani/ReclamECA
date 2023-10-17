import pymongo
import smtplib
import email.message

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


class Post():
    def __init__(self, local, corpo, nome):
        self.local = local
        self.corpo = corpo
        self.nome = nome

    def cadastrar(self):
        c = init_client()
        db= c["databases"]
        post = db["post"]
        p = {"local" : self.local, "corpo" : self.corpo, "nome" : self.nome}
        post.insert_one(p)
        c.close()
    
def mostrar():
    c = init_client()
    db = c["databases"]
    usuarios = db["post"]
    p = usuarios.find()
    l=[]
    for i in p:
        l.append(i)
    l.reverse()
    return l 

def enviar_email(destino,nome, lugar, corpo, dre,emaili):  
    corpo_email = f"""
    <p>Ola, Boa tarde</p>
    <p>Mensagem direcionada pelo ReclamECA!!</p>
    <hr>
    <p>Problema relatado: </p>
    <p> {corpo} </p>
    <p>Mensagem escrita por: {nome} - {str(dre)} - {emaili}</p>
    """

    msg = email.message.Message()
    msg['Subject'] = f"Problema em {lugar}"
    msg['From'] = destino
    msg['To'] = "p18062004@gmail.com"
    password = 'zuht dypp ojgm sapl' 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')


def achar_email(bloco):
    dict = {
        "A" : "cdsantos.med@gmail.com",
        "B" : "cdsantos.med@gmail.com",
        "C" : "cdsantos.med@gmail.com",
        "D" : "cdsantos.med@gmail.com",
        "E" : "cdsantos.med@gmail.com",
        "F" : "cdsantos.med@gmail.com",
        "G" : "cdsantos.med@gmail.com",
        "H" : "cdsantos.med@gmail.com"
    }

    return dict[bloco]

