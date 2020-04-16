# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 18:58:27 2018

@author: Sofia
"""

def pascal(n):
    number=0
    for i in range(n):
        for j in range(n):
            number=i*j
            return(number)
            j=j+1
        i=i+1
    
    
    
    
numero=3
#
#numero=5
#
print(pascal(numero))