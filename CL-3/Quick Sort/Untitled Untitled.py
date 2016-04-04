#!/usr/bin/python 

"""
author: Jaideep Kekre
"""
from multiprocessing import Pool  
def echo(x):
        print x 
p=Pool(4)


p.map(echo,1,3,4)
