#!/usr/bin/python3
import os
import sys
import time

def banner():
	os.system("clear")
	print('''
################################
#                              #
#                              #
#          Digicode            #
#          by kl43s            #
#                              #
#                              #
################################
''')

def cle(a,b,c, service, port):  
	combo = str(a) + " " + str(b) + " " + str(c)
	ip = str(input("IP du serveur : "))
	user = str(input("user cible ssh : "))
    
	ssh = 'ssh -p ' + str(port) + ' ' + user + '@' + ip
	sftp = 'sftp -P ' + str(port) + ' ' + user + '@' + ip
	ftp = 'ftp ' + ip + ' ' + str(port)
    
	serviceReseau = {1:ssh, 2:sftp, 3:ftp} 
    
	f = open("cle.sh", "w")
	f.write("for x in " + combo + "; do nmap -Pn --host-timeout 201 --max-retries 0 -p $x " + ip + " && sleep 1; done && " + serviceReseau[service])
	f.close()
	os.system("chmod +x cle.sh")

def digicode(a, b, c, service, port):
	os.system('''
iptables -F

iptables -N KNOCKING
iptables -N GATE1
iptables -N GATE2
iptables -N GATE3
iptables -N PASSED


iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT

iptables -A INPUT -i lo -j ACCEPT
iptables -A INPUT -p tcp --dport 80 -j ACCEPT
iptables -A INPUT -j KNOCKING

iptables -A GATE1 -p tcp --dport ''' + str(a) + ''' -m recent --name AUTH1 --set -j DROP
iptables -A GATE1 -j DROP
iptables -A GATE2 -m recent --name AUTH1 --remove


iptables -A GATE2 -p tcp --dport ''' + str(b) + ''' -m recent --name AUTH2 --set -j DROP
iptables -A GATE2 -j GATE1
iptables -A GATE3 -m recent --name AUTH2 --remove


iptables -A GATE3 -p tcp --dport ''' + str(c) + ''' -m recent --name AUTH3 --set -j DROP
iptables -A GATE3 -j GATE1
iptables -A PASSED -m recent --name AUTH3 --remove

iptables -A PASSED -p tcp --dport ''' + str(port) + ''' -j ACCEPT
iptables -A PASSED -j GATE1

iptables -A KNOCKING -m recent --rcheck --seconds 15 --name AUTH3 -j PASSED
iptables -A KNOCKING -m recent --rcheck --seconds 15 --name AUTH2 -j GATE3
iptables -A KNOCKING -m recent --rcheck --seconds 15 --name AUTH1 -j GATE2
iptables -A KNOCKING -j GATE1
''')
	print("Installation du digicode terminé. \nVotre code est le suivant : ", a, " ", b, " ", c, ".")
	cle(a,b,c, service, port)

def menu():
	print("Afin de fabriquer votre digicode personnalise suivez les consignes.")
	while True:
		try:
			a = int(input("premier numero : "))
			b = int(input("deuxieme numero : "))
			c = int(input("troisieme numero : "))
			service = int(input("Service (1: ssh, 2:sftp, 3:ftp) : "))
			port = int(input("Sur quel port voulez-vous joindre votre service ?"))
			break
		except:
			print("Entrez un entier !")

	digicode(a, b, c, service, port)

banner()
menu()
