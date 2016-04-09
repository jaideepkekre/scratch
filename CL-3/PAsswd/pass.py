#!/usr/bin/python 

"""
author: Jaideep Kekre
"""
import hashlib 


data_base_connection=dict()

def get_pw():   
        uid=raw_input('Enter user ID:')
        pwd=raw_input('Enter Password:')
        status=get_type(pwd)
        print status 
        data_base_connection[uid]=encrypt(pwd,status)
        print data_base_connection 
        
def get_type(pwd):
       
        if pwd.islower() :
                return 1 
        elif pwd.isupper() : 
                return 2 
        elif pwd.isdigit() : 
                return 3 
        elif pwd.isalnum() :
                return 4 
        else: 
                return 5 
        
def encrypt(pwd,status):
        if status == 1 :
                return do(pwd,1)
        if status == 2 :
                return do(pwd,None,2)
        if status == 3 :
                return do(pwd,None,None,3)
        if status == 4 :
                return do(pwd,None,None,None,4)
        if status == 5 :
                return do(pwd,None,None,None,None,5)                    

def do ( pwd ,a=None , b=None , c= None , d=None , e = None ) :
        if a is not None :
                return hashlib.sha1(pwd).hexdigest()
        if b is not None :
                return hashlib.sha1(pwd).hexdigest()  
        if c is not None :
                return hashlib.sha1(pwd).hexdigest()  
        if d is not None :
                return hashlib.sha1(pwd).hexdigest()  
        if e is not None :
                return hashlib.sha1(pwd).hexdigest()           
        
       
while True :
        get_pw()










