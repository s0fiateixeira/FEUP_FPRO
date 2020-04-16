# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 11:42:39 2018

@author: Sofia
"""

def find_dtype(atuple, data_type):
    new=tuple()
#    print((atuple[0]).__class__.__name__)
#    print(data_type.__name__)
    for i in range (len(atuple)):
        if (atuple[i]).__class__.__name__==data_type:
            new=new+tuple([atuple[i]])
        else:
            new=new+tuple()
    return(new)

tuplo=tuple((0, 1, 1j, "string"))
tipo="complex"
print(find_dtype(tuplo, tipo))
  
            