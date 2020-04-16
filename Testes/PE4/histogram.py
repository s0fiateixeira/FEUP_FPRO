#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 15:17:14 2019

@author: exame
"""

def  histogram(alist, bins):
    bins = list(bins)
    frequency_1 = 0
    frequency_2 = 0
    frequency_3 = 0
    result = list([])
    for i in range(len(alist)):
        if alist[i] >= 0 and alist[i] < 3:
            frequency_1 += 1
        elif alist[i] >= 3 and alist[i] < 7:
            frequency_2 += 1
        elif alist[i] >= 7 and alist[i] < 12:
            frequency_3 += 1
    result.append(frequency_1)
    result.append(frequency_2)
    result.append(frequency_3)
    return(result)
    
    
    
#print(histogram([1, 1, 1, 4, 5, 8, 10], (0, 3, 7, 12)))
#print(histogram([0, 3, 4, 7, 8, 1, 5], (0, 3, 7, 12)))
#print(histogram([3, 0, 1, 5, 3, 2], (0, 3, 6)))