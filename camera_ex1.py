import picamera

camera = picamera.PiCamera()
camera.rotation = 180
camera.capture ("pic.jpg")
