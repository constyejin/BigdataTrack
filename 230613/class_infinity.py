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