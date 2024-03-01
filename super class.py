# class computer():
#     def dell(self,ram,rom):
#         self.ram=ram
#         self.rom=rom

#
# class dell(computer):
#     def __init__(self,ram,rom):
#         super().__init__(ram,rom)
#         return self.ram * self.rom
#
# class hp(computer):
#     def __init__(self,ram,rom):
#         super().__init__(ram,rom)
#         return self.ram+self.rom
#
# obj1=computer()
# obj2=dell()
# obj3=hp()

# class computer():
#     def __init__(self,ram,rom):
#         self.ram=ram
#         self.rom=rom
#
# class dell(computer):
# #     def __init__(self,ram,rom):
#         super().__init__(ram,rom)
#     def dell1(self):
#         return self.ram*self.rom
#
# class hp(computer):
#     def __init__(self,ram,rom):
#         super().__init__(ram,rom)
#     def hp2(self):
#         return self.ram+self.rom

# obj1=dell(22,44)
# obj2=hp(333,777)
# obj3=computer(23,55)
# print(obj1.dell1())
# print(obj2.hp2())

#
#
# class dell():
#     def __init__(self):
#         print("dell is good")
#     def dell1(self):
#         print("dell1 is good")
#
# class hp(dell):
#     def __init__(self):
#         super().__init__()
#         print("hp is an good")
#     def hp2(self):
#         print("hp2 is good ")
#
# obj2=hp()

