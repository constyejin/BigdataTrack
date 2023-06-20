# 고수학 연산을 위해 임포트
import numpy as np
#  # scikit-learn의 샘플 데이터 로드를 위해 import
# sklearn (scikit-learn install) => pip install scikit-learn
# scikit-learn의 경우 Numpy, Scipy 모듈도 추가로 설치 해야한다. 
# pip로 install시 자동설치 되므로 추가 설치 할 필요 X
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
  # print(rate)

# print(dojun_arr / sungjun_arr)

# indexing & slicing
print(dojun_list[0])
print(dojun_list[-1])
print(dojun_list[-2])
# 0부터 시작 : 뒤에 생략 
print(dojun_list[:])
# 3개 다 나오게 하고싶다면 끝자리 수 + 1
print(dojun_list[0:2])

# tuple & list (2차원 배열)
dojun_arr_a = np.array([(1,2,3), (4,5,6)])
dojun_arr_b = np.array([(1,2,3), (4,5,6)])

print(dojun_arr_a[0][1])
print(dojun_arr_a[1])
print(dojun_arr_b)

# type of
print(type(dojun_arr_a))
print(type(dojun_arr_b))
print(type(dojun_arr_b[0][1]))

# 값 바꾸기
dojun_arr_b[0][1] = 20
print(dojun_arr_b)

# 1차원 데이터, 2차원 데이터
print(dojun_arr_b[0])
# slicing을 하면 차원이 하나 더 씌워진다.
print(dojun_arr_b[:1])

print(dojun_arr_a[0])
print(dojun_arr_a[:1][0])

# shape
# print((dojun_arr_b[0]).shape)
# print((dojun_arr_b[:1]).shape)

# ndim
# print((dojun_arr_b[0]).ndim)
# print((dojun_arr_b[:1]).ndim)


arr = np.array([[10, 20, 30, 40], [50, 60, 70, 80], [90, 100, 110, 120]])
print(arr[1])

# True / False로 값 반환
print(dojun_arr_a >=5)
# True 값만 추출
print(dojun_arr_a[dojun_arr_a >=5])

dojun_arr_c = np.array([["1",2,3], [4,5,6]])
print(dojun_arr_c)


# 3차원 배열
dojun_arr_3d = np.array([[[1,2,3], [4,5,6]], [[7,8,9], [10,11,12]]])
print(dojun_arr_3d)
print(dojun_arr_3d.shape)

# shape과 len의 차이 (len은 첫번째 값만)
print(dojun_arr_3d.shape[0])
print(len(dojun_arr_3d))
print(len(dojun_arr_3d.shape))

print(dojun_arr_3d.ndim)
print(type(dojun_arr_3d[0][0][0]))

yejin_arr_2d = np.array([[1,2,3], [4,5,6]])
print(type(yejin_arr_2d[0][0]))

# dtype
yejin_arr_2d = np.array([[1,2,3], [4,5,6]], dtype = np.float32)
print(yejin_arr_2d.dtype)

yejin_arr_2d = yejin_arr_2d.astype(np.int64)
print(yejin_arr_2d.dtype)


print(np.zeros((2, 3)))
print(np.ones((2, 3)))
print(np.full((2, 3), 10))

# arr.T