# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 16:57:25 2019

@author: Sofia
"""

def alarm(hour, minutes):
    alarm_minutes = (minutes + 51)%60
    minutes_to_hour = (minutes + 51)//60
    alarm_hour = (hour + 6)%24 + minutes_to_hour
    return(str(alarm_hour) + ":" + str(alarm_minutes))
    
    
#print(alarm(5, 10))