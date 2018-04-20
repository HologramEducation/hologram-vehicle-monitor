import obd

connection = obd.OBD() # auto-connects to USB or RF port

cmd = obd.commands.STATUS # select an OBD command (sensor)

response = connection.query(cmd) # send the command, and parse the response

print(response.value) # returns unit-bearing values thanks to Pint
