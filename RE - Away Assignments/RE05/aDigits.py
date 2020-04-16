# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 12:38:06 2018

@author: Sofia
"""

def adigits(num1, num2, num3):
    n1=int(num1)
    n2=int(num2)
    n3=int(num3)
    while (n1>=n2 and n1>=n3):
        if n2>=n3:
            n1=n1*100
            n2=n2*10
            final=n1+n2+n3
        else:
            n1=n1*100
            n3=n3*10
            final=n1+n2+n3
        return final
    
    while (n2>=n1 and n2>=n3):
        if n1>=n3:
            n2=n2*100
            n1=n1*10
            final=n1+n2+n3
        else:
            n2=n2*100
            n3=n3*10
            final=n1+n2+n3
        return final
    
    while (n3>=n2 and n3>=n1):
        if n1>=n2:
            n3=n3*100
            n1=n1*10
            final=n1+n2+n3
        else:
            n3=n3*100
            n2=n2*10
            final=n1+n2+n3
        return final

numero1=int(input("Escolha o primeiro número: "))
numero2=int(input("Escolha o segundo número: "))
numero3=int(input("Escolha o terceiro número: "))
print (adigits(numero1, numero2, numero3))
    
