#factorial

# def factorial(x):
#     if x==1:
#         return 1
#     else:
#         return x * factorial(x-1)
#
# num=7
# print(num,factorial(num))


#pattern
# row=6
# for i in range(row+1):
#     for j in range(i):
#         print("*",end="")
#     print()

#polindrome number

# num=int(input("enter the number"))
#
# num_string=str(num)
#
# if num_string==num_string[::-1]:
#     print("polindrome number")
# else:
#     print("not a polindrome number")



# def polindrome(num):
#     num_string=str(num)
#
#     if num_string==num_string[::-1]:
#         return True
#     else:
#         return False
#
# print(polindrome(123321))
# print(polindrome(121))
# print(polindrome(12))

###prime number
# num=int(input("enter the prime number"))
#
# for i in range(2,num,4):
#     if num%i==0:
#         print("prime number")
#         break
#     else:
#         print("not an prime number")


#
# def GCD(x,b):
#     while b:
#         x,b=b,x%b
#     return x
#
# num1=28
# num2=38
# print(num1,num2,GCD(num1,num2))

#
#
# num=int(input())
# num2=int(input())
#
# while num2:
#     num,num2=num2,num%num2
# print(num)


###Reverse a List: Write a Python program to reverse a list without using the reverse()
# function.
# list=[1,2,3,4,5,6,7,8,9,0]
# lenth_list=len(list)
#
# reversed_list=list[lenth_list::-1]
# print(list)
# print(reversed_list)



#