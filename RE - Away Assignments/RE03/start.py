# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 16:55:59 2018

@author: Sofia
"""

import turtle
lados=int(input("Escolha o número de lados: "))

window=turtle.Screen()
window.bgcolor("blue")
estrela=turtle.Turtle()
estrela.color("white")
estrela.shape("circle")
estrela.pensize(3)
    
for repeticoes in range(0,lados):
    estrela.forward(150)
    estrela.stamp()
    estrela.backward(150)
    estrela.right(360/lados)
    
turtle.done()
turtle.bye()