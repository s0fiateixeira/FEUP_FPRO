#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 14:45:24 2019

@author: exame
"""

def ackermann(m, n):
    if m == 0:
        return(n+1)
    if m > 0 and n == 0:
        return(ackermann(m-1,1))
    else:
        return(ackermann(m-1, ackermann(m, n-1)))
        
#print(ackermann(0, 0))
#print(ackermann(2, 1))
#print(ackermann(3, 4))