#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 14:48:44 2019

@author: exame
"""

def  gcd(a, b):
    if a%b == 0:
        return(b)
    else:
        new_n = a%b
        return(gcd(a, new_n))
    

#print(gcd(25, 5))
#print(gcd(21, 14))
#print(gcd(65, 26))     