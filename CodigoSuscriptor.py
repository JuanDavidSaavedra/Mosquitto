import paho.mqtt.client as mqtt

# Configuración del broker
BROKER_HOST = "IP_DEL_BROKER"  # Cambia esta IP por la IP del broker
BROKER_PORT = 1883

# Callback para manejar mensajes recibidos
def on_message(client, userdata, msg):
    print(f"Mensaje recibido en el tema {msg.topic}: {msg.payload.decode()}")

# Suscriptor 1
def subscriber_1():
    client = mqtt.Client("Subscriber1")
    client.on_message = on_message
    client.connect(BROKER_HOST, BROKER_PORT)
    client.subscribe("topic/sensor1")
    client.loop_forever()

# Suscriptor 2
def subscriber_2():
    client = mqtt.Client("Subscriber2")
    client.on_message = on_message
    client.connect(BROKER_HOST, BROKER_PORT)
    client.subscribe("topic/sensor2")
    client.loop_forever()

# Suscriptor 3
def subscriber_3():
    client = mqtt.Client("Subscriber3")
    client.on_message = on_message
    client.connect(BROKER_HOST, BROKER_PORT)
    client.subscribe("topic/sensor3")
    client.loop_forever()

# Ejecutar los suscriptores
if __name__ == "__main__":
    import threading
    threading.Thread(target=subscriber_1).start()
    threading.Thread(target=subscriber_2).start()
    threading.Thread(target=subscriber_3).start()
