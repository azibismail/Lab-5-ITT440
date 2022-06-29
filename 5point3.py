import socket
import sys
import json

s=socket.socket()

port=8080

s.connect(('10.1.1.85',port))

data=s.recv(1024)
data=data.decode("utf-8")

s.send(b'Thank You from Client!');

dataJ=json.loads(data)

print(type(dataJ))
print(dataJ)

s.close()
