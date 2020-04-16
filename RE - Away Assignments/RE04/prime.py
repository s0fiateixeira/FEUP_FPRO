# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 13:57:04 2018

@author: Sofia
"""

n=int(input("Insira um número: "))

for i in range(2, n+1):
    if i != n:
        i = n % i
        if i == 0:
            result="False"
            print (result)
            break
    else:
        result="True"
        print (result)
        break