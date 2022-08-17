
# a,b,c
# a+b+c=n    c = n-a-b
# a**2+b**2=c**2

# a**2+b**2 = (n-a-b)**2

# n = int(input())
# a = 1
# b = 1
# is_finished = False
# while a <= n//3 and not is_finished:
#     b = a+1
#     a2 = a**2
#     while b <= n//2 and not is_finished:
#         if b**2+a2 == (n-a-b)**2:
#             print(a, b, int((a**2+b**2)**0.5))
#             is_finished = True
#         b += 1
#     a += 1
#     if is_finished:
#         break
# else:
#     print("Impossible")


# b**2 + a**2 = (n-a)**2 -2*(n-a)*b+b**2
# a**2=(n-a)**2-2(n-a)*b
# (a**2-(n-a)**2)/(2(n-a))=b

# n = int(input())
# a = 1
# b = 1
# while a < n:
#     b = int(((n-a)**2-a**2)/(2*(n-a)))
#     c = n-a-b
#     if a**2+b**2 == c**2 and b > 0 and c > 0:
#         out = [a, b, c]
#         out.sort()
#         print(*out)
#         break
#     a += 1
# else:
#     print("Impossible")


# a = [1, 2, 1, 5, 1, 3, 4, 6, 8, 0]
# a.append(5)
# b = a[2:5:2]
# b = a.pop(0)
# c = "ac"
# if c in a:
#     b = a.index(c)
#     print(b)
# print(a)
# print(a.count(1))
# a.remove("abc")
# a.insert(2, "mohammad")
# b = a.copy()
# b = ["m", "a"]
# a.extend(b)
# a.reverse()
# a.sort(reverse=True)
# print(a)

# b = [[1,2],[3,4]]
# print( b[1][0] )

# a = [[int(input()), int(input())], [int(input()), int(input())]]
# print(a)
# print(a[0][0]*a[1][1]-a[1][0]*a[0][1])

# a = [[], []]
# for i in range(len(a)):
#     for j in range(2):
#         a[i].append(int(input()))
# print(f"|{a[0][0]:4} {a[0][1]:4}|\n|{a[1][0]:4} {a[1][1]:4}|")
# a=[[1],[2]]

# import numpy
# rows = 3
# cols = 3
# a = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# for i in range(len(a)):
#     for j in range(len(a[0])):
#         a[i][j] = int(input())
# print(a)
# 1 2 3
# 4 5 6
# 7 8 9

# 1*(5*9 - 6*8) - 2*(4*9-6*7) + 3*(4*8 - 5*7)

# det = (a[0][0]*(a[1][1]*a[2][2] - a[1][2]*a[2][1]) -
#        a[0][1]*(a[1][0]*a[2][2] - a[1][2]*a[2][0]) +
#        a[0][2]*(a[1][0]*a[2][1] - a[1][1]*a[2][0]))
# print(det)

# b = numpy.array(a)
# print(numpy.linalg.det(b))

from typing import MutableMapping


a = "abcdefg"
# a = ["a", "b", "c", "d", "e", "f"]
# print(a[3:6])
# list  => mutable
# str   => immutable
# a[0] = "z"
# print(a)

# tuple   => immutable
# t = (1,2,3,4,5,6)
# t[0]=4
# set  => Mutable

a = {"1","2"}
print(a)

# b=str(a)
print("".join(a))






