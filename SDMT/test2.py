#!usr/bin/python
"""
Owner :Jaideep Kekre
#_author_ = Jaideep Kekre
#_info_   = This module contains a Python Script
"""
import xml.etree.ElementTree as ET
import math
tree = ET.parse('math2.xml')
root = tree.getroot()
#print root
op1 = list()
oper = ""
x = ""
for thing in root:
    # print thing.tag
    print thing
    if thing.tag == "op":
        op1.append(thing.text)

    if thing.tag == "operation":
        oper = thing.text

print op1, oper

if oper == "cos":
    x = 0
    while len(op1) > 0:
        x = float(op1.pop())
        print "The COS of " + str(x) + "is :" + str(math.cos(x))

if oper == "sin":
    x = 0
    while len(op1) > 0:

        x = float(op1.pop())
        print "The sin of " + str(x) + "is :" + str(math.sin(x))

if oper == "add":
    x = 0
    while len(op1) > 0:
        x = x+float(op1.pop())

    print x

if oper == "sub":
    x = 0
    while len(op1) > 0:
        x = x-float(op1.pop())

    print x








    # print thing.attrib
    #print thing.text
