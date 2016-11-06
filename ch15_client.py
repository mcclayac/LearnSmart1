__author__ = 'anthonymcclay'
__project__ = 'LearnSmart1'
__date__ = '11/6/16'
__revision__ = '$'
__revision_date__ = '$'


#!/usr/bin/python

# This is client.py file

# Import socket module
import socket

# Create a socket object
s = socket.socket()

# Get local machine name
host = socket.gethostname()

# Reserve a port for your service.
port = 12345

s.connect((host, port))

print(s.recv(1024).decode('utf-8'))

# Close the socket when done
s.close