# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 11:42:01 2018

@author: Sofia
"""

def unique(atuple):
    atuple=tuple(sorted(atuple))
#    new=tuple()
    new=tuple([atuple[0]])
    for i in range (1, len(atuple)):
        if atuple[i] != atuple[i-1]:
            new=new+tuple([atuple[i]])
#        elif atuple[i]==atuple[i-1]:
#            new=new+tuple([atuple[i]])
#            break
    new=tuple(sorted(new))
    return (new)
    
tuplo=(8, 8, 1, 3, 1, 3, 5)
print(unique(tuplo))