#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 15:05:22 2019

@author: exame
"""

def maximum_depth(l):
    maximo = 1
    for i in range(len(l)):
        depth = len(l[i])+2
        if depth >= maximo:
            maximo = depth
    return(maximo)

    
#print(maximum_depth([[], [[]], [], [[]]]))
#print(maximum_depth([[[], [], [[]]], [[]], [], [[]]]))
#print(maximum_depth([[[], [], [[]]], [[[[]]]]]))