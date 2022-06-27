
from flask import Flask,jsonify, request,blueprints #request proporciona los datos enviados atravez de peticiones http (para crear un nuevo objeto en la list)

app = Flask(__name__)   #este es mi servidor

from products import burgas

from blueprint.birras import birras

app.register_blueprint(birras)

@app.route('/burguers')
def getBurgas():
    return jsonify(burgas)



@app.route('/add/burguer',methods=['GET','POST'])
def addBurga():
    new_burga ={
        "nombre": request.json['nombre'],
        "precio": request.json['precio'],
        "url": request.json['url']
    }
    burgas.append(new_burga)
    return jsonify({"message": "Producto agregado satisfactoriamente","producto":burgas})


if __name__ == '__main__':
    app.run(debug=True, port=5000)                  #ejecuta mi servidor en modo debug (se pueden hacer cambios sin volver a abrirlo) en el puerto 5000
