# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 15:18:21 2018

@author: Sofia
"""

n=int(input("Insira um número: "))
result=""
for i in range (0,n+1):
    if (i % 3) == 0 and (i % 5) == 0:
        result=result+" "
    elif (i % 3) == 0:
        result=result+"Fizz "
    elif (i % 5) == 0:
        result=result+"Buzz "
    else:
        result=result+str(i)+" "

print(result)