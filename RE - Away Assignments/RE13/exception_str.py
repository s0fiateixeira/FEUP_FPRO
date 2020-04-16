# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 19:28:04 2019

@author: Sofia
"""


def exception_str(f):
    try:
        f()
    except Exception as e:
        return(e)
    else:
        return("No exception was raised")
    
    
#print(exception_str(lambda: 1/0))
#print(exception_str(lambda: 0))