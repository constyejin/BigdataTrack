import xlwings as xw

wb = xw.books.active
ws = wb.sheets.active

num1 = ws.range('B2').value
num2 = ws.range('C2').value

num3 = num1 + num2

ws.range('D2').value = num3