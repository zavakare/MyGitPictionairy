#!/usr/bin/env python

import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('10.0.124.24', 8089))
clientsocket.send('shut up alex')
