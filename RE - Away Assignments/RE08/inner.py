# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 17:52:09 2018

@author: Sofia
"""

def inner(u, v):
    result=0
    for i in range (len(v)):
        result=result+(int(v[i])*int(u[i]))
    return(result)
        
        

#prim=[]
#seg=[]

#prim=[1, 2]
#seg=[2, 4]
    
#prim=[1, 2, 3, 4, 5]
#seg=[2, 3, 4, 5, 6]
#
#print(inner(prim, seg))