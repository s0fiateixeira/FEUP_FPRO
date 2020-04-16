# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 11:40:11 2018

@author: Sofia
"""

def wc(filename):
    file = open(filename, "r")
    file = file.read()
    n_c=0
    n_words=0
    n_sentences=0
    words = file.split()
    sentences = file.split("\n")
    for i in range(len(sentences)):
        n_sentences += 1
    for i in range(len(words)):
        n_words += 1
    for i in range(len(file)):
        n_c += 1
    return(n_sentences, n_words , n_c)
    
    
    

#print(wc("shakespeare.txt"))
#    
#print(wc("monty.txt"))