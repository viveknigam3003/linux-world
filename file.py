import os 
import subprocess
def createFile():
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

def createRemoteFile(remotehost):
	print("Enter File Name: ", end=' ')
	FileName = input()
	y = subprocess.getstatusoutput("ssh {} cat {}".format(remotehost, FileName))
	x = subprocess.getstatusoutput("ssh {} touch {}".format(remotehost, FileName))
	if y[0] == 0:
		os.system('tput setaf 1')
		print ("File of this name already exits. Try a different name")
		os.system('tput setaf 7')
	else:
		os.system('tput setaf 2')
		print ("File Successfully Created")
		os.system('tput setaf 7')

def deleteFile():
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

def deleteRemoteFile(remotehost):
	print("Enter File Name: ", end=' ')
	FileName = input()
	y = subprocess.getstatusoutput("ssh {} cat {}".format(remotehost, FileName))
	if y[0] == 0:
		os.system('tput setaf 2')
		os.system("ssh {} rm {}".format(remotehost, FileName))
		print ("'{}' Deleted Sucessfully".format(FileName))
		os.system('tput setaf 7')
	else:
		os.system('tput setaf 1')
		print ("File '{}' Does Not Exists".format(FileName))
		os.system('tput setaf 7')