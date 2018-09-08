import sys

print("Hello world")

x = 5
print(type(x))
x = 'teo'
print(type(x))
x = True
print(type(x))
x = 5.5
print(type(x))
x = complex(113, 114)
print(type(x))

print("=========")

# delete variable
# x = "Obama"
# print(x)
# del x
# print(x)

print("Thông tin chi tiết của int: \n")
print(sys.int_info)

print("Thông tin chi tiết của float:  \n")
print(sys.float_info)

"""
Hoc python co gi vui @@!
"""

print("Please enter input : ============")
a = int(input())
b = 5
c = a + b

print(c)

thisList = ["apple", "banana", "cherry"]
thisList.pop(0)
print(thisList)


def name():
    print("My name is Python")
    print("My name is Python")
    print("My name is Python")
    print("My name is Python")
    print("My name is Python")
    print("My name is Python")
    print("My name is Python")


name()


def getAddress(address):
    print(address)


getAddress("Ha Noi")
