# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 15:54:30 2018

@author: Sofia
"""

p = 1000
r1= float(input("What is the first interest rate? "))
n1= float(input ("What is the first frequency that the interest is paid out (per year)? "))
r2= float(input("What is the second interest rate? "))
n2= float(input ("What is the second frequency that the interest is paid out (per year)? "))
t= 1

a1 = (p*((1+(r1/n1))**(n1*t)))
a2 = (p*((1+(r2/n2))**(n2*t)))

if a1>a2:
   print("The first final amount (",a1, ") is higher then the second(",a2,").") 
elif a2>a1:
    print("The second final amount (",a2,") is higher then the first(",a1,").") 
elif a1==a2:
    print("The final amounts are equal (",a1,"=",a2,").") 