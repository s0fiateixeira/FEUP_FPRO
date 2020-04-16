# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 11:55:03 2018

@author: Sofia
"""

def is_perfect(n):
    if n<0:
        print("Error! It needs to be a positive integer!")
    else:
        sum = 0
        for x in range(1, n):
            if n % x == 0:
                sum += x
        return sum == n

#a perfect number is a positive integer that is equal to the sum of its proper
#positive divisors, that is, the sum of its positive divisors excluding the number itself. 
  
numero=int(input("Escolha um número: "))
print (is_perfect(numero))