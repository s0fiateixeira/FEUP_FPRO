# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 16:00:36 2018

@author: Sofia
"""

def collatz(n):
    result = str(n)
    for i in range (n, 0, -1):
        if (n%2)==0:
            result = result + "," + str(int(i/2))
        else:
            result = result + "," + str((i*3)+1)
    return(result)
    
    
     
number=3

#number=12


print(collatz(number))