# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 17:25:21 2018

@author: Sofia
"""

def discard_middle(s):
    result=""
    if len(s)<=3:
        return("")
    else:
        return(result+s[0]+s[1]+s[-2]+s[-1])
    
    
    
    
    
#string="string"

#string="n"

#print(discard_middle(string))