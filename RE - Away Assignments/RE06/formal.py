# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 12:07:13 2018

@author: Sofia
"""

def formal(name):
    palavras=name.split()
    SecondForm=(str(palavras[-1]) + ", ")
    for i in range ((len(palavras))-1):
        a=str(palavras[i])
        SecondForm=SecondForm+(str(a[0]) + ". " )
        i=i+1
    return(SecondForm)
    
    
#nome=input()
#print(formal(nome))