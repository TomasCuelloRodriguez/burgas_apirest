from utils.db import db

class Birra(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    nombre = db.Column(db.Sting)
    precio = db.Column(db.Sting)
    url = db.Column(db.Sting)

    def __init__(self,nombre,precio,url):
        self.nombre = nombre
        self.precio = precio
        self.url = url
