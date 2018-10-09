def mainpgm(var) :
	try :
		while(var!=5) :
			if(var==1) :
				import program1
				program1.tuple()
			elif(var==2) :
				import program2
				program2.list()
			elif(var==3) :
				import program3
				program3.printstatement()
			elif(var==4) :
				import program4
				program4.dict()
			else :
				print "Wrong selection\n"
			print("Enter another selection :")
			var = input()
			mainpgm(var)
		print "Exit!!"
	except NameError :
		print "It's a NameError\nEnter another selection :"
		var = input()
		mainpgm(var)
	except IndexError :
		print "It's a IndexError\nEnter another selection :"
		var = input()
		mainpgm(var)

if __name__ == "__main__" :
	print ("1: Convert tuple into list\n2: Insert and delete elements in list\n3: Print statement\n4: Sorting dictionary\n5: Exit")
	var = int(input("Enter the selection :"))
	mainpgm(var)
