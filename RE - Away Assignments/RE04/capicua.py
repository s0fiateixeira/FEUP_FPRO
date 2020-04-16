# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 15:21:25 2018

@author: Sofia
"""

num=int(input("Insira um número: "))

numero=num
inverso=0
while numero != 0:
#   O digito da direita é encontrado
    digito_direita=numero%10
#   O inverso vai ser o inverso anterior mais o último dígito
    inverso=(inverso*10)+digito_direita
#   Tira o último dígito ao número para que seja completado o ciclo
    numero=numero//10
if num==inverso:
    print(num, "is a palindrome")
else:
    print(num, "is not a palindrome")