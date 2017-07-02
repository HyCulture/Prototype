#Importing libraries
import time, datetime, os, csv

#define date
date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
tfile = open("/sys/bus/w1/devices/28-80000003962a/w1_slave")
text = tfile.read()
tfile.close()

#Write in CSV file if the temperature sensor is active
if tfile is True:
    read_seconde_line = text.split("\n")[1] #Skip the first line
    tempData =  read_seconde_line.split(" ")[9] #Read only temp data
    temperature = float(tempData[2:]) #Get data
    temperature = temperature / 1000 #Transform data in degres temprature
else :
    return False


header = [
     u'Date',
     u'Time',
     u'Data_temp',
]

values = [
     [u'date', u'date', u'temperature']
]

def write_csv(header, values):
    """
    Write all data in CSV files
    """
    files = open('Data_temperature.csv', 'w')
    ligneHeader = ";".join(header) + "\n"
    files.write(ligneHeader)
    for _ in values:
        ligne = ";".join(values) + "\n"
        files.write(ligne)

    files.close()
    time.sleep(5)

write_csv(header, values)
