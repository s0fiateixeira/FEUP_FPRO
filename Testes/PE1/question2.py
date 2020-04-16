#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 17:19:40 2018

@author: exame
"""

d=int(input("Write a number: "))
num=int(input("Write another number: "))

result=0
dig=0
soma=0
dig1=0
while num//10!=0:
    
#    dig1=num%10
#    dig2=(((num%100)-dig1)//10)
#    dig3=((((num%1000)-dig1)//10)-dig2)//10
    dig=dig+((num%10**soma)-dig//10)
    dig1=dig1//10+dig//10
    soma=soma+1
    if (d>dig):
        result=result+(2*dig)
    else:
        result=result+0

print(result)