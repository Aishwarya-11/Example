#program to create file in runtime and copy

import os
from shutil import copyfile

f = open("myfile.txt","w+")
copyfile('sample.txt',f)
print("File copied successfully!")
a = open("myfile.txt",'r')
print(a.read())
a.close()
