# x=int(input("enter x:"))
# y=int(input("enter y:"))
# z=x/y
# print(z)

# try:
#     x = int(input("enter x:"))
#     y = int(input("enter y:"))
#     z = x / y
# except ZeroDivisionError:
#     print("enter a value greater than zero")
# except ValueError:
#     print("enter a numeric value")
# else:
#     print(z)
# finally:
#     print("completed")

# while True:
#     try:
#         x = int(input("enter x:"))
#         y = int(input("enter y:"))
#         z = x / y
#     except ZeroDivisionError:
#         print("enter a value greater than zero")
#     except ValueError:
#         print("enter a numeric value")
#     else:
#         print(z)
#         break
#     finally:
#         print("completed")

# FILE NOT FOUND ERROR
# try:
#     f=open("loop.py")
# except FileNotFoundError:
#     print("File not found")
# else:
#     print("File found")

# INDEX ERROR

list=[1,2,3,4]
try:
    print(list[6])
except IndexError:
    print("out of range")
else:
    print("found")
