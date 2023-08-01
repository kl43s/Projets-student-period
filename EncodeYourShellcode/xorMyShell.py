#!/usr/bin/python
#coding:utf-8
import sys

try:
	a = sys.argv[1]
	a = a.split("x")
	test = []
	count = 0

	while True:
		try:
			cle = int(input("Saisissez comme clé un entier : "))
			break
		except ValueError and NameError:
			count += 1
			if count >= 2:
				print("Mauvaise valeur, essayez d'entrer un entier.")
			else:
				print("Mauvaise valeur.")

	for i in range(len(a)-1):
		if a[i] == "":
			del a[i]

	#-------- Etape 1
	print(a)
	print(len(a))

	for j in range(len(a)):
		temp = int(a[j], base=16)
		temp = hex(temp ^ cle)
		if len(temp) == 3:
			temp = temp.replace("0x", "0x0")
		temp = temp.replace("0x", "\\x")
		test.append(temp)


	#\n\n\n-------- Etape 2
	print(test)
	print(len(test))

	#\n\n\n-------- Etape 3
	print("".join(test))

except:
	print "usage : %s " % sys.argv[0]
