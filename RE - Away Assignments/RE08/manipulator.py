# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 17:53:43 2018

@author: Sofia
"""

def manipulator(l, cmds):
    new = []
    lista = []
    for i in range(len(cmds)):
        if "insert" in cmds:
            lista.insert(int(cmds[7]), int(cmds[9:]))
            if (i+1) == "print":
                new.append(lista)
        if "remove" in cmds:
            lista.remove(int(cmds[7:]))
        if cmds[i][:6]=="append":
            l.insert(-1, cmds[i][:6])
        if cmds[i]=="sort":
            sorted(str(l))
        if cmds[i]=="pop":
            l = l.pop()
        if cmds[i]=="reverse":
            l = l.reverse()
        if cmds[i]=="print":
            new = new + str(l)
    return(new)
    
    
    
    
ll= []
cmdss= ["insert 0 5", "insert 1 10", "insert 0 6", "print", "remove 6", "append 9", "append 1", "sort", "print", "pop", "reverse", "print"]

#ll= [2, 4]
#cmdss= ["print", "remove 4", "append 1", "sort", "print", "pop", "reverse", "print"]

#ll=[]
#cmdss=["print"]

print(manipulator(ll, cmdss))