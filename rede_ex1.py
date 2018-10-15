import socket
import picamera
import time

ip = "10.0.0.10"
porta = 15000

socket_cliente = socket.socket()
socket_cliente.connect((ip, porta))

conexao = socket_cliente.makefile ('wb')

try:
	camera = picamera.PiCamera()
	camera.resolution = (320, 320)
	camera.framerate = 15

	time.sleep(2)

	camera.start_recording (conexao, format = "h264")
	camera.wait_recording (60) 
	camera.stop_recording ()

except:

	print ("Erro no envio do video" )

finally:
	camera.close ()
	socket_cliente.close ()
