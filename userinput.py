import sys

def funcn() :
	try :
		num = int(input())
		print ("Entered number :",num)
	except NameError :
		print ("Error!!!Enter another :")
		funcn()
if __name__ == "__main__" :
	funcn()
