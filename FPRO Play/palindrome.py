# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 18:20:34 2018

@author: Sofia
"""
#_________PROGRAMA QUE EU FIZ_________
#
#def palindrome(astring):
#    n_pal=0
#    for i in range(len(astring)+1):
#        if i == astring.index(astring[-1]):
#            return(n_pal)
#        elif astring[i-1] == astring [i+1]:
#            n_pal = n_pal+1


#_________PROGRAMA QUE EU ENCONTREI NA NET_________
    

def palindrome(astring):

    def check_palin(word):
        for i in range(int(len(word)/2)):
            if word[i] != word[-1*(i+1)]:
                return False
        return True

    left = 0
    right = len(astring)
    j=right
    results=[]

    while left < (right-1):
        temp = astring[left:j] #Time complexity O(k)
        j -= 1

        if check_palin(temp):
            results.append(temp)

        if j<left+2:
            left+=1
            j=right

    return ("For string " + "'" + astring + "': " + str(len(list(results))) + " palindrome substrings")



string = "geek"

#string = "ababa"

print(palindrome(string))