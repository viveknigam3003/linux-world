import os 
import subprocess
import getpass
import host

os.system('tput setaf 6')
print ("\t\t\tWelcome to Linux Tool")
print ("\t\t\t------------------")
os.system ('tput setaf 7')

pword = "password"
InputPass = getpass.getpass("Enter Password: ")

if InputPass != pword:
	os.system('tput setaf 1')
	print("Authentication Failed!")
	os.system('tput setaf 7')
	exit()

else:
	while True:
		os.system("clear")
		print ("\t\t\tWelcome to Linux Tool")
		print ("\t\t\t------------------")
		print("Run on? localhost/remotehost Press(l/r): ", end=' ')
		platform=input()

		if platform=="l":
			host.local()

		elif platform=="r":
			host.remote()

		else:
			os.system('tput setaf 1')
			print("Alert: Invalid!")
			os.system('tput setaf 7')
			
