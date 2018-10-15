import gpizero
from time import sleep

verde = gpiozero.Led (18)
vermelho = gpiozero.Led (23)
amarelo = gpiozero.Led (24)
azul = gpiozero.Led (25)

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
