#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 22:09:18 2017

@author: vincent
"""

#Importing libraries
import time, datetime, os, csv, sys

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

hd = True
while True:
    try:
        #define date
        date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        tfile = open("/sys/bus/w1/devices/28-8000002712a5/w1_slave")
        text = tfile.read()
        tfile.close()

        #Convert data temp in degres
        read_seconde_line = text.split("\n")[1] #Skip the first line
        tempData =  read_seconde_line.split(" ")[9] #Read only temp data
        temperature = float(tempData[2:]) #Get data
        temperature = temperature / 1000 #Transform data in degres temprature

        #Write in CSV file the temperature sensor
        header = [[u'Date', u'Time', u'Temperature']]

        values = []
        values.append(date[0:10])
        values.append(date[10:20])
        values.append(float(temperature))

            files = open('Data_temperature.csv', 'a')
            writer = csv.writer((files), delimiter=',')
            if hd == True:
                writer.writerows(header)
                hd = False
            writer.writerow(values)
            #If temperature it's get with success or not :
            if temperature is not None:
                #print the temperature on the console
                print('Temp={0:0.1f} C°'.format(temperature))
                time.sleep(300)
                files.close()
            else:
                print('Failed to get reading. Try again!')
                sys.exit(1)

    except KeyboardInterrupt:
        #add the date to the name file
        os.system('mv Data_temperature.csv Data_temperature_'+ (str(date[0:10])) +'.csv')
        #made secure copy thanks to scp to the raspberry server
        os.system('scp Data_temperature'+ (str(date[0:10])) +'.csv pi@192.168.1.13:/home/pi/hyculture/captemp_files')
        print('Done !')
        print('Delete previous file ...')
        #delete the current file
        os.system('rm Data_temperature'+ (str(date[0:10])) +'.csv')
        print('Done !')
        quit()
