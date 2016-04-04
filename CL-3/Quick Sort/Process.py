from multiprocessing import Manager , Queue , Process 
from random import randint 

def sort(lis):
	if len(lis) == 0 :
		return []
	
	pivot = lis[0]
	lower = sort(process_lesser(lis[1:],pivot))
	upper = sort(process_higher(lis[1:],pivot))
	
	return  lower + [pivot] + upper  
	
def process_lesser(arg_list,pivot):
        que=Queue()
        p=Process(target=lesser,args=(arg_list,pivot,que))
       
        p.start()
        lis=que.get()
        #p.join()        
        return lis
        
def process_higher(arg_list,pivot):
        que=Queue()
        p=Process(target=higher,args=(arg_list,pivot,que))
        
        p.start()
        lis=que.get()
        #p.join()        
        return lis 
        
        

def lesser (arg_list,pivot,que):        
	elements = [x for x in arg_list if x < pivot]
	que.put(elements)
	
def higher (arg_list,pivot,que):
	elements = [x for x in arg_list if x > pivot]
	que.put(elements)  


x=0
lis=list()
while x < 1000 :
        num = randint(1,5000)
        lis.append(num)
        x=x+1
        
print sort(lis)

