# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 14:26:57 2018

@author: Sofia
"""

def count_until(tup):
    result = 0
    i = 0
#    print((tup[2].__class__.__name__) == "tuple")
    while (tup[i].__class__.__name__) != "tuple":
        result += 1
        i += 1
        if (tup[i].__class__.__name__) == "tuple":
            return(result)
            break
    if "tuple" not in (tup[i].__class__.__name__):
        return(-1)
    
    
    
    
    
ttup = (1, '2', 3, 4.0, 5j)

#ttup = (1, 2, (3,), 4.0, 5j)

print(count_until(ttup))