from class_basic import FourCal3 as fc3

class Cbup(fc3):
  def mul(self, num1, num2):
    result = num1 * num2
    return result

  def div(self, num1, num2):
    if num2 != 0 :
      result = num1 / num2
    else :
      result = "ERROR!"
    return result

obj1 = Cbup()
print("전직전사", obj1.add(5, 5), obj1.subst(5, 5), obj1.mul(5, 5), obj1.div(5, 5))


# 클래스 재정의
class cbupup(fc3):
  def add(self, num1, num2):
    result = num1 + num2
    return "더하기 결과는 " + str(result) + "입니다.\n"
    # result_text = "더하기 결과는 {} 입니다".format(str(result))

  def mul(self, num1, num2):
    result = num1 + num2
    return "곱하기 결과는 " + str(result) + "입니다.\n"

  def div(self, num1, num2):
    if num2 != 0:
      result = num1 / num2
    else :
      result = "ERROR!"
    return "나누기 결과는 " + str(result) + "입니다."

obj3 = cbupup()
print("2차 전직전사\n", obj3.add(1, 1), obj3.mul(1, 1), obj3.div(1, 1))