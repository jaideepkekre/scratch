#!usr/bin/python
#Owner :Jaideep Kekre
#_author_ = Jaideep Kekre
#_info_   = This module contains a Python Script for scanning ports
from socket import * 
import sys

def main(target):

    #target = raw_input('Enter host to scan:')
    #target = sys.argv[0]
    #print target
    targetIP = gethostbyname(target)
    print 'Starting scan on host ', targetIP

    #scan reserved ports
    #65535
    store = ""
    for i in range(1,65535):
        #print i 
        s = socket(AF_INET, SOCK_STREAM)
        result = s.connect_ex((targetIP, i))
        #print result              
        if(result == 0) :
            print 'Port %d: OPEN' % (i,)            
            genericSTR="Port Open :"
            store=store+genericSTR+str(i)+'\n'            
        s.close()
    pass

    filename="Portlogger"+"_"+str(targetIP)+".txt"
    portfile=open(filename,'w+')
    portfile.writelines(store)
    portfile.close()
    print("Scan done!")
    print("Output written to Portlogger_"+str(targetIP)+".txt")

	


if __name__ == '__main__':
    
    main(sys.argv[1])