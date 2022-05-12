#Let's play with some numbers

# name = "NetworkChuck"
#
# age = 37
#
# actual_age = 39.96
#
# math = 5 ** 5
#
# results = age + actual_age + math
# print(results)


# print(name)
# print(age)
#
# print(type(name))
# print(type(age))


#Let's duild robot Barista!!!
print("Hello, welcome to NetworkChuck Coffe!!!!")
name = input("What is your name? \n")
print("Hello " + name + ", thank you so much for coming in today!")

menu = "Black Coffe, Espresso, Latte, Cuppucino"

print(name + ", what would you like from our menu today? Here is what we are serving. \n" + menu)

order = input()

price = 8

quantity = input("How many coffees would you like?\n")

total = price * int(quantity)
print("Thank you. Your total is: $" + str(total))

print("Sounds good " + name + ", we'll have your " + quantity + " " + order + " ready for in a moment.")