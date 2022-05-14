print("Hello, welcome to NetworkChuck Coffe!!!!")

name = input("What is your name? \n")
if  name == "Ben" or name == "ben" or name == "Patricia" or name == "Loki":
    evil_status = input("Are you evil?\n")

    good_deeds = int(input("How many good deeds have you done today? \n"))

    if evil_status == "Yes" or evil_status == "yes" and good_deeds < 4:
        print("You're not welcome here Evil " + name + " Get out!")
        exit()
    else:
        print(name + " yuo can came in today. ")

else:
    print("Hello " + name + ", thank you so much for coming in today!")
    menu = "Black Coffee, Espresso, Latte, Cuppuccino, Frappuccino"

    print(name + ", what would you like from our menu today? Here is what we are serving. \n" + menu)

    order = input()
    if order == "Frappuccino":
        price = 13
    elif order == "Black Coffee":
        price = 3
    elif order == "Latte":
        price = 6
    elif order == "Cuppuccino":
        price = 8
    else:
        print("Sorry we don't have that here.")
        price = 0
        exit()
    quantity = input("How many coffees would you like?\n")



    total = price * int(quantity)
    print("Thank you. Your total is: $" + str(total))

    print("Sounds good " + name + ", we'll have your " + quantity + " " + order + " ready for in a moment.")
