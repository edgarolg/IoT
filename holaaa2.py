from flask import Flask, request, jsonify
from grovepi import *

app = Flask(__name__)

# sensores
sensor_ultrasonico = 1
sensor_temperatura = 2
sensor_mov_adentro = 3
sensor_mov_afuera = 4

# actuadores
led_spotlight_1 = 5
led_spotlight_2 = 6
led_spotlight_3 = 7
led_aroma_1 = 8
led_aroma_2 = 9
buzzer = 10
servo = 11

# establecer pines
pinMode(sensor_ultrasonico, "INPUT")
pinMode(sensor_temperatura, "INPUT")
pinMode(sensor_mov_adentro, "INPUT")
pinMode(sensor_mov_afuera, "INPUT")
pinMode(led_spotlight_1, "OUTPUT")
pinMode(led_spotlight_2, "OUTPUT")
pinMode(led_spotlight_3, "OUTPUT")
pinMode(led_aroma_1, "OUTPUT")
pinMode(led_aroma_2, "OUTPUT")
pinMode(buzzer, "OUTPUT")
pinMode(servo, "OUTPUT")

# funciones
def runModo(modo_int):
    if modo_int == 1: # modo speech
        # prender spotlights 
        digitalWrite(led_spotlight_1, 1)
        digitalWrite(led_spotlight_2, 1)
        digitalWrite(led_spotlight_3, 1)
        # establecer temperatura
        digitalWrite(servo, 1)
        # establecer aroma
        digitalWrite(led_aroma_1, 1)
        digitalWrite(led_aroma_2, 1)
        # prender pantalla

    elif modo_int == 2: # modo video
        # prender pantalla
        # prender luces LED
        # prender bocinas
        # digitalWrite(buzzer, )
        digitalWrite()
    elif modo_int == 3:
        digitalWrite()


# funciones app
@app.route("/")
def hello():
    return "Hello World!"


@app.route('/modo', methods=['PUT'])
def controlLed():
    
    data = request.get_json()
    
    if 'modo' in data:
        runModo(data['modo'])
        return jsonify({'message': 'Modo establecido.'})

    else:
        return jsonify({'error': 'Mensaje no entendido.'}, 400)



if __name__ == "main":
    app.run(host="0.0.0.0", port=8080)