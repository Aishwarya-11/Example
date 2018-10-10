#program to create sourcefile and destination file in runtime and copy the contents of sourcefile to destinationfile

import os
import sys
import os.path
from shutil import copyfile
from sys import stdin

def destinationfunction() :
	destinationfile = raw_input("Enter destination file name :")
	if (destinationfile!='x') :	
		if (os.path.isfile(destinationfile)) :
			print("Do you want to overwrite?(y/n)")
			selection = input()
			if(selection == 'y')
				copyfile(sourcefile,destinationfile)
				print("File copied successfully!")
				print("Copied content in destination file\n")
				a = open(destinationfile, "r")
				print(a.read())
				a.close()
			elif(selection=='n') :
				print("Contents of destination file\n")
				a = open(destinationfile,"r")
				print(a.read())
				a.close()
		else :
			f = open(destinationfile,"w+")
			copyfile(sourcefile,destinationfile)
			print("File copied successfully!")
			b = open(destinationfile, "r")
			print(b.read())
			b.close()
	else :
		print("Exit!")

if __name__ == "__main__" :
	print("Enter x to exit")
	sourcefile = raw_input("Enter source file name :")
	if (sourcefile!='x') :
		if(os.path.isfile(sourcefile)) :
			print("Already exists!! Do you want to overwrite?(y/n)")
			option = input()
			if (option == 'y') :
				f = open(sourcefile,"w")
				print("Enter the data :")
				data = sys.stdin.readlines()
				f.write(str(data))
				f.close()
				destinationfunction()
			elif(option == 'n') :
				destinationfunction()
		else :
			f = open(sourcefile,"w+")
			print("Enter the data :")
			data = sys.stdin.readlines()
			f.write(str(data))
			f.close()
			destinationfunction()
	else :
		print("Exit!!")

