from openpyxl import Workbook
wb = Workbook()

# grab the active worksheet
ws = wb.active

# Data can be assigned directly to cells


# Rows can also be appended
ws.append([1, 2, 3])


# Save the file
wb.save("sample.xlsx")
