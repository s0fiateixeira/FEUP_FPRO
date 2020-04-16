#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 17:46:52 2018

@author: exame
"""

dec=int(input("Choose a number: "))

octal=0
n=0
while dec//10!=0:
    n=n+1
    octal=n+dec//8
    dec=dec//10

print(octal)