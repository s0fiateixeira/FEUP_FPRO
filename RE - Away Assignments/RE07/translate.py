# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 11:43:12 2018

@author: Sofia
"""

def translate (astring, table):
    new=""
#    new=new+str(table[4][1])
#    print(new)
    for i in range (len(astring)):
        for j in range (len(table)):
            if (str(table[j][0])==astring[i]):
                new=new+str(table[j][1])
                break
        if (str(table[j][0])!=astring[i]):
            new=new+astring[i]
    return(new)
    
    
#frase="Hello world!"
#tabela=(('a', 1), ('e', 2), ('i', 3),('o', 4), ('u', 5), ('!', ' :)'))
    
#frase="Testing this string..."
#tabela=((' ', '--'), ('.','!'), ('i', 'o'), ('t', 'tt'))
#print(translate(frase, tabela))