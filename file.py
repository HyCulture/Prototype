#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 22:09:18 2017

@author: vincent
"""

#Importing libraries
import time, datetime, os, csv, sys
import os.path
from NewLine import WriteLine

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

while True:
    try:
        #define date
        date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        tfile = open("w1_slave.txt")
        text = tfile.read()
        tfile.close()
        
        #Convert data temp in degres
        read_seconde_line = text.split("\n")[1] #Skip the first line
        tempData =  read_seconde_line.split(" ")[9] #Read only temp data
        temperature = float(tempData[2:]) #Get data
        temperature = temperature / 1000 #Transform data in degres temprature
        
        #Write in CSV file the temperature sensor
        header = [[u'Date', u'Time', u'Data_temp']]
        
        values = []
        values.append(date[0:10])
        values.append(date[10:20])
        values.append(float(temperature))
        if os.path.exist(Data_temperature.csv):
            open('Data_temperature.csv', 'w') as files:
            writer = csv.writer((files), delimiter=',')
            writer.writerows(header)
            writer.writerow(values)
            WriteLine(values)
            #If temperature it's get with success or not :
            if temperature is not None:
                print('Temp={0:0.1f} C°'.format(temperature))
                time.sleep(10)
            else:
                print('Failed to get reading. Try again!')
                sys.exit(1)
        files.close()
                   
    except KeyboardInterrupt:
        quit()
