# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

num=int(input("Write a number: "))

if num//1000!=0:
    print("Invalid number! Write a number with 3 digits only!!!")
    
else:
    dig1=num%10
    dig2=(((num%100)-dig1)//10)
    dig3=((((num%1000)-dig1)//10)-dig2)//10 
    armstrong=(dig1**3)+(dig2**3)+(dig3**3)
    if num==armstrong:
        print("True")
    else:
        print("False")