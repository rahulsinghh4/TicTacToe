#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 11:30:29 2018

@author: Rahul
"""
import random
x = input("Rock, paper, or scissors? Enter 1 for rock, 2 for paper, and 3 for scissors")
#x = z
#if str(x)=="rock":
 #   z = 1
#if str(x)=="paper":
 #   z = 2
#if str(x)=="scissors":
 #   z = 3
#else:
 #   print("invalid response")     
#str("paper")=int(2)
#str("scissors")=int(3)
y = random.randint(1,4)
if int(x) == y:
    print("tie")
elif int(x)==2 and y==1:
    print("you win!")
elif int(x)==3 and y==1:
    print("you lose:(") 
elif int(x)==1 and y==2:
    print("you lose :(")
elif int(x)==3 and y==2:
    print("you win!")
elif int(x)==1 and y==3:
    print("you win!")
else:
    print("you lose :(")   
    
#elif int(x)==2 and y==3:
   # print("you lose :(")
