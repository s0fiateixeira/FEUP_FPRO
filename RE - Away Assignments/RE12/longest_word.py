# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 11:40:48 2018

@author: Sofia
"""

def longest_word(url):
    import urllib.request
    response = urllib.request.urlopen(url)
    html = response.read().decode()
    
    import urllib.request
    response = urllib.request.urlopen(" https://raw.githubusercontent.com/fpro-admin/recitas/master/words")
    content = response.read().decode()
    
    
    
#    content = open("words", "r")
#    content = content.read()

#    words_url = set(html.split())
#    words_dict = set(content.split())
#    words = words_url.intersection(words_dict)
#    max_len = len(max(words, key = len))
#    word = [w for w in words of len(w) == max_len]
#    return(word)
    
    maximo = 0
    palavra_maior = ""
    text = set(html.split())
    words_dict = set(content.split())
    palavras = text.intersection(words_dict)
    for i in range(len(text)):
        if len(palavras[i]) > maximo:
            maximo = len(palavras[i])
            palavra_maior = palavras[i]
        elif len(palavras[i]) == maximo:
            pass
    return(palavra_maior)
            
            
            
            
#print(longest_word("https://en.wikipedia.org/wiki/Monty_Python"))

#print(longest_word("https://web.fe.up.pt/~jlopes/doku.php/teach/fpro/sheet"))

print(longest_word("https://raw.githubusercontent.com/fpro-admin/recitas/master/shakespeare.txt"))