import xml.dom.minidom
import os.path 

def function() :
	filename = raw_input("Enter filename :")
	if(filename!='x') :
		if(os.path.isfile(filename)) :
			xmlObject = xml.dom.minidom.parse(filename)
			print("Enter data to retrieve :")
			var = raw_input()
			tagname = xmlObject.getElementsByTagName(var)[0]
			print ''.join( [node.data for nose in tagname.childNodes] )
			function()
		else :
			print("File doesn't exist!!!")
			function()
	else :
		print("Exit")

if __name__ == "__main__" :
	print("Enter x to exit")
	function()
