__author__ = 'anthonymcclay'
__project__ = 'LearnSmart1'
__date__ = '11/6/16'
__revision__ = '$'
__revision_date__ = '$'


#!/usr/bin/python

# This is server.py file
# Import socket module
import socket

# Create a socket object
s = socket.socket()

# Get local machine name
host = socket.gethostname()
print("\n Local machine name: ",host)

hostIP = socket.gethostbyname(host)
print("Hostname IP : " , hostIP)



# Reserve a port for your service.
port = 12345
print("\n port: ",port)

# Bind to the port
s.bind((host, port))

# Now wait for client connection.
s.listen(5)

while True:
    # Establish connection with client.
    c, addr = s.accept()
    print("Got connection from", addr)
    c.send("Thank you for connecting".encode('utf-8'))
    # Close the connection
    c.close()


