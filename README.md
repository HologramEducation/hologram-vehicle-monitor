## Hologram Vehicle Monitoring Example

### WIP

We'll have a full write up explaining how to get everything set-up from scratch and connecting to each platform.

## Pre-reqs

Install the following!

adafruit-io python sdk https://github.com/adafruit/io-client-python

Hologram Nova SDK https://github.com/hologram-io/hologram-python

Hologram CLI https://hologram.io/docs/guide/nova/developer-tools/

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
