# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 12:52:57 2018

@author: Sofia
"""

def mastermind(g1, g2, g3, c1, c2, c3):
    points=0 
    if (g1==c1):
        points=points+3
    elif (g2!=c2) or (g3!=c3):
        if (g1==c2) or (g1==c3):
            points=points+1
            
    if (g2==c2):
        points=points+3
    elif (g1!=c1) or (g3!=c3):
        if (g2==c1) or (g2==c3):
            points=points+1
            
    if (g3==c3):
        points=points+3
    elif (g1!=c1) or (g2!=c2):
        if (g3==c1) or (g3==c2):
            points=points+1
    
    return points

user_guess1=input("Digite a primeira cor: ")
user_guess2=input("Digite a segunda cor: ")
user_guess3=input("Digite a terceira cor: ")
correct_key1=input("Digite a primeira cor da chave: ")
correct_key2=input("Digite a segunda cor da chave: ")
correct_key3=input("Digite a terceira cor da chave: ")
print (mastermind(user_guess1, user_guess2, user_guess3, correct_key1, correct_key2, correct_key3))
        