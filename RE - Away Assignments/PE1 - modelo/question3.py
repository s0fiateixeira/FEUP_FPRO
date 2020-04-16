# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 16:20:44 2018

@author: Sofia
"""

num=float(input("Escolha um número: "))

if num==0:
    root=0
else:
    aproximation=num/2
    root=(aproximation+(num/aproximation))/2.0
    
    while (int(root*100)) != (int(aproximation*100)):
        aproximation=root
        root=(root+(num/root))/2.0
        
    print()
    print("%.3f"% root)