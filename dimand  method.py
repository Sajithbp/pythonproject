# #
# class a():
#     def method(self):
#         print("method is A")
#
# class b():
#     def method(self):
#         print("method is B")
#
# class c(a,b):
#     pass
#     # def method(self):
#     #     print("method is c")
#
# obj1=c()
# obj1.method()

#
# class BCOM():
#     def student(self):
#         print("b.com student was good")
#
# class BCA(BCOM):
#     pass
#     # def student(self):
#     #     print("bca student has good")
#
# class BSC(BCOM):
#     def student(self):
#         print("bsc student also a good")
#
# class BA(BCA,BSC):
#     pass
#
#
# c=BA()
# c.student()
# c1=BCA()
# c1.student()


#
# class over():
#     def name(self):
#         print("overraiding is good")
#
# class method(over):
#     def name1(self):
#         super().name()
#         print("method is good")
#
# c1=method()
# c1.name1()

"""Constructor in inheritance"""

#
# class A:
#     def feature(self):
#         print("A")
#     pass
#
#
# class B(A):
#     def feature(self):
#         print("B")
#
#     pass
#
# class C(A):
#     def feature(self):
#         print("C")
#     pass
#
#
# class D(A):
#     def feature(self):
#         print("D")
#     pass
#
#
# class E(B, C,D):
#
#
#     pass
#
#
#
#
# a = E()
# print(E.mro())
# a.feature()




class A:
    def feature(self):
        print("A")
    pass


class B:
    def feature(self):
        print("B")

    pass

class C(A):
    def feature(self):
        print("C")
    pass


class D(B, C):
    def feature(self):
        print("D")
    pass


class E(C):
    def feature(self):
        print("E")
    pass


class F(D, E, C):
    def feature(self):
        print("F")
    pass

a = F()
print(F.mro())
a.feature()