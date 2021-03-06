# a = 5
# N = (100,)
# WIDTH, HEIGHT = (1000, 500)
#
# def myFunc(b):
#     for x in range(b):
#         n=x+1
#         print(n, end=" ")
#     print(n)
#
# myFunc(6)


# a = 5
# N = (100,)
# WIDTH, HEIGHT = (1000, 500)
#
# def myFunc(b):
#     a = 10
#     for x in range(b):
#         n=x+1
#         print(n, end=" ")
#
# myFunc(6)
# print("\n\n%d"%(a))

# name = "Tom"
#
# def say_hi():
#     print("Hello", name)
#
# def say_bye():
#     name = "Bob"
#     print("Good bye", name)
#
# say_hi()
# say_bye()

# N = (100,)
# WIDTH, HEIGHT = (1000, 500)
#
# def myFunc(b):
#     global a
#     a = 10
#     for x in range(b):
#         n=x+1
#         print(n, end=" ")
#
# myFunc(6)
# print("\n\n%d"%(a))


# nonlocal

x = 0
def outer():
    x = 1
    def inner():
        nonlocal x
        x = 2
        print("inner:", x)

    inner()
    print("outer:", x)

outer()
print("global:", x)
