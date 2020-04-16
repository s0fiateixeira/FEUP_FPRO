# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 11:43:48 2018

@author: Sofia
"""

def sort_grades(records):
    new=tuple()
#    letras=""
    media_ant=0
    for i in range (len(records)):
        media=(int(records[i][2][0])+int(records[i][2][1]))/2
        if media < media_ant:
            continue
        elif media > media_ant:
            new = new + tuple((records[i]))
            media_ant=media
        elif media < media_ant:
            new = new
    return(new)
#        elif media==media_ant:
#            for j in range (len(records)):
#                letras=letras+records[i][j][0]
#                alfabeto=tuple(sorted(letras))
#                for z in range(alfabeto):
#                    new = new + records[i][j][z]
#    return(new)
    
    
    
    
    
    
#notas=(('João', 'up20186042', (90, 87)),('Ana', 'up20186040', (90, 90)),('José', 'up20186063', (70, 90)),('Ana', 'up20186061', (90, 90)),('Tiago', 'up20186070', (100, 90)))

notas=(('Maria', 'up20190001', (60, 70, 80)),('Maria', 'up20190002', (60, 70, 80)),('Mario', 'up20190003', (100, 10, 80)),('Rui', 'up20190004', (90, 100, 90)),('Ana', 'up20190005', (90, 100, 90)))

print(sort_grades(notas))