# import class_basic
# obj1 = class_basic.FourCal3()
# print("용병전사", obj1.add(5, 2), obj1.subst(5, 2))


# import class_basic as cb
# obj2 = cb.FourCal3()
# print(obj2.add(5, 2))

# from class_basic import FourCal3
# obj3 = FourCal3()
# print(obj3.add(5, 2))

from class_basic import FourCal3 as fc3
obj4 = fc3()
print(obj4.add(5, 2))