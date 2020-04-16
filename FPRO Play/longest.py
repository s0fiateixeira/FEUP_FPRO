# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 17:30:25 2018

@author: Sofia
"""

def longest(s):
    t = s.split()
    maximo = 0
    for i in range(len(t)):
        if (len(t[i])) > maximo:
            maximo = len(t[i])
    return(maximo)
    
    
    
    
    
#sentence = "A list with some words"

#sentence = "Unnecessarily long sentence since the longest word is the first one"

#print(longest(sentence))