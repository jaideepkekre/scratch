#!/usr/bin/python 

"""
author: Jaideep Kekre
"""

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def mod_inv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m
def modinv(x,p):

        y = pow(x, p-2, p)
        return y 
        
        
q= mod_inv(2,5)
w=mod_inv(2,5)

if q==w:
        print "T"



