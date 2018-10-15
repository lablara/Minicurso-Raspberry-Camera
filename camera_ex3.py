from picamera import PiCamera
from time import sleep

with PiCamera() as camera:
	camera.resolution = (640, 480)
	camera.start_preview ()

	try:
		for i in range (101):
			camera.brightness = i
			sleep (0.1)

		camera.brightness = 50

		for i in range (-100, 101):
			camera.contrast = i
			

 		camera.contrast = 0

 		for i in range (-100 , 101):
 			camera.saturation = i
			sleep (0.05)

 		camera.saturation = 0

 		for i in range (-100, 101):
 			camera.sharpness = i
			sleep (0.05)

 	finally:
 		camera.stop_preview()
 		camera.close()
