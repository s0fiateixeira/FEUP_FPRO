# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 13:04:44 2018

@author: Sofia
"""
def get_positions(word_list, sentence):
    
    for i in range (3):
        for j in range (3):
            if i != j:
                if word_list[j] + " " + word_list[i] == sentence:
                    result = str(j) + " " + str(i)
    return result


lista=["hello", "world", "lousy"]              
frase="lousy world"
print(get_positions(lista,frase))