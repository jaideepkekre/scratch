#!usr/bin/python
"""
Owner :Jaideep Kekre
#_author_ = Jaideep Kekre
#_info_   = This module contains a Python Script
"""
import xml.etree.ElementTree as ET
import math
tree = ET.parse('math.xml')
root = tree.getroot()
#print root
op1 = ""
op2 = ""
oper = ""
for thing in root:
    # print thing.tag
    if thing.tag == "op1":
        op1 = thing.text

    if thing.tag == "op2":
        op2 = thing.text

    if thing.tag == "operation":
        oper = thing.text

print op1 , op2 , oper

if oper == "add":
    op1 = int(op1)
    op2 = int(op2)
    print op1 + op2

if oper == "cos":
    op1 = int(op1)
    op2 = int(op2)

    print "cos of " + str(op1) + " is " +str(math.cos(op1))
    print "cos of " + str(op2) + " is " +str(math.cos(op2))




    # print thing.attrib
    #print thing.text
