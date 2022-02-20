# try:
#     x = int(input("Enter the number: "))
#     x += 5
#     print(x)
# except ValueError:
#     print("Enter the exact number! ")
#     x = int(input("Enter the number: "))
#     x += 5
#     print(x)

# x = 0
# while x == 0:
#     try:
#         x = int(input("Enter a number: "))
#         x += 5
#         print(x)
#     except ValueError:
#         print("You can only enter a number!")

try:
    x = 5 / 1
    x = int(input("Enter number:"))
except ZeroDivisionError:
    print("Division by zero!")
except ValueError:
    print("Data entered incorrectly")
else:
    print("There are no errors, everything is correct.")
finally:
    print("Finally")
