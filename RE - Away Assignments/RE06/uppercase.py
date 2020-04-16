# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 12:07:35 2018

@author: Sofia
"""

def uppercase(astring):
    for i in range (2):
        if ((astring.split())[i]!=((astring.split())[i]).lower()):
#    !=lower em vez de =l.upper por causa dos pontos e assim
            return(astring.upper())
        else:
            return(astring)
    
    
#frase=input("Write a sentence: ")
#print(uppercase(frase))