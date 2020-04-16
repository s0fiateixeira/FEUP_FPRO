# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 11:42:26 2019

@author: Sofia
"""

def count_exceptions(f, n1, n2):
    excepts = 0
    for i in range(n1, n2+1):
        try: f(i)
        except Exception:
            excepts +=1
    return(excepts)
    
    
    
#print(count_exceptions(lambda x: 1/(abs(x)-2), -5, 5))
#print(count_exceptions(lambda x: 1/0 if x > 10 else 0, 0, 50))