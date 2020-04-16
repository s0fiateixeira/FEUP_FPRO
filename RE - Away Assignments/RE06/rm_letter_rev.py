# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 11:41:14 2018

@author: Sofia
"""

def rm_letter_rev(l, astr):
    reverse=(astr[::-1])
    s=""
    for i in range (len(reverse)):
        if reverse[i] != l :
            s=s+reverse[i]
            i=i+1
            
    return(s)
            
    
#letter=input("Which letter do you want to remove? ")
#sentence=input("Write a sentence: ")
#print(rm_letter_rev(letter, sentence))