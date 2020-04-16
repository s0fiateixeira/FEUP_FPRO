#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 11:42:39 2018

@author: up201806629
"""

import turtle
number_sides = input ("Choose the number of sides: ")
length_side= input ("Choose the length of the side: ")
border_color= input ("Choose the border color: ")
fill_color= input ("Choose the fill color: ")

window=turtle.Screen()
pol=turtle.Turtle()

pol.begin_fill()
i=0
while i<(int(number_sides)): 
    pol.right(360/(int(number_sides)))
    pol.forward(int(length_side))
    pol.color(border_color)
    pol.fillcolor(fill_color)
    i=(i+1)
pol.end_fill()

turtle.done()
turtle.bye()