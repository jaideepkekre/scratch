#!usr/bin/python
#Owner :Jaideep Kekre
#_author_ = Jaideep Kekre
#_info_   = This module contains a Python Script for scanning ports
from socket import * 
import sys
import threading

store =""
threads=[] 

def main(target):

    #target = raw_input('Enter host to scan:')
    #target = sys.argv[0]
    #print target
    targetIP = gethostbyname(target)
    print 'Starting scan on host ', targetIP

    #scan reserved ports
    #65535
    
    threadController(targetIP) 
    
        
    
    filename="Portlogger"+"_"+str(targetIP)+".txt"
    portfile=open(filename,'w+')
    portfile.writelines(store)
    portfile.close()
    print("Scan done!")
    print("Output written to Portlogger_"+str(targetIP)+".txt")
    print"YO1"
    exit()
    print "YO"

def threadController(argTarget):
    
    for argPort in range(5000):
        t = threading.Thread(target=threader,args=(argTarget,argPort))
        t.start()
        threads.append(t)
        
    for t in threads:
        t.join(0.0005)



def threader(argTarget,argPort):
    global store  
    #print argPort
    
    s = socket(AF_INET, SOCK_STREAM)
    result = s.connect_ex((argTarget,argPort))
    s.close()
    print argPort
    #print result              
    if(result == 0) :
        print 'Port %d: OPEN' % (argPort,)            
        genericSTR="Port Open :"
        store=store+genericSTR+str(argPort)+'\n'    
        
    




if __name__ == '__main__':
    
    main(sys.argv[1])