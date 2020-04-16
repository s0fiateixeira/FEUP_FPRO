# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 16:14:34 2018

@author: Sofia
"""

num=int(input("Give me a number: "))

soma=0
for divisor in range (1, num+1):
    if num%divisor==0:
        divisor=num/divisor
        soma=soma+divisor
print(int(soma))