#program to copy the contents of one file to another

with open("sample.txt") as f :
	with open("output.txt") as f1 :
		for line in f :
			f1.write(line)

f1.close()
f.close()
file = open("output.txt",'r')
data = file.read()
file.close()
print data
