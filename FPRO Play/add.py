# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 19:54:36 2018

@author: Sofia
"""

def add_item(tup, idx, item):
    new = []
    for i in range(len(tup)):
        if i == idx:
            new += tuple(item)
        else:
            new += tuple(tup[i])
    return(new)
    
    
    
ttup=(1,2,3)
iitem=[4,5]
iidx=1
print(add_item(ttup, iidx, iitem))