def list() :
	print ("Creating a list and performing insertion and deletion operations\n ")
	print ("Enter the length :")
	length = int(input())
	print("Enter the values :")
	list1 = []
	for i in range(length) :
		value = input()
		list1.append(value)
	print (list1)
	print ("Enter the value to insert :")
	num1 = input()
	list1.insert(0,num)
	print (list1)
	print (list1.pop())
	del list1[-1]
	print (list1)
	list1.insert(3,list1.pop(2))
	print (list1)
