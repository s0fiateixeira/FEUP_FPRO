#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 17:41:11 2018

@author: exame
"""

def treasure(clues):
    
#    that receives a dictionary of clues where each key
#    is a location and each value is a clue of what is
#    the next location to go
    location = list(clues.keys())
    clue = list(clues.values())
    print(location)
#    for i in range(len(location)):
#            print(location(i))
    
    
    
print(treasure({(0,0): (1,0), (1,0): (2,0), (2,0): (3,0)}))
#print(treasure({(0,0): (1,0), (2,1): (3,5), (1,0): (2,1)}))
#print(treasure({(0,0): (5,6), (7,8): (6,7), (5,6): (6,7), (6,7):(7,8)}))
#print(trasure({(-1,1): (0,0), (0,0): (1,0), (1,0): (-1,1)}))