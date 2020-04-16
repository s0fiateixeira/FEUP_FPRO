# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 11:43:35 2018

@author: Sofia
"""

def triplet(atuple):
    result=tuple()
#    new=tuple(sorted(atuple))
#    if (len(new)) > 2:
    r=len(atuple)-1
    for i in range (len(atuple)-2):
            l = i+1
            while (l < r):
                sum= int(atuple[i]) + int(atuple[l]) + int(atuple[r])
                if (sum < 0):
                    l = l + 1
                if (sum > 0):
                    r = r - 1
                if (sum == 0): 
                    result=tuple([atuple[i]]+[atuple[l]]+[atuple[r]])
                    l= l + 1
    return(result)
#    else:
#        return("ERROR! The tupple needs more than 3 integers!!")
    
    
    
    
#tuplo=(-8, 0, 4, -2, -1, 1, 2)
#tuplo=(-1, 1, 1, 1)
tuplo=(-4, 3, 0, -2, -1, -3)

print(triplet(tuplo))