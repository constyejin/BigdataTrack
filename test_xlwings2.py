import xlwings as xw
import joblib
import statsmodels.api as sm

loaded_model = joblib.load('./model/apt_price.pkl')

wb = xw.books.active
ws = wb.sheets.active

year = ws.range('B2').value
square = ws.range('C2').value
floor = ws.range('D2').value

pred = loaded_model.predict([[1, year, square, floor]])
ws.range('E2').value = pred
print("엑셀에 예측가격을 입력하였습니다.")