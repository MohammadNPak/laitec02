
# str           str()
# number
#   bool        bool()
#   int         int()
#   float       float()
#   complex     complex()

# type()
# input()  print()


# if conditions1:
#   commands1
# elif conditions2:
#   commands2
# elif condition3:
#   commands3
# else:
#   commands4

# < > <= >= != ==
# and or not
# bool()

# while conditions:
#   commands

#   if condition2:
#     break
#   if condition3:
#     continue
#   some commands
# else:
#   commands

# ادامه ی برنامه

# list
# tuple
# dict
# set


# a = 0
# while a<10:
#   a+=1
#   if a==6:
#     continue
#   print(a)

# name = "mohammad"
# age = 30
# message = f"my name is {name} and i'm {age} years old"
# print(message)

# n = int(input("please enter n: "))
# i=2
# while i<n:
#   # print(f"{n}%{i} = {n%i}")
#   if n%i ==0:
#     print("not prime")
#     break
#   i+=1
# else:
#   print("prime")





# m = int(input("please enter m: "))
# n = 2
# while n<=m:
#   # ************** is n prime?****************
#   i=2
#   is_prime = False
#   while i<n:
#     if n%i ==0:
#       is_prime=False
#       break
#     i+=1
#   else:
#     is_prime=True
#   # ********************************
#   if is_prime and m%n==0:
#     print(n)
#     m=m//n
#     n=2
#     continue
#   n+=1


# n = int(input())
# f = 1
# i = 1
# while i<=n:
#   f *=i
#   i+=1
# print(f)


# n = 5

# *
# **
# ***
# ****
# *****

# n = int(input())
# i = 1
# while i<=n:
#   j=1
#   while j<=i:
#     print("*",end="")
#     j+=1
#   print()
#   i+=1


#     *
#    **
#   ***
#  ****
# *****

# n = int(input())
# i = 1
# while i<=n:
#   j=1
#   while j<=n:
#     if j<=n-i:
#       print(" ",end="")
#     else:
#       print("*",end="")
#     j+=1
#   print()
#   i+=1


# n =5                    2*i-1     space = n-i
#     *         i = 1   star = 1    space = 4 
#    ***        i = 2   star = 3    space = 3
#   *****       i = 3   star = 5    space = 2
#  *******      i = 4   star = 7    space = 1
# *********     i = 5   star = 9    space = 0

# n = int(input())
# i = 1
# while i<=n:
#   j=1
#   while j<=n+i-1:
#     if j<=n-i:
#       print(" ",end="")
#     else:
#       print("*",end="")
#     j+=1
#   print()
#   i+=1


# a = [2,1,40,"m",True]
#   #  0 1 2  3   4       index
# print(type(a))
# print(a[1::2])
# a[3]=80
# print(a)



# numbers =[
#   2,3,4,5,6,7,8,9,0,12,23,34,56,78,89,90,4
# ]
# 0 - 15
# 0<= index < len
# -len<= index < 0

# i = 0
# s = 0
# while i<len(numbers):
#   s+=numbers[i]
#   i+=1
# print(s)

# print(numbers)
# numbers.append("mohammad")
# print(numbers)

even_numbers= []

i =0
while i<100:
  even_numbers.append(i)
  i+=2
print(even_numbers)




