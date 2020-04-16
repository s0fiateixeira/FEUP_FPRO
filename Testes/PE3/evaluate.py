#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 17:12:14 2018

@author: exame
"""

def evaluate(a, x):
    soma = 0
    for i in range(len(a)):
        soma += (a[i])*(x**i)
    return(soma)
    
    
#print(evaluate([1, 2, 4], 5))
#print(evaluate([1, 2, 4], 10))
#print(evaluate([1, 2, 4, 6, 8], 2))
    
