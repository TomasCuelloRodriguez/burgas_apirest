from flask import Blueprint, Flask, blueprints,jsonify,request,redirect,url_for
from products import birras

birras = Blueprint('birras','__name__')

@birras.route('/birras')
def getBirras():
    return jsonify(birras)

@birras.route('/add/birra', methods=['GET','POST'])
def addBirra():
    new_birra ={
        "nombre": request.json['nombre'],
        "precio": request.json['precio'],
        "url": request.json['url']
    } 
    birras.append(new_birra)
    return jsonify({"message": "Producto agregado satisfactoriamente","producto":birras})