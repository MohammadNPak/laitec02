

# def say_hello(name):
#     output = f"hello my Name is {name}"
#     print(output)


# say_hello("mohammad")

# say_hello("ali")

# say_hello("hasan")

# say_hello("gholi")
# z =2

# def add(x, y):
#     return x+y


# a = add(1, 3)
# print(a)

# def get_info(name, last_name, age):
#     info = f"hello I'm {name} {last_name} and I'm {age} years old"
#     return info


# name_ = input("name:")
# last_name_ = input("last name:")
# age_ = input("age")
# print(get_info(name_, last_name_, age_))

# from math import exp, sin, cos
# from my_math import exp2, sin as my_sin, cos as my_cos
# x = 10
# error = 0.001
# a = exp2(10, error=0.001)
# print(abs(sin(x)-my_sin(x, error)) <= error)
# print(abs(cos(x)-my_cos(x, error)) <= error)


l=lambda x:x**2

m = lambda x,y: x if x<y else y
r=x if x<y else y
# a=2>3?0:1
if x<y:
  return x
else:
  return y

print(l(5))
