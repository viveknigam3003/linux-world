import subprocess
def date():
	print(subprocess.getoutput("date"))

def remoteDate(remotehost):
	print(subprocess.getoutput("ssh {} date".format(remotehost)))

def cal():
	print(subprocess.getoutput("cal"))

def remoteCal(remotehost):
	print(subprocess.getoutput("ssh {} cal").format(remotehost))

def list():
	print("\n")
	print(subprocess.getoutput("ls"))

def remoteList(remotehost):
	print("\n")
	print(subprocess.getoutput("ssh {} ls").format(remotehost))
