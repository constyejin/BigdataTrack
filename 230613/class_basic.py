# 1
class FourCal1:
  def setdata(self, num1, num2):
    self.num1 = num1
    self.num2 = num2

  def add(self):
    result = self.num1 + self.num2
    return result

  def subst(self):
    result = self.num1 - self.num2
    return result

obj1 = FourCal1()
obj1.setdata(5,2)
print("전사1", obj1.add(), obj1.subst())

obj2 = FourCal1()
obj2.setdata(2,2)
print("마법사1", obj2.add(), obj2.subst())


# 2
class FourCal2:
  # __init__ 사용시 setdata 없이 사용 가능
  def __init__(self, num1, num2):
    self.num1 = num1
    self.num2 = num2

  def add(self):
    result = self.num1 + self.num2
    return result

  def subst(self):
    result = self.num1 - self.num2
    return result

obj2 = FourCal2(10, 5)
print("전사2", obj2.add(), obj2.subst())


# 3 method로 바로 데이터를 받는다
class FourCal3:
  def __init__(self):
    print("FourCal3를 이용해 주셔서 감사합니다.")

  def add(self, num1, num2):
    result = num1 + num2
    return result

  def subst(self, num1, num2):
    result = num1 - num2
    return result

obj3 = FourCal3()

print("전사3", obj3.add(10, 2), obj3.subst(10, 2))