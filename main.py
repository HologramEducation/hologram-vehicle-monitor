import sys
import time
import obd

# adafruitConfig.py should store your credentials
# ADAFRUIT_IO_KEY and ADAFRUIT_IO_USERNAME
from adafruitConfig import *
from Adafruit_IO import MQTTClient

from Hologram.HologramCloud import HologramCloud

connection = obd.OBD() # auto-connects to USB or RF port

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

    cmd = obd.commands.SPEED # select an OBD command (sensor)
    obd_response = connection.query(cmd) # send the command, and parse the response

    location = hologram.network.location
    if location is None:
        data = { 'location': 'None', 'speed': obd_response.value }
    else:
        print 'Latitude: ' + str(location.latitude)
        print 'Longitude: ' + str(location.longitude)
        data = {
                'location':
                    { 'lat': str(location.latitude), 'lon': str(location.longitude)},
                'speed': obd_response.value
                }

    client.publish('fleet', str(data))
    time.sleep(60)
