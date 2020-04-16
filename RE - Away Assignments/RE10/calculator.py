# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 11:43:13 2018

@author: Sofia
"""

# calculator( ((1, '+', (9, '*', 2)), '-', 3) )

# calculator( 1, '+', (9, '*', 2)) + calculator(3)

# calculator( 1) + calculator((9, '*', 2) + 3


def calculator(expr):
    # condição base
    if expr.__class__ == int:
        return(expr)
    
    a, op, b = expr
    a = calculator(a)
    b = calculator(b)

    if op == "+":
        return(a+b)
    elif op == "-":
        return(a-b)
    elif op == "*":
        return(a*b)
    elif op == "/":
        return(a/b)
    
    
    
    
    
#operacao = (1, '+', 2)
#operacao = ((1, '+', 2), '*', 3)

#print(calculator(operacao))