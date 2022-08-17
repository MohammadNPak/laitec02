def add(x, y=2, *args, **kwargs):
    print(args)
    print(kwargs)
    return x+y


z = add(1, 2)
a = add(1, 2, 3, 4, d=4)
print(z)
print(a)


def simple_decorator(f):
    def wraper():
        print("hello start decoration")
        f()
        print("end decoration")
    return wraper

@simple_decorator
def func():
    print("hello from func")


func()