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
    location = hologram.network.location

    cmd = obd.commands.SPEED # select an OBD command (sensor)
    obd_response = connection.query(cmd) # send the command, and parse the response
    obd_data = obd_response.value

    if obd_data is None:
        obd_data = 0

    if location is None:
        lat = 0
        lon = 0
    else:
        lat = location.latitude
        lon = location.longitude

    data = str(obd_data) + ',' + str(lat) + ',' + str(lon) + ', 0'

    print('Publishing: ' + str(data))
    client.publish('fleet/csv', str(data))
    time.sleep(120)
