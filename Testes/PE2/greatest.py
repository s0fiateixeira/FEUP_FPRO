#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 16:22:03 2018

@author: exame
"""

def greatest(num):
    new = ""
    if num < 0:
       return("ERROR") 
    else:
        num = str(num)
        num = tuple(num)
        num = (sorted(num))
        for i in range(len(num)-1, 0, -1):
            new += str(num[i])
    new += str(num[0])
    return(int(new))
    
    
    
#numero = 310909

#numero = 7187

#numero = 99

#print(greatest(numero))