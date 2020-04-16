# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 11:43:27 2018

@author: Sofia
"""
#file_finder("dirs")
#file_finder("home")
#file_finder("Documents", "Downloads", "tmp.txt", "page.html")
    # Documents - file_finder("FPRO", "Python")
    # Downloads - file_finder("Movies")
            # Movies - file_finder("TV Series", "l.avi")
####################################################################

def file_finder(dirs, file_name):
    path = ""
    if file_name in dirs:
        return(path)
    
    
        for i in range(len(dirs)):
            pasta = dirs[i][0]
            novo = file_finder(pasta, file_name)
            path += str(dirs[i][0]) + "/" + novo
        return(path)

###########################################################

    new = list([])
    apendices = list([])
    for i in range(len(alist)):
        if alist[i].__class__ != list:
            new.append(alist[i])
        else:
            apendices += flatten(alist[i])
    return(new + apendices)

###########################################################

dirs = ["home",
            ["Documents",
                 [ "FPRO", "lists.txt", "recursion.pdf", "functions" ],
                 [ "Python", "hello_world.py", "readme.md" ],
            ],
            ["Downloads",
                [ "Movies",
                      [ "TV Series", "BreakingBad.mp4", "TheBigBangTheory.avi" ],
                      "1.avi", "22", "001.mp4"
                ],
            ],
            "tmp.txt", "page.html"
        ]
    
    
#procurar = "Documents"
procurar = 'recursion.pdf'
print(file_finder(dirs, procurar))