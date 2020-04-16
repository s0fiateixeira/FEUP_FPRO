# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 19:11:35 2018

@author: Sofia
"""

def unpack_rev(atuple):
    new = ""
    for i in range(len(atuple)-1, 0-1, -1):
        new = new + atuple[i] + " "
    return(new)
    
    
#tuplo = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
#print(unpack_rev(tuplo))