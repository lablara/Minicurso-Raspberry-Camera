from picamera import PiCamera
from time import sleep

sleep (2)

with PiCamera() as cam:
	cam.resolution = (640, 480)
	for n in range (1 , 11):
		cam.capture ("pic " + str (n) + ".jpg" )
		sleep (1)
