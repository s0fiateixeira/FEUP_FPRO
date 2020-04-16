# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 20:33:06 2018

@author: Sofia
"""

def roman_to_integer(astring):
    roman_values = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    total = 0
    for i in range(1, len(astring)):
        if (roman_values[astring[i-1]]) >= (roman_values[astring[i]]):
            total += roman_values[astring[i-1]]
        else:
            total -= roman_values[astring[i-1]]
    return(total)
    
    
frase = 'XV'
#frase = 'LXXXIV'
#frase = 'XLIII'
#frase = 'MMMCMXCIX'

print(roman_to_integer(frase))