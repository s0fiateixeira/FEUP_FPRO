# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 20:03:08 2018

@author: Sofia
"""

def sparse_dot_product(dict1, dict2):
    soma = 0
    for key, value in dict1.items():
        for keys, values in dict2.items():
            if key == keys:
                soma += value*values
    return(soma)
    
    
#d1 = {1: 3, 7: 1}
#d2 = {1: 3, 7: 1}

#d1 = {0: 1, 1: 1}
#d2 = {2: 1, 3: 1}

#print(sparse_dot_product(d1, d2))