import statsmodels.api as sm
import joblib
import sys

# print(len(sys.argv))
# print(sys.argv)

if len(sys.argv) == 4:
  year = sys.argv[1]
  squere = sys.argv[2]
  floor = sys.argv[3]
  print(year, squere, floor)
else :
  sys.exit("건축년도, 면적, 층을 입력해주세요.")

loaded_model = joblib.load('./model/apt_price.pkl')
print(loaded_model.predict([[1, int(year), int(squere), int(floor)]]))

pred = loaded_model.predict([[1, int(year), int(squere), int(floor)]])
print("예측금액은 {:,.0f}만원입니다.".format(pred[0]))