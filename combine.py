import xlrd,xlwt
from xlwt import Workbook

wb = xlrd.open_workbook("sample.xlsx")
wb1 = xlrd.open_workbook("example.xlsx")
sheet1 = wb.sheet_by_index(0)
sheet2 = wb1.sheet_by_index(0)
sheet1.cell_value(0,0)
sheet2.cell_value(0,0)
w = Workbook()
sheet = w.add_sheet("sheet1")
seat_number = []
resource = []
age = []
count = 0

def combine() :
	print ("Enter the team to be retrieved :")
	inp = raw_input()

	for col in range(sheet1.nrows) :
		if sheet1.cell_value(col,3) == inp :
			k = col
			for x in range(sheet2.nrows) :
				if sheet2.cell_value(x,2) == sheet1.cell_value(k,2) :
					seat_number.append(sheet1.cell_value(k,1))
					resource.append(sheet1.cell_value(k,2))
					age.append(sheet2.cell_value(x,3))
		else :
			count =+1
			if count == sheet1.nrows :
				print ("Team not found! Try with another!!")
				combine()
	for i in range(len(seat_number)) :
		sheet.write(i,0,seat_number[i])
		sheet.write(i,1,resource[i])
	for j in range(len(seat_number)) :
		sheet.write(j,2,age[j])
	w.save("output.xlsx")

if __name__ == "__main__" :
	combine()

