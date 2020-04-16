#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 17:24:42 2018

@author: exame
"""

tS=float(input("What is the swimming time? "))
tC=float(input("What is the cycling time? "))
tR=float(input("What is the running time? "))

time=(tS+tC+tR)%60
S_velo=1.5/tS
C_velo=40/tC
R_velo=10/tR

if (time>4.0):
    print("Time")
elif (S_velo<2):
    print("Swimming")
elif (C_velo<20):
    print("Cycling")
elif (R_velo<8):
    print("Running")
else:
    print(time)