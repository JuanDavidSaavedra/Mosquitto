# publicador2.py
import paho.mqtt.client as mqtt
import time

client = mqtt.Client()
client.connect("localhost", 1883, 60)

while True:
    client.publish("topic/test", "Mensaje de Amazon")
    time.sleep(5)