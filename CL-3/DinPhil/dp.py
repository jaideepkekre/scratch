#!/usr/bin/python 

"""
author: Jaideep Kekre
"""

#!/usr/bin/python 
from multiprocessing import Manager
import threading 

from time import sleep

manager=Manager()

#fork_list=manager.list()
philo_list=manager.list()
locked=manager.list()
number=-1 

def init():
	global number
        x=int(raw_input("Enter Number of Philosophers "))
        number=x
        
        i=0 
        while i<x:                                
                
                philo_list.append(i)
                
                '''
                H,S,W
                hungry , sleeping , waiting
                '''
                
                i=i+1
                
def eat(philo):

        left = -1
        right = -1 
        x=philo
        
        if x == 0 :
                left = number-1
        else :
                left=x-1 
        
        right = x 
        done=False
        
        while not done :
                status = get_status(left,right)
                if status == True :
                
                        set_lock(left,right)
                        sleep(10)
                        print"Philosopher:" + str(x) + "has eaten "
                        done=True 
                        release_lock(left,right)
                        return True 
                        
                else :
                        print"Philosopher:" + str(x) + "is waiting "
                        sleep(0.5)

def get_status(left,right):
        if left in locked:        	
                return False
        elif right in locked:        	
                return False
        else:	
        	
                return True 
                
                
def set_lock(left,right): 
        done=False 
        lock=threading.Lock()
        while not done :
                if get_status(left,right) == True :
                        with lock :
                                locked.append(left)
                                locked.append(right)
                                done=True 
def release_lock(left,right):       
        lock=threading.Lock()
        
	if left in locked :
                with lock :
                        locked.remove(left)
                        
	if right in locked :
                with lock :
                        locked.remove(right)

def start_dinner():
	i=0
	
	
	while i<number:		
		philo  = philo_list.pop()	
		thread = threading.Thread(target=eat, args=[philo])
		thread.start()
		i=i+1

	
                         
       
    
        
                        
                
  
         
 
        

 
init()

start_dinner()

                


