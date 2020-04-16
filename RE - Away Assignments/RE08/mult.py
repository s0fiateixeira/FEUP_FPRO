# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 17:53:30 2018

@author: Sofia
"""

def mult(M, N):
    result=[[0 for row in range(len(N[0]))] for col in range(len(M))]
    for i in range (len(M)):
        if len(N[i])>len(M):
            return([])
        else:
            for j in range (len(N[0])):
                for h in range (len(N)):
                    result[i][j]+=(M[i][h])*(N[h][j])
    return(result)
    
    
mm=[[1, 2], [3, 4]]
nn=[[2, 0], [1, 2]]

#mm=[[1, 2, 3], [4, 5, 6]]
#nn=[[9], [8], [7]]

#mm=[[7, 8, 9, 10]]
#nn= [[5], [3], [2], [7]]

print(mult(mm, nn))