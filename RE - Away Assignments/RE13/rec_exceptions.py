# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 11:44:47 2019

@author: Sofia
"""

def rec_exceptions(l):
    result = []
    for i in range(len(l)):
        try:
            f = l[i]
            res = f()
        except Exception as e:
            result.append(e)
        else:
            result += rec_exceptions(res)
    return(result)



#print(rec_exceptions([lambda: 1/0]))
#print(rec_exceptions([lambda: [lambda: [1,2,3].index(-1), lambda:''[2]], lambda: [1,2,3][4], lambda: [lambda: [lambda: 1/0]]]))