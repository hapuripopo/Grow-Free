import socket, time
import requests, json
from influxdb import InfluxDBClient as influxdb

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
print('Conneted...')

# awaiting for message
while True:
    client_soc, addr = server_soc.accept()
    print('Connected client addr: ', addr)
    
    data = client_soc.recv(1024).decode()
    print(f'recv msg: {data}')

    if data == 'On':
        # shoot
        dbdata = [{
            'measurement' : 'plant',
            'tags':{
                'VisionUni' : '2410',
            },
            'fields':{
                'check' : 'true',
            }
        }]
        client = None
        try:
            client = influxdb('localhost',8086,'root','root','plant')
        except Exception as e:
            print("Exception "+str(e))
        
        if client is not None:
            try:
                client.write_points(dbdata)
            except Exception as e:
                print("Exception write : "+str(e))
            finally:
                client.close()
        reply = 'succeed'
        # Sending reply
        client_soc.send(bytes(reply, 'utf-8'))

# lose connections
time.sleep(3)
server_soc.close()