from picamera import PiCamera
from gpiozero import Button, LED
from time import sleep

camera = PiCamera()

butao = Button (18)

azul = LED (25)

def fotografar():
	camera.capture ("foto.jpg")
	print ("Foto capturada")

def ligarled():
	azul.on()
	sleep (1)
	azul.off()

sleep (1)
print ("Iniciando programa de captura de imagens")

botao.when_pressed = ligarled
botao.when_released = fotografar
