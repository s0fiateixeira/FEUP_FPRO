# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 15:19:42 2018

@author: Sofia
"""

side1=int(input("Escolha o primeiro lado: "))
side2=int(input("Escolha o segundo lado: "))
side3=int(input("Escolha o terceiro lado: "))

if ((side1+side2<=side3)or(side2+side3<=side1)or(side1+side3<=side2)):
    result="Not a triangle"
    print(result)
    pass
elif (side1==side2 and side2==side3):
    result="Equilateral"
    print(result)
elif (side1!=side2 and side2!=side3):
    result="Scalene"
    print(result)
else:
    result="Isosceles"
    print(result)