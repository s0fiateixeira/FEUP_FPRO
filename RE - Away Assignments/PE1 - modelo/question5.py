# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 16:21:06 2018

@author: Sofia
"""

lower=int(input("What is the lowest number? "))
upper= int(input("What is the highest number? "))

print("Prime numbers between",lower,"and",upper,"are:")

for num in range(lower,upper + 1):
   # prime numbers are greater than 1
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)