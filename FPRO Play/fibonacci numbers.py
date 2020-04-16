# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 21:31:55 2018

@author: Sofia
"""

def fib(n):
    resposta = list([])
    numero = 0
    if n == 0:
        resposta = resposta + list([0])
        numero += 0
    elif n == 1:
        resposta = resposta + list([1])
        numero += 1
    else:
        count = n
        while numero != 0:
            numero += n + numero
            resposta = list([fib(n-1) + fib(n-2)])
            count -= 1
    return(resposta)
        
        
print(fib(5))