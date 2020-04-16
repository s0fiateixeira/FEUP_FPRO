# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 17:54:04 2018

@author: Sofia
"""

def local_minima(alist, n):
    result = []
    for i in range(n//2, len(alist)-n//2):
        viz = []
        for j in range(1, n//2):
            viz += [i-j, i+j]
            n = len(viz)
            count = 0
            for k in viz:
                if alist[i] <= alist[k]:
                    count += 1
            if count == n:
                for l in range(len(result)-n//2, len(result)-1):
                    if alist[i] != result[l][0]:
                        result += [(alist[i], i)]
                        break
    return (result)
    
    
    
    
    
lista = [10, 3, 3, 14, 5, 7, 4]
numero = 3

#lista = [0, 3, 3, 14, 5, 7, 4]
#numero = 3

#lista = [2, 1, 1, 1, 7, 3, 1]
#numero = 5

print(local_minima(lista, numero))