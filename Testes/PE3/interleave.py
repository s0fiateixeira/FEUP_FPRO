#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 17:12:15 2018

@author: exame
"""

def interleave(alist1, alist2):
    if len(alist1) <= len(alist2):
        comp = len(alist1)
    else:
        comp = len(alist2)
    if alist1 == list([]) or alist2 == list([]):
        return(list([]))
        
    final = list([])
    for i in range(comp):
        if (alist1[i]).__class__.__name__ != "list":
            final.append(alist1[i])
            final.append(alist2[i])
        else:
            lista1 = alist1[i]
            lista2 = alist2[i]
            final += (interleave(lista1, lista2))
    return(final)
        
        
        
        
#print(interleave([1, [4,2]], [3, [7,4]]))
#print(interleave(['a','b','c'], [1,2,3,4,5]))
#print(interleave([], [1,2]))
#print(interleave([1, ['a', 'b'], 2], [3, [True, False], 4]))
#            correta     [1, 3, 'a', True, 'b', False, 2, 4]
#            minha       [1, 3, ['a', True, 'b', False], 2, 4]