import os.path 

def function() :
	filename = raw_input("Enter filename :")
	if(filename!='x') :
		if(os.path.isfile(filename)) :
			with open("sample.json",'r') as f:
				data = json.load(f)
			print("Enter data to retrieve :")
			var = raw_input()
			print data[var]
			function()
		else :
			print("File doesn't exist!!!")
			function()
	else :
		print("Exit")

if __name__ == "__main__" :
	print("Enter x to exit")
	function()
