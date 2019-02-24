#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 11:12:18 2018

@author: Rahul
"""

x = input('enter leap year:')
for y in range (0,100):
    l1 =[100*y]
    l2 =[400*y]
if int(x) in l2:
    print("leap year")    
elif int(x) in l1:
    print("not a leap year")
        


for z in range(1,10000):
    l3 = [z*4]
    
elif int(x) in l3:
   print("leap year")
else:
   print("not leap year")
