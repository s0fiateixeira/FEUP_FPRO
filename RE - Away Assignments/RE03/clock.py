# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 16:35:22 2018

@author: Sofia
"""

import turtle
window=turtle.Screen()
window.bgcolor("lightgreen")
relogio=turtle.Turtle()
relogio.shape("turtle")
relogio.color("blue")
relogio.pensize(3)


for angulo in range(0,12):
    relogio.penup()
    relogio.forward(100)
    relogio.pendown()
    relogio.forward(10)
    relogio.penup()
    relogio.forward(20)
    relogio.stamp()
    relogio.backward(130)
    relogio.pendown()
    relogio.right(360/12)
    
turtle.done()
turtle.bye()