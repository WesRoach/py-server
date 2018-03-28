#!/usr/bin/python
# Notes: https://www.youtube.com/watch?v=DIPZoZheMTo

import socket
import threading

#AF_INIT - IPv6
#SOCK_STREAM - TCP Connection
#SOCK_DGRAM - UDP Connection
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind(('0.0.0.0', 10000))

sock.listen(1)

connections = []

def handler(c, a):
    global connections
    while True:
        # c (connection) is receiving data
        data = c.recv(1024) # max data is 1024 bytes
        for connection in connections:
            connection.send(bytes(data))
        if not data:
            connections.remove(c)
            c.close()
            break

while True:
    # c - connection; a - address (clients)
    c,a = sock.accept()
    # connection thread
    cThread = threading.Thread(target=handler, args=(c,a))
    cThread.daemon = True
    cThread.start()
    connections.append(c)
    print(connections)
