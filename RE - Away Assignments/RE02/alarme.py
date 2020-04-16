# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import datetime
tempo = datetime.datetime.now()
print (tempo.strftime("%H:%M"))
minutos = (tempo.minute + 30)%60
horas = (tempo.hour + 8 +(tempo.minute + 30)//60)%24
print (str (horas) + ":" + str(minutos))
