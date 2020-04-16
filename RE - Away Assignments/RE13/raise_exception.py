# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 11:44:25 2019

@author: Sofia
"""

def raise_exception(alist, value):
    result = list([])
    for i in range(len(alist)):
        if alist[i] <= value:
            my_error = ValueError(str(alist[i]) + " is not greater than " + str(value))
            result.append(my_error)
    return(result)
            
   
#print(raise_exception([1, -2, 3, 0], 3))
#print(raise_exception([3], 2))