import xlrd,xlwt
import os
from xlwt import Workbook
import pandas as pd

wb = xlrd.open_workbook("sample.xlsx")
wb1 = xlrd.open_workbook("example.xlsx")
sheet1 = wb.sheet_by_index(0)
sheet2 = wb1.sheet_by_index(0)
sheet1.cell_value(0,0)
sheet2.cell_value(0,0)
w = Workbook()
sheet = w.add_sheet("sheet1")


df = pd.read_excel('sample.xlsx')
print ("Enter the Team to be retrieved :")
inp = raw_input()
data = df.loc[df["Team"]==inp]


dfList = []
newpath = "/home/test"
dfList.append(data)
appended_data = pd.concat(dfList)
appended_data.to_excel(os.path.join(newpath, 'test3.xlsx'))

wb2 = xlrd.open_workbook("test3.xlsx")
sheet3 = wb2.sheet_by_index(0)
sheet3.cell_value(0,0) 

seat_number = []
resource = []
age = []

for k in range(sheet3.nrows) :
	for x in range(sheet2.nrows) :
		if sheet2.cell_value(x,2) == sheet3.cell_value(k,2) :
			seat_number.append(sheet3.cell_value(k,1))
			resource.append(sheet3.cell_value(k,2))
			age.append(sheet2.cell_value(x,3))
for i in range(len(seat_number)) :
	sheet.write(i,0,seat_number[i])
	sheet.write(i,1,resource[i])
for j in range(len(seat_number)) :
	sheet.write(j,2,age[j])
w.save("output.xlsx")
