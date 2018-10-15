from picamera import PiCamera
from gpiozero import DistanceSensor, LED, Buzzer
from time import sleep
from datetime import datetime

camera = PiCamera()

azul = LED (25)
som = Buzzer()

sensor = DistanceSensor (echo=18, trigger=23, max_distance=0.5)

def fotografar():
	
	azul.on()
	som.beep()
	
	hora = datetime.now()
	camera.capture (str(hora) + ".jpg")
	print ("Foto capturada: " + str(hora))
	
	azul.off()

sleep (1)

while True:
	sensor.wait_for_in_range()
	fotografar()
