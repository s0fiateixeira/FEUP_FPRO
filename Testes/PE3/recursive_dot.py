#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 17:12:15 2018

@author: exame
"""

def recursive_dot(l1, l2):
#Write a function recursive_dot(l1, l2) that computes the inner dot product
#using the two lists provided — the two lists follow the same structure.
#   For example, if l1=[1, [2, 3]] and l2=[4, [5, 6]], then the result will
#   be 1*4+(2*5+3*6).
#    You might want to use type(x) to find the type of x.
    soma = 0
    for i in range(len(l1)):
        if (l1[i]).__class__.__name__ == "int":
            soma += l1[i]*l2[i]
        else:
            lista1 = l1[i]
            lista2 = l2[i]
            soma += recursive_dot(lista1, lista2)
    return(soma)
    
    
#print(recursive_dot([1, [2, 3]], [4, [5, 6]]))
#print(recursive_dot([[5, 3, 1], [2, 4]], [[4, 2, 0], [1, 3]]))
#      recursive_dot([5, 3, 1], [4, 2, 0])
#      recursive_dot(5*4 + 3*2 + 1*0)
#      
#      recursive_dot([2, 4], [1, 3])
#      recursive_dot(2*1+4*3)
#print(recursive_dot([2], [1]))
#print(recursive_dot([-2, [-5, 6], [13]], [4, [1, 2], [-1]]))