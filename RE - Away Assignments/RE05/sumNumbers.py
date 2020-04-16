# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 11:45:20 2018

@author: Sofia
"""

def sum_numbers(n):
        for i in range(n):
            n=n+i
        return n

numero=int(input("Soma até ao número: "))
print (sum_numbers(numero))