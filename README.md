## Hologram Vehicle Monitoring Example

This example uses the Hologram Nova USB Modem with a Raspberry Pi in order to relay OBDII data to the AdafruitIO cloud. This guide assumes you have access to a terminal on your Raspberry Pi. I recommend [connecting via a serial terminal.](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-5-using-a-console-cable/)

## Installation

Run the following in a terminal, it will install the [Hologram](https://hologram.io/docs/guide/nova/developer-tools/), [Adafruit-IO](https://github.com/adafruit/io-client-python) and [OBD](https://github.com/brendan-w/python-OBD) Python SDKs as well as the Hologram CLI.

```bash
curl -L hologram.io/python-install | bash
curl -L hologram.io/python-update | bash

sudo pip install adafruit-io
sudo pip install obd
```

## Hardware

- Hologram NOVA https://hologram.io/nova/
- Raspberry Pi 3
- USB OBDII ELM327 Reader https://www.amazon.com/gp/product/B074V5YBYR/ref=oh_aui_detailpage_o03_s00?ie=UTF8&psc=1

## Run the Example

1. Clone this repo
2. Create a file adafruitConfig.py with the following:

```python
ADAFRUIT_IO_KEY      = 'YOUR ADAFRUIT IO KEY'
ADAFRUIT_IO_USERNAME = 'YOUR ADAFRUIT IO USERNAME'
```

3. Spin up the network connection through the NOVA
```bash
sudo hologram network connect
```

4. Start the script
```bash
sudo python main.py
```

5. Go to your adafruit.io account and create a dashboard to watch your new feed named "fleet"
6. ????
7. PROFIT

## OBD-II Commands

The main example send up values returned from the SPEED command. Below is a basic example of how to use the OBD python library.

Here is a link to all the supported commands: https://github.com/brendan-w/python-OBD/blob/master/docs/Command%20Tables.md

Give different ones a shot and see if there is data that you might find more useful from your vehicle.

```python
import obd

connection = obd.OBD() # auto-connects to USB or RF port
cmd = obd.commands.STATUS # select an OBD command (sensor)
response = connection.query(cmd) # send the command, and parse the response

print(response.value) # returns unit-bearing values thanks to Pint
```

## Adafruit IO dashboard
