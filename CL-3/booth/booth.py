#!/usr/bin/python 

"""
author: Jaideep Kekre
"""

a=-25
b=25
product=0 
def rever(int_arg):
        str_arg=reversed(str(int_arg))


def multiply(): 
	global a 
        a_str=twos(a)
        #print a_str 
        
        y=reversed(a_str) 
        booth_bit=0
        index = 0 
         
         
        for lsb in y :
        	
        	lsb=int(lsb)
        	#print lsb, product
        	if lsb == 1 :	
        		if booth_bit == 0 : 
        			update_product(index,-1)
        	if lsb == 0 : 	
        		if booth_bit == 1  :	
        			update_product(index,1)
        	index=index+1
        	booth_bit=lsb 
        			
        return product 
        
def twos(aint):
	if aint >= 0 :
		
		return '0' + str(bin(aint)[2:])
		
		
	else :
		abin=str(bin(aint)[3:])
		abin='0'+abin
		
		
		new=str()
		for bit in abin:
			
			if bit == '1' :
				new=new+'0'
			if bit == '0' :
				new=new+'1'
		
		return add(new,'1')  
		
		
def add (n,m):
	return bin(int ( n,2) + int ( m , 2 ) )[2:]

def update_product(index,sign):
	global product
	if sign == 1 :
		product=product + b*(pow(2,index))
	if sign == -1 :
		product=product - b*(pow(2,index))  
print (multiply())
		
