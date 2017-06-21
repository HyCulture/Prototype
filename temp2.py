import time
import datetime

while True :
	"""
	Permet de récupérer les données du capteur de température
	"""
	date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	tfile = open("/sys/bus/w1/devices/28-80000003962a/w1_slave")
	text = tfile.read()
	tfile.close()
	secondline = text.split("\n")[1]
	temperaturedata = secondline.split(" ")[9]
	temperature = float(temperaturedata[2:])
	temperature = temperature / 1000
	fichier = open("Temperatures.txt", "a")
	fichier.write(str(date)+"   ")
	fichier.write(str(temperature)+'\r\n')
	fichier.close()
	time.sleep(5)
