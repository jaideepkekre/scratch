#!/bin/bash
#Owner :Jaideep Kekre
#_author_ = Jaideep Kekre
#_info_   = This module contains a Bash script 
echo "*****************************************"
kill -9 `cat pid_DO_NOT_DELTE.txt`
echo "SERVER STOPPED"

rm pid_DO_NOT_DELTE.txt 
echo "Cleaned up PID file!"
echo "*****************************************"