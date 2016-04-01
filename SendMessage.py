#!/usr/bin/env python

import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('10.0.124.24', 1200))
with open("drawThis.txt","r") as ins:
	lines = ins.readlines()
	for line in lines:
		word = line.split()
		clientsocket.send(word[0])
