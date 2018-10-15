from picamera import PiCamera
from gpiozero import Button, LED
from time import sleep

camera = PiCamera()

butao = Button (18)

azul = LED (25)

def fotografar():
	camera.capture ("foto.jpg")

def ligarled():
	azul.on()
	sleep (1)
	azul.off()

sleep (1)

botao.when_pressed = ligarled
botao.when_released = fotografar
