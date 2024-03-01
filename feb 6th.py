# #method _riding
#
# # class employee():
# #     def setnumofworkinghours(self):
# #         self.numofworkinghours=40
# #
# #     def displythenumberofworkinghoures(self):
# #         print(self.numofworkinghours)
# #
# # class trainee(employee):
# #     def setnumofworkinghours(self):
# #         self.numofworkinghours=45
#
# #     def resetnumofworkinghoures(self):
# #         super().setnumofworkinghours()
# #
# #
# #
# # obj1=employee()
# # obj1.setnumofworkinghours()
# # print("numofworkinghours:",end=" ")
# # obj1.displythenumberofworkinghoures()
# #
# # trainee=trainee()
# # trainee.setnumofworkinghours()
# # print("numofworkinghoures:",end="")
# # trainee.displythenumberofworkinghoures()
# #
# # trainee.resetnumofworkinghoures()
# # print("number_of_working_houres:",end=" ")
# # trainee.displythenumberofworkinghoures()
#
#
# #
# class Animal:
#     def make_sound(self):
#         print("Animal makes a generic sound")
#
# class Dog(Animal):
#     def make_sound(self):
#         super().make_sound()  # Call the superclass method
#         print("Dog barks")
#
# class Cat(Animal):
#     def make_sound(self):
#         super().make_sound()  # Call the superclass method
#         print("Cat meows")
#
# # Creating objects of the subclasses
# dog = Dog()
# cat = Cat()
#
# # Calling the overridden method
# dog.make_sound()  # Output: Animal makes a generic sound\nDog barks
# cat.make_sound()  # Output: Animal makes a generic sound\nCat meows



#method riding and super()

# class student():
#     def class1(self):
#         print("class student have more then 1000 member")
#
# class besant(student):
#     def class2(self):
#      super().class1()
#     print("besant have tech student")
#
# class sap(student):
#     def class3(self):
#         super().class1()
#         print("print sap is software coures")
#
# obj1=besant()
# obj1.class2()
#
# #
# class student():
#     def r1(self):
#         print("r1 have main string")
#
#     def no_of_student(self):
#         print("r1 have more bca student")
#
# class class1(student):
#     def ro2(self):
#         super().r1()
#         print("ro2 less student include bcom")
#
#     def ro3(self):
#         print("rom3 have equle number student")
#
#
# obj1=class1()
# obj1.ro2()

