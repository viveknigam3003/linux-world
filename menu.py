import os 
import subprocess
<<<<<<< HEAD

while (1):
	print("\n")
	os.system('tput setaf 6')
	print ("\t\t\tWelcome to Linux Tool")
	print ("\t\t\t------------------")
	os.system ('tput setaf 7')

	print("""
	Press 1: to check date
	Press 2: to check cal
	Press 3: to check ls
	Press 4: to create user
	Press 5: to create file
	Press 6: to remove user
	Press 7: to delete file
	Press 8: exit
	""")

	print ("enter your choice:", end=' ')
	ch = input()

	if int(ch) == 1: 
		print(subprocess.getoutput("date"))

	elif int(ch) == 2:
		print(subprocess.getoutput("cal"))

	elif int(ch) == 3:
		print("\n")
		print(
		print(subprocess.getoutput("ls"))

	elif int(ch) == 4:
		print("Enter User Name: ", end=' ')
		UserName = input()
		x = subprocess.getstatusoutput("useradd {}".format(UserName))
		if x[0] == 0:
			os.system('tput setaf 2')
			print ("User Successfully Created")
			os.system('tput setaf 7')
		else:
			os.system('tput setaf 1')
			print ("User Not Created : {}".format(x[1]))
			os.system('tput setaf 7')
	elif int(ch) == 5:
		print("Enter File Name: ", end=' ')
		FileName = input()
		y = subprocess.getstatusoutput("cat {}".format(FileName))
		x = subprocess.getstatusoutput("touch {}".format(FileName))
		if y[0] == 0:
			os.system('tput setaf 1')
			print ("File of this name already exits. Try a different name")
			os.system('tput setaf 7')
		else:
			os.system('tput setaf 2')
			print ("File Successfully Created")
			os.system('tput setaf 7')
	elif int(ch) == 6:
		print("Enter User Name: ", end=' ')
		UserName = input()
		x = subprocess.getstatusoutput("userdel {}".format(UserName))
		if x[0] == 0:
			os.system('tput setaf 2')
			print ("User Successfully Removed")
			os.system('tput setaf 7')
		else:
			os.system('tput setaf 1')
			print ("User '{}' Does Not Exists".format(UserName))
			os.system('tput setaf 7')
	elif int(ch) == 7:
		print("Enter File Name: ", end=' ')
		FileName = input()
		y = subprocess.getstatusoutput("cat {}".format(FileName))
		if y[0] == 0:
			os.system('tput setaf 2')
			os.system("rm {}".format(FileName))
			print ("'{}' Deleted Sucessfully".format(FileName))
			os.system('tput setaf 7')
		else:
			os.system('tput setaf 1')
			print ("File '{}' Does Not Exists".format(FileName))
			os.system('tput setaf 7')
		
	elif int(ch) == 8:
		os.system('tput setaf 6')
		print ("\n***Thank You***\n")
		os.system('tput setaf 7')	
		exit()
	else:
		os.system('tput setaf 1')
		print ("Invalid Key. Retry")
		os.system('tput setaf 7')

=======
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
			
>>>>>>> 527e9409575da24b0be13d5e26f2660832aa8812
