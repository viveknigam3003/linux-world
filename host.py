import user
import utilities
import file
import os 
import subprocess


#Blank Comment
def local():
		print("""
		Press 1: to check date
		Press 2: to check cal
		Press 3: to check ls
		Press 4: to create user
		Press 5: to remove user
		Press 6: to create file
		Press 7: to delete file
		Press 8: exit
		""")
			
		print ("Enter your choice:", end=' ')
		ch = input()

		if int(ch) == 1: 
			utilities.date()				

		elif int(ch) == 2:
			utilities.cal()

		elif int(ch) == 3:
			utilities.list()

		elif int(ch) == 4:
			user.addUser()
		
		elif int(ch) == 5:
			user.removeUser()
			
		elif int(ch) == 6:
			file.createFile()
		
		elif int(ch) == 7:
			file.deleteFile()

		elif int(ch) == 8:
			os.system('tput setaf 6')
			print ("\n***Thank You***\n")
			os.system('tput setaf 7')	
			exit()
		
		else:
			os.system('tput setaf 1')
			print ("Invalid Key. Retry")
			os.system('tput setaf 7')
		print("Press Any Key To Continue...")
		input()

def remote():
		print("Enter remotehost IP: ", end=' ')
		remotehost=input()

		print("""
		Press 1: to check date
		Press 2: to check cal
		Press 3: to check ls
		Press 4: to create user
		Press 5: to remove user
		Press 6: to create file
		Press 7: to delete file
		Press 8: Ping {} to check connectivity.
		Press 9: exit
		""".format(remotehost))
			
		print ("enter your choice:", end=' ')
		ch = input()

		if int(ch) == 1:
			utilities.remoteDate(remotehost)

		elif int(ch) == 2:
			utilities.remoteCal(remotehost)
		
		elif int(ch) == 3:
			utilities.remoteList(remotehost)

		elif int(ch) == 4:
			user.addRemoteUser(remotehost)
			
		elif int(ch) == 5:
			user.removeRemoteUser(remotehost)
			
		elif int(ch) == 6:
			file.createRemoteFile(remotehost)

		elif int(ch) == 7:
			file.removeRemoteFile(remotehost)

		elif int(ch) == 8:
			os.system("ping {}".format(remotehost))

		elif int(ch) == 9:
			os.system('tput setaf 6')
			print ("\n***Thank You***\n")
			os.system('tput setaf 7')	
			exit()
		
		else:
			os.system('tput setaf 1')
			print ("Invalid Key. Retry")
			os.system('tput setaf 7')
		print("Press Any Key To Continue...")
		input()
