#!/usr/bin/python 
import math
from hashlib import sha1
from random import randint 
"""
author: Jaideep Kekre
"""
message="I am ted."

def H(message):
        return int(sha1(message).hexdigest(),16)


def mod_inv(x,p):

        y = pow(x, p-2, p)
        return y 
        
def generate_keys():
        q=11
        p=23
        i=(p-1)/float(q)
        g=(math.pow(2,i))%p
        
        return [p,q,g]
        
        
def create_keys(p,q,g):
        x=7 
        y=(math.pow(g,x))%p        
        return [x,y]


def sign(p,q,g,x,y):
        k = randint(1, q-1)
        
        """
        int?
        """
        r = (int(math.pow(g, k)) % p) % q
        print "r-->" + str(r)
        
        k_inv = mod_inv(k, q)
        s = int(k_inv * (H(message) + x*r)) % q
        
        print"s-->" + str(s)
        return [r,s] 
        
        
def verify(p,q,r,s,y):
        w = int(mod_inv(s, q))
        u1 = (H(message) * w) % q
        u2 = (r*w) % q
        v = (int(math.pow(g, u1) * math.pow(y, u2)) % p) % q
       
        print 'v--->'  + str(v)
        print 's --->' + str(s)
        
        
        
        
p , q , g = generate_keys()
x,y = create_keys(p,q,g)
r,s=sign(p,q,g,x,y)
verify(p,q,r,s,y)

        
               
