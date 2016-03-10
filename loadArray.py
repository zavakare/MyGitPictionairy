#!/usr/bin/env python

import random
import GamePlay
import startGame

def arrayOne():
	with open("category1.txt","r") as ins:
                global array 
		array = []
                for line in ins:
                        array.append(line)

def arrayTwo():
	with open("category2.txt","r") as ins:
                global array2 
		array2 = []
                for line in ins:
                        array2.append(line)
def arrayThree():
        with open("category3.txt","r") as ins:
		global array3
                array3 = []
                for line in ins:
                        array3.append(line)

def arrayFour():
        with open("category4.txt","r") as ins:
		global array4
                array4 = []
                for line in ins:
                        array4.append(line)

