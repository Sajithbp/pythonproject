"""OOPS CONCEPTS"""
"""CLASS == classes are user define blue print or prototype"""
"""if calci is class then sum, mul, sub and div are methode"""
"""classes is consist of methods, class variables, instant variable and constructor etc """
"""creation of new object not needed"""


# class Calculator:
#     num = 100
#
#     def getdata(self):
#         print("i am executing methode in class")
#
#
# cal = Calculator()
# cal.getdata()
# print(cal.num)


"""constructor is a methode when an object is create """


# class Calculator:
#     num = 100
#
#     def getdata(self):
#         print("i am executing methode in class")
#
#     def _init_(self):
#         print("i am called automatically when object is created")
#
#
# cal = Calculator()
# cal.getdata()
# print(cal.num)


"""self :- is used as the reference to the current instance of the clss when you define methode use must include self 
parameter in method definition"""
"""self key word is mandatory for calling variable name into methode"""
"""new key word not required create for object new key word use in other program in java"""


class Calculator:
    num = 100

    def getdata(self):
        print("i am executing methode in class")

    def __init__(self, a, b):
        self.a = a  #
        self.b = b
        print("i am called automatically when object is created")

    def summation(self):
        return self.a + self.b + Calculator.num


# cal = Calculator(10, 23)
# cal1 = Calculator(17, 6)
# print(cal.summation())
# print(cal1.summation())