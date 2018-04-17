# Import standard python modules.
import random
import sys
import time

import obd

connection = obd.OBD() # auto-connects to USB or RF port

from Adafruit_IO import MQTTClient
from Hologram.HologramCloud import HologramCloud

ADAFRUIT_IO_KEY      = 'YOUR ADAFRUIT IO KEY'
ADAFRUIT_IO_USERNAME = 'YOUR ADAFRUIT IO USERNAME'

def connected(client):
    print('Connected to Adafruit IO!')

def disconnected(client):
    print('Disconnected from Adafruit IO!')
    sys.exit(1)

client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

client.on_connect    = connected
client.on_disconnect = disconnected

client.connect()

client.loop_background()

while True:
    hologram = HologramCloud(None, network='cellular')
    location = hologram.network.location

    cmd = obd.commands.SPEED # select an OBD command (sensor)
    response = connection.query(cmd) # send the command, and parse the response
    
    data = { 'location': location, 'speed': response.value.to("mph") }

    client.publish('fleet', data)
    time.sleep(60)
