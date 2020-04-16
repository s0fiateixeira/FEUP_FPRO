# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 12:06:56 2018

@author: Sofia
"""

def count(word, phrase):
    resultado=0
    phrase=phrase.upper()
    word=word.upper()
    dividir=phrase.split()
    for i in range ((len(dividir))-2):
        if (word in dividir[i])==True:
            resultado=resultado+1
        else:
            resultado=resultado+0
    return(resultado)
    
    
    
#frase=input("Write a sentence: ")
#palavra=input("Write a word: ")
#print(count(palavra, frase))