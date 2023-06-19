# 고수학 연산을 위해 임포트
import numpy as np
#  # scikit-learn의 샘플 데이터 로드를 위해 import
from sklearn.datasets import load_iris
import sklearn.datasets

# print(dir(sklearn.datasets))
iris = load_iris()
# print(iris)

# print(iris.feature_names)
# print(iris.data[:10])
# print(iris.target_names)

dojun_list = [100, 50, 30]
sungjun_list = [200, 30, 80]

total_list = dojun_list + sungjun_list
# print(total_list)

dojun_arr = np.array(dojun_list)
sungjun_arr = np.array(sungjun_list)

total_arr = dojun_arr + sungjun_arr
# print(total_arr)

# print(dojun_arr * sungjun_arr)

for dojun, sungjun in zip(dojun_list, sungjun_list):
  rate = dojun / sungjun
  print(rate)

print(dojun_arr / sungjun_arr)