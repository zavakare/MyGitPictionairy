#!/usr/bin/env python

#loads all category files  into arrays - each entry separated by space

import random
import GamePlay
import startGame

def arrayOne():
	with open("category1.txt","r") as ins:
		lines = ins.readlines()
                global array 
		array = []
                for line in lines:
			words = line.split()
			for word in words:
                        	array.append(word)

def arrayTwo():
	with open("category2.txt","r") as ins:
		lines = ins.readlines()
                global array2
                array2 = []
                for line in lines:
                        words = line.split()
                        for word in words:
                                array2.append(word)
def arrayThree():
        with open("category3.txt","r") as ins:
		lines = ins.readlines()
                global array3
                array3 = []
                for line in lines:
                        words = line.split()
                        for word in words:
                                array3.append(word)

def arrayFour():
        with open("category4.txt","r") as ins:
		lines = ins.readlines()
                global array4
                array4 = []
                for line in lines:
                        words = line.split()
                        for word in words:
                                array4.append(word)
