# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 17:13:26 2019

@author: Sofia
"""

def dogs(h_age):
    if h_age <= 2:
        dog_age = (h_age // 10,5)
    else:
        dog_age = 21
        for i in range(2, h_age):
            dog_age += (h_age // 4)
    return(dog_age)
    
    
print(dogs(1))