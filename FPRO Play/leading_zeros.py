# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 17:46:55 2018

@author: Sofia
"""

def remove_leading(ip):
    t=ip.split(".")
    new = t[0]
    for i in range(1, len(t)):
        if (len(t[i]) == 1):
            new = new + "." + t[i]
        elif (len(t[i]) != 1) and (t[i][0] == "0"):
            new = new + "." + t[i][1:]
        elif (t[i][0] != "0"):
            new = new + "." + t[i]
    return(new)
        
    
    
    
    
    
    
    
#IPv4 = "255.024.01.01"

#IPv4 = "192.168.0.24"

#print(remove_leading(IPv4))