from picamera import PiCamera
from gpiozero import DistanceSensor, LED, Buzzer
from time import sleep
from datetime import datetime

camera = PiCamera()
camera.rotation = 180

azul = LED (25)
som = Buzzer(24)

sensor = DistanceSensor (echo=18, trigger=23, max_distance=0.5)

def fotografar():
	azul.on()
	som.on()
	
	hora = datetime.now()
	camera.capture (str(hora) + ".jpg")
	print ("Foto capturada: " + str(hora))
	
	sleep(0.5)
	azul.off()
	som.off()

sleep (1)

while True:
	sensor.wait_for_in_range()
	fotografar()
