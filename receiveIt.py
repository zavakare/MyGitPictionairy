#!/usr/bin/env python

#recieves message

import socket
from Tkinter import *
import reciever

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('10.0.124.24', 1200))
serversocket.listen(5) # become a server socket, maximum 5 connections
while True:
    connection, address = serversocket.accept()
    buf = connection.recv(64)
    if len(buf) > 0:
        reciever.main(buf)

