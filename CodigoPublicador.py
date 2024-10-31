import paho.mqtt.client as mqtt
import time

# Configuración del broker
BROKER_HOST = "localhost"  # Cambiar a la IP del broker si es remoto
BROKER_PORT = 1883

# Crear un cliente de publicación
client = mqtt.Client("Publisher1")

# Conectarse al broker
client.connect(BROKER_HOST, BROKER_PORT)

# Publicador 1
def publisher_1():
    while True:
        client.publish("topic/sensor1", "Mensaje desde Publisher 1")
        time.sleep(5)

# Publicador 2
def publisher_2():
    client2 = mqtt.Client("Publisher2")
    client2.connect(BROKER_HOST, BROKER_PORT)
    while True:
        client2.publish("topic/sensor2", "Mensaje desde Publisher 2")
        time.sleep(5)

# Publicador 3
def publisher_3():
    client3 = mqtt.Client("Publisher3")
    client3.connect(BROKER_HOST, BROKER_PORT)
    while True:
        client3.publish("topic/sensor3", "Mensaje desde Publisher 3")
        time.sleep(5)

# Ejecutar los publicadores
if __name__ == "__main__":
    import threading
    threading.Thread(target=publisher_1).start()
    threading.Thread(target=publisher_2).start()
    threading.Thread(target=publisher_3).start()
