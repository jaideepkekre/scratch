#!/bin/bash
#Owner :Jaideep Kekre
#_author_ = Jaideep Kekre
#_info_   = This module contains a Bash script 
echo "********************************"
nohup python ws.py 192.168.9.141:40123 > ws_logger.txt 2>&1& 
echo $! > pid_DO_NOT_DELTE.txt 
echo "Server started at PID:"
echo $!
echo "PID saved in pid_DO_NOT_DELTE.txt , contents are :"

cat pid_DO_NOT_DELTE.txt 

