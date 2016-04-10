#!/usr/bin/python 

"""
author: Jaideep Kekre

"""
x=[1,23,45,6,7,88,3,3,3,3,3,3,3,3,3,3,223,445,6]

def oddevenSort(x):
	sorted = False
	while not sorted:
		sorted = True
                print "1"
		for i in range(0, len(x)-1, 2):
			if x[i] > x[i+1]:
				x[i], x[i+1] = x[i+1], x[i]
				sorted = False
		for i in range(1, len(x)-1, 2):
			if x[i] > x[i+1]:
				x[i], x[i+1] = x[i+1], x[i]
				sorted = False
	return x




print(oddevenSort(x))
