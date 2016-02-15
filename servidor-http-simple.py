#!/usr/bin/python

"""
Simple HTTP Server
Jesus M. Gonzalez-Barahona and Gregorio Robles
{jgb, grex} @ gsyc.es
TSAI, SAT and SARO subjects (Universidad Rey Juan Carlos)
"""

import socket

# Create a TCP objet socket and bind it to a port
# We bind to 'localhost', therefore only accepts connections from the
# same machine
# Port should be 80, but since it needs root privileges,
# let's use one above 1024

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.bind(('', 1234))

# Queue a maximum of 5 TCP connection requests

mySocket.listen(5)

# Accept connections, read incoming data, and answer back an HTML page
#  (in an infinite loop)

while True:
    print 'Waiting for connections'
    (recvSocket, address) = mySocket.accept()
    body = "Hola. Eres de esta IP:" + str(address[0]) 
    body += " y de este puerto:" + str(address[1])
    print 'HTTP request received:'
    print recvSocket.recv(1024)
    recvSocket.send("HTTP/1.1 200 OK\r\n\r\n" +
                    "<html><body><h1>"+ body + "</h1></body></html>" +
                    "\r\n")
    recvSocket.close()
