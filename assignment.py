import xlrd,xlwt
from xlwt import Workbook

wb1 = xlrd.open_workbook("NETWORK_LLD.xlsx")
ws1 = wb1.sheet_by_name("Connectivity matrix")
wb2 = xlrd.open_workbook("INFRA_LLD.xlsx")
ws2 = wb2.sheet_by_name("OBO")
w = Workbook()
sheet = w.add_sheet("sheet1")

from_subcomp = []
port = []
to_ip = []
for col1 in range(ws1.ncols) :
	if ws1.cell_value(0,col1) == "From Vendor" :
		k = col1
		for row1 in range(ws1.nrows) :
			if ws1.cell_value(row1,k) == "SeaChange" :
				for l in range(ws1.ncols) :
					if ws1.cell_value(0,l) == "From subcomponent" :
						from_subcomp.append(ws1.cell_value(row1,l))
				for m in range(ws1.ncols) :
					if ws1.cell_value(0,m) == "Port" :
						port.append(ws1.cell_value(row1,m))
				for n in range(ws1.ncols) :
					if ws1.cell_value(0,n) == "To IP" :
						to_ip.append(ws1.cell_value(row1,n))
for x in range(len(from_subcomp)) :
	sheet.write(x,0,from_subcomp[x])
for y in range(len(port)) :
	sheet.write(y,1,port[y])
for z in range(len(to_ip)) :
	sheet.write(z,2,to_ip[z])

subcomp = []
hostname = []
for col2 in range(ws2.ncols) :
	if ws2.cell_value(1,col2) == "Subcomponents" :
		j = col2
		for row2 in range(ws2.nrows) :
			subcomp.append(ws2.cell_value(row2,j))
for col3 in range(ws2.ncols) :
	if ws2.cell_value(1,col3) == "Hostname" :
		i = col3
		for row3 in range(ws2.nrows) :
			hostname.append(ws2.cell_value(row3,i))
for x in range(len(subcomp)) :
	sheet.write(x,3,subcomp[x])
for x in range(len(hostname)) :
	sheet.write(x,4,hostname[x])

w.save("find.xlsx")

data = []
wb3 = xlrd.open_workbook("find.xlsx")
ws3 = wb3.sheet_by_index(0)
ws3.cell_value(0,0)
print ("Subcomponent  -->  Hostname")
for s in range(ws3.nrows) :
	for t in range(ws3.nrows) :
		if ws3.cell_value(s,0) == ws3.cell_value(t,3) :
			data1 = ws3.cell_value(s,0)
			data2 = ws3.cell_value(t,2)
			data3 = ws3.cell_value(t,1)
			data4 = ws3.cell_value(t,4)
			if data1 == "" :
				exit()
			else :
				print(data1+" "+"-->"+" "+data2+" "+"-->"+" "+data3+" "+"-->"+" "+data4)





