import os
import json
from pynello import Nello
import paho.mqtt.client as mqtt

n = Nello(username=os.environ['NELLO_USERNAME'], password=os.environ['NELLO_PASSWORD'])

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT with result code "+str(rc))

    for location in n.locations:
        data = { "type": "location", "location_id": location.location_id, "address": location.address }
        msg = json.dumps(data)

        print msg
        client.publish(os.environ['MQTT_TOPIC'], msg)

    client.subscribe(os.environ['MQTT_TOPIC'])

def on_message(client, userdata, msg):
    splits = msg.payload.split(' ')

    if splits[0].lower() == 'open':
        data = { 'type': 'open', 'location_id': splits[1] }
    else:
        data = json.loads(msg.payload)

    if data['type'].lower() == 'open':
        print "Opening: %s" % (data['location_id'])
        n.open_door(data['location_id'])

if os.environ.get('MQTT_PORT', None) is None:
    port = 1883
else:
    port = int(os.environ['MQTT_PORT'])

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

if os.environ.get('MQTT_USER', None) is not None:
    client.username_pw_set(os.environ['MQTT_USER'], os.environ['MQTT_PASSWORD'])
    
client.connect(os.environ['MQTT_BROKER'], port, 60)

client.loop_forever()
