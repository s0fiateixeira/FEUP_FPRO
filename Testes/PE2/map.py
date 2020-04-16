# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def map(pos, steps):
    x = pos[0]
    y = pos[1]
    steps = steps.split("-")
    for i in range(len(steps)):
        if steps[i] == "up":
            y += 1
        elif steps[i] == "down":
            y -= 1
        elif steps[i] == "left":
            x -= 1
        elif steps[i] == "right":
            x += 1
    return(tuple([x,y]))
    
    
    
    
    
#ppos=(0,0)
#ssteps="up-up-left-right-up-up"

#ppos=(0,4)
#ssteps="up-up-left-left-up-up"

#print(map(ppos, ssteps))