#!/usr/bin/env python

import socket
import tkMessageBox
import os
import requests

try:
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket.connect(('10.0.124.24', 1200))
except:
    tkMessageBox.showinfo("Error", "Cannot connect to server to send over the word to draw. The game will now shutdown.")
    os.system("./killAllPython.sh")

with open("drawThis.txt","r") as ins:
    lines = ins.readlines()
    for line in lines:
        word = line.split()
	clientsocket.send(word[0])

