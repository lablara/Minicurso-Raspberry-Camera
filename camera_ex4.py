from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.framerate = 15

camera.resolution = (128, 128)
camera.preview_fullscreen = False
camera.preview_window = (0, 0, 128, 128)

camera.start_preview()
 
camera.start_recording ("video.h264")

sleep (10)

camera.stop_recording()
camera.stop_preview()

camera.close()
