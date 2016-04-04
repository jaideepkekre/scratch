#!/usr/bin/python 

"""
author: Jaideep Kekre
"""
from multiprocessing import Pool  
def echo(x):
        print x 
p=Pool(4)
a=[34,5,]

x=10
while x >0:
        p.map(echo,[a])
        x=x-1
