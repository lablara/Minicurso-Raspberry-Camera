import gpiozero
from time import sleep

verde = gpiozero.LED (18)
vermelho = gpiozero.LED (23)
amarelo = gpiozero.LED (24)
azul = gpiozero.LED (25)

sleep (1)

while True:

	verde.on()
	sleep (1)
	verde.off()

	vermelho.on()
	sleep (1)
	vermelho.off()

	amarelo.on()
	sleep (1)
	amarelo.off()

	azul.on()
	sleep (1)
	azul.off()
	
	sleep (1)
	verde.on()
	vermelho.on()
	amarelo.on()
	azul.on()
	
	sleep (3)
	
	verde.off()
	vermelho.off()
	amarelo.off()
	azul.off()
	
	sleep (1)
