import socket, time
import requests, json
from influxdb import InfluxDBClient as influxdb

# insert your information
HOST = '10.40.45.19'
PORT = 12345

# server socket open
server_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')

try:
    server_soc.bind((HOST, PORT))
except socket.error:
    print('Bind failed')

# ready to connect with client
server_soc.listen()
print('Connected...')

client_soc, addr = server_soc.accept()
print('Connected client address: ', addr)

# waiting for message
while True:
    data = client_soc.recv(1024).decode()
    print(f'Received massage: {data}')

    # Android App sends a signal to watering
    if data == 'ON':
        # Run EV3
"""
check
"""
        # And shoot data for DB
        db_data = [{
            'measurement': 'plant',
            'tags': {
                'VisionUni': '2410',
            },
            'fields': {
                'check': 'true',
            }
        }]

        client = None
        reply = 'SUCCESS'

        try:
            client = influxdb('localhost', 8086, 'root', 'root', 'plant')
        except Exception as e:
            print("Exception ", str(e))

        if client is not None:
            try:
                client.write_points(db_data)
            except Exception as e:
                print("Exception write : ", str(e))
                reply = 'ERROR'
            finally:
                client.close()

        # Sending reply
        client_soc.send(bytes(reply, 'utf-8'))

    # Android App sends a signal to show DB data
    if data == 'SHOW_DATA':
        pass
"""
check
"""
# lose connections
time.sleep(3)
server_soc.close()
