#!/usr/bin/env python

import socket

UDP_IP = "10.0.124.24"

UDP_Port = 1200

MESSAGE = "Hello, World!"

print "UDP target IP:", UDP_IP

print "UDP target port:", UDP_PORT

print "message:", MESSAGE

sock = socket.socket(socket.AF_INET, # Internet

socket.SOCK_DGRAM) # UDP

sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
