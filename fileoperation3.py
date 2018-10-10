#program to overwrite an existing file or copy to a new file by creating destination file alone in runtime

import os
import os.path
from shutil import copyfile
destinationfile = raw_input("Enter destination file name :")
if (os.path.isfile(destinationfile)) :
	print("Do you want to overwrite?(y/n)")
	selection = input()
	if(selection == 'y')
		copyfile('sample.txt',destinationfile)
		print("File copied successfully!")
		print("Copied content in destination file\n")
		a = open(destinationfile, "r")
		print(a.read())
		a.close()
	else :
		print("Contents of the destination file\n")
		a = open(destinationfile,"r")
		print(a.read())
		a.close()
else :
	f = open(destinationfile,"w+")
	copyfile('sample.txt',destinationfile)
	print("File copied successfully!")
	b = open(destinationfile,"r")
	print(b.read())
	b.close()
