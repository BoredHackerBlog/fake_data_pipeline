import paho.mqtt.client as mqtt
import json
import base64
import requests
import diskcache as dc
from time import sleep

sleep(10)

topic = "userdata/raw"

broker = "mosquitto"

cache = dc.Cache('tmp')

user = "admin"
password = "admin"
bas64encoded_creds = base64.b64encode(bytes(user + ":" + password, "utf-8")).decode("utf-8")
headers = {"Content-type": "application/json", "Authorization": "Basic " + bas64encoded_creds}
index = "login_events"
zinc_host = "http://zinc:4080"
zinc_url = zinc_host + "/api/" + index + "/document"

def on_message(client, userdata, message):
    json_str = message.payload.decode()
    res = requests.put(zinc_url, headers=headers, data=json_str)

client = mqtt.Client("consumer")
client.on_message = on_message

client.connect(broker, keepalive=120)

client.subscribe(topic)

client.loop_forever()