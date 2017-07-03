#Importing libraries
import time, datetime, os, csv

#define date
date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
tfile = open("/sys/bus/w1/devices/28-80000003962a/w1_slave")
text = tfile.read()
tfile.close()

#Convert data temp in degres
def convert_temp(file):
    temperature = 0
    if file is True:
        read_seconde_line = text.split("\n")[1] #Skip the first line
        tempData =  read_seconde_line.split(" ")[9] #Read only temp data
        temperature = float(tempData[2:]) #Get data
        temperature = temperature / 1000 #Transform data in degres temprature

convert_temp(tfile)

#Write in CSV file the temperature sensor
header = [
     [u'Date',
     u'Time',
     u'Data_temp']
]

values = []
values.append(date[0:10])
values.append(date[10:20])
values.append(float(temperature))

def write_csv(header, values):
    """
    Write all data in CSV files
    """
    with open('Data_temperature.csv', 'w') as files:
        writer = csv.writer((csvfile), delimiter=',')
        writer.writerows(header)
    for _ in values:
        writer.writerow(values)

    files.close()
    time.sleep(5)

write_csv(header, values)
