"""
    Este codigo es para correr en la raspberry pi con un shield un led y que este prenda y apague
    usando el servicio de apis de postman
"""
import json
from flask import Flask
from flask import request, jsonify
from grovepi import *

app = Flask(__name__)

led1 = 4
pinMode(led1, "OUTPUT")

@app.route("/")
def hello():
    return "Hello World!"


@app.route('/led', methods=['PUT'])
def control_led():


    if request.method == 'PUT':
        data = request.get_json()

        if 'estado' in data:
            digitalWrite(led1, data['estado'])
            return jsonify({'message': 'Estado del LED actualizado correctamente'})
        else:
            return jsonify({'error': 'El cuerpo de la solicitud debe contener el estado del LED'}, 400)



if __name__ == "main":
    app.run(host="0.0.0.0", port=5001)
