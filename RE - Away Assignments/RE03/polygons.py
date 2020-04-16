#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 11:44:47 2018

@author: up201806629
"""


import turtle
window=turtle.Screen()
pol=turtle.Turtle()
for sides in [4, 3, 6, 8]: 
    i=0
    while i<=(sides-1): 
        pol.forward(50)
        pol.right(360/sides)
        i=(i+1)
    pol.penup()
    pol.forward(150)
    pol.pendown()
        
turtle.done()
turtle.bye()