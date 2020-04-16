# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 11:40:28 2018

@author: Sofia
"""

#   flatten('Hello' + flatten([2, [[], False]]) + flatten([True]))
#   flatten('Hello' + 2 + flatten([], False) + True)
#   flatten('Hello' + 2 + flatten([]) + False + True)
#   flatten('Hello' + 2 + "" + False + True)


def flatten(alist):
    new = list([])
    apendices = list([])
    for i in range(len(alist)):
        if alist[i].__class__ != list:
            new.append(alist[i])
        else:
            apendices += flatten(alist[i])
    return(new + apendices)    
    

    
#lista = ['Hello', [2, [[], False]], [True]]
#lista = [[]]
#lista = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

#print(flatten(lista))