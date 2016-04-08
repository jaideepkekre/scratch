#/usr/bin/python
import random 
import multiprocessing
from multiprocessing import Process  
import math


elements_dict=dict()
global_list=list()
process_table=list()

def generate_data():
        max_data=raw_input("Enter the number of data values you want to create in Memory =====>\t")

        i=0
        elements=list()

        while i < int(max_data):
                number=random.randint(0,99999)
                elements.append(number)
                elements_dict[number]= i  
                i=i+1             
        
        print elements  
        return elements

 
def search(elements,element_to_search):          
        elements.sort()
        mid_pos = len(elements)/2        
        mid=elements[mid_pos]
       
        if mid == element_to_search :
                print "Found ===> " + str(element_to_search) + " at : " + str(elements_dict[element_to_search])
                return True 
                
        if len(elements) == 1 :
                print "Sorry ! Not found! :("
                return False 
                
        if mid < element_to_search  : 
                elements_arg = list(elements[mid_pos:])               
                search(elements_arg,element_to_search)   
                  
        if mid > element_to_search  : 
                elements_arg = list(elements[:mid_pos])              
                search(elements_arg,element_to_search)
ele=generate_data()
ip = int(raw_input("Enter element to search =======>\t"))

cpu_nos = multiprocessing.cpu_count()
length=len(ele)
unit=length/float(cpu_nos)
unit = int (round(unit))
lower=0
upper=unit
run=1

while run < cpu_nos:
        
      lis = ele[lower:upper]
      lower=lower+unit      
      upper=upper+unit
      run=run+1
      global_list.append(lis)
global_list.append(ele[upper-unit:])

for lis in global_list :         
        p=Process(target=search , args=(lis,ip))
        process_table.append(p)
        p.start()    
        

      


    
                  
                
        
