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
print("전사", obj1.add(), obj1.subst())

obj2 = FourCal1()
obj2.setdata(2,2)
print("마법사", obj2.add(), obj2.subst())