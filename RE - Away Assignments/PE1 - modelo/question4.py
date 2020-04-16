# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 16:20:54 2018

@author: Sofia
"""

LE= int(input("In-class assignments grade: "))
RE= int(input("Away assignments grade: "))
PE= int(input("Practical on compuer tests grade: "))
TE= int(input("Final theory test grade: "))


if (LE<0 or LE>100 or RE<0 or RE>100 or PE<0 or PE>100 or TE<0 or TE>100):
    print ("Input error")
elif PE<40 or TE<40:
    print ("RFC")
else:
    grade = int((LE + RE + 4 * PE + 4 * TE) / 50)
    print(grade)