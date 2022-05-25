def gcd(x, y):
    for i in range(min(x, y), 1, -1):
        if x % i == 0 and y % i == 0:
            return i
    return 1


def factorial(n):
    f = 1
    for i in range(1, n+1):
        f = f*i
    return f


def exp(x, n):
    s = 1+x
    for i in range(2, n+1):
        s = s + (x**n)/factorial(n)
    return s


def exp2(x, error):
    s = 1+x
    i = 2
    while True:
        diff = (x**i)/factorial(i)
        s = s+diff
        if diff <= error:
            return s
        i += 1


def sin(x, error):
    s = x
    i = 3
    sign = -1
    while True:
        diff = sign*(x**i)/factorial(i)
        s = s+diff
        if abs(diff) <= error:
            return s
        i += 2
        sign *= -1


def cos(x, error):
    s = 1
    i = 2
    sign = -1
    while True:
        diff = sign*(x**i)/factorial(i)
        s = s+diff
        if abs(diff) <= error:
            return s
        i += 2
        sign *= -1


# 0 1 2 3 4 5 6 7  8  9  10
# 0,1,1,2,3,5,8,13,21,34,55

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)


def factoraial2(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n*factoraial2(n-1)
