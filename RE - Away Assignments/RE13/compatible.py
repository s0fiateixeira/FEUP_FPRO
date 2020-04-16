# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 11:44:02 2019

@author: Sofia
"""

def compatible(A, B):
    colunas_A = 0
    linhas_B = 0
    for i in range(len(A[0])):
        colunas_A += 1
    for i in range(len(B)):
        linhas_B += 1
    try:
        assert colunas_A == linhas_B, "A and B cannot be multiplied"
    except Exception as e:
        return(e)
    else:
        return("A and B can be multiplied")
    
    
#numero de colunas de A tem de ser o numero de linhas de b
    
    
#print(compatible([[2,2], [1,1]], [[5,5,5,5], [5,5,5,5]]))
#print(compatible([[1,2,2], [1,2,2]], [[1,2,3,4], [1,2,3,4]]))