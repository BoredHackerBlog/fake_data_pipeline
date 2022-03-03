import paho.mqtt.client as mqtt
from faker import Faker
from time import sleep
import json

sleep(10)

topic = "userdata/raw"

broker = "mosquitto"

client = mqtt.Client("producer")

client.connect(broker, keepalive=120)

fake = Faker()

while True:
    sleep(1)
    for _ in range(3):
        login_event = {"user": fake.ascii_safe_email(), "ip": fake.ipv4_public(address_class="c")}
        client.publish(topic, json.dumps(login_event))
