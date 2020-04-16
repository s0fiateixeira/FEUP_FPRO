# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 15:20:59 2018

@author: Sofia
"""

n1=int(input("Insira o primeiro número: "))
n2=int(input("Insira o segundo número: "))

casas_decimais=0
num2=n2
#Conta o número de casas decimais do segundo número
while num2!=0:
    num2=num2//10
    casas_decimais=casas_decimais+1
    
#Acrescenta 10^nºcasas_decimais ao primeiro número (fica com zeros nesse local) e depois soma o valor do segundo
result = ((n1*(10**casas_decimais))+n2)
print(result)