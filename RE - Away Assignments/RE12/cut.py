# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 11:40:36 2018

@author: Sofia
"""

def cut(filename, delimiter, field):
    file = open(filename, "r")
    file = file.read()
    linhas = file.split("\n")
    result = str(field)
#    print(linhas)
#    print(linhas[0][2])
    for i in range(len(linhas)):
        linha = (linhas[i]).split(",")
        result += "\n" + str(linha[field])
    return(result)
    
    
    
    

print(cut("data.csv", ", ", 2))
#
#print(cut("data.csv", ", ", [2,4]))