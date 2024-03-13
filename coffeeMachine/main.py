MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

i=1
coffeeMoney=0.0



while i>0:
    money = 0.0
    quarters = 0
    dimes = 0
    pennies = 0
    nickles = 0
    refund = 0.0
    enough=True

    coffee=input("What would you like ?(espresso,latte.cappuccino)")

    # espresso
    if coffee=="espresso" :
        if int(resources["water"])<int(MENU["latte"]["ingredients"]["water"]):
            print("Not enough water")
            enough = False
        if int(resources["coffee"])<int(MENU["latte"]["ingredients"]["coffee"]) :
            print("Not enough coffee")
            enough = False
        if int(resources["milk"]) < int(MENU["latte"]["ingredients"]["milk"]):
            print("Not enough milk")
            enough = False

        if enough:

            print("Please insert coins")
            quarters = int(input("How many quarters "))
            dimes=int(input("How many dimes "))
            pennies = int(input("How many pennies "))
            nickles = int(input("How many nickles "))
            money+=(quarters*.25)+(dimes*.10)+(nickles*.05)+(pennies*.01)

            if money==MENU["espresso"]["cost"]:
                coffeeMoney += money

                int(resources["water"] - MENU["espresso"]["ingredients"]["water"])
                int(resources["coffee"] - MENU["espresso"]["ingredients"]["coffee"])
                print("Enjoy your coffee and have a nice day!")

            elif money>MENU["espresso"]["cost"]:
                refund=money-MENU["espresso"]["cost"]
                money-=refund
                print(str(refund)+" Has been refunded")
                coffeeMoney+=money

                int(resources["water"] - MENU["espresso"]["ingredients"]["water"])
                int(resources["coffee"] - MENU["espresso"]["ingredients"]["coffee"])
                print("Enjoy your coffee and have a nice day!")

            else:
                print("You do not have enough money")
                print(str(money) + " Has been refunded")
                money=0
                i=i+1
        else:
            print("Not enough ingredients")
            i+=1

# latte
    if coffee=="latte" :
        if int(resources["water"])<int(MENU["latte"]["ingredients"]["water"]):
            print("Not enough water")
            enough = False
        if int(resources["coffee"])<int(MENU["latte"]["ingredients"]["coffee"]) :
            print("Not enough coffee")
            enough = False
        if int(resources["milk"]) < int(MENU["latte"]["ingredients"]["milk"]):
            print("Not enough milk")
            enough = False

        if enough:
            print("Please insert coins")
            quarters = int(input("How many quarters "))
            dimes=int(input("How many dimes "))
            pennies = int(input("How many pennies "))
            nickles = int(input("How many nickles "))
            money+=(quarters*.25)+(dimes*.10)+(nickles*.05)+(pennies*.01)

            if money==MENU["latte"]["cost"]:
                coffeeMoney += money

                int(resources["water"] - MENU["latte"]["ingredients"]["water"])
                int(resources["coffee"] - MENU["latte"]["ingredients"]["coffee"])
                int(resources["milk"] - MENU["latte"]["ingredients"]["milk"])
                print("Enjoy your coffee and have a nice day!")

            elif money>MENU["latte"]["cost"]:
                refund=money-MENU["latte"]["cost"]
                money-=refund
                print(str(refund)+" Has been refunded")
                coffeeMoney+=money

                int(resources["water"] - MENU["latte"]["ingredients"]["water"])
                int(resources["coffee"] - MENU["latte"]["ingredients"]["coffee"])
                int(resources["milk"] - MENU["latte"]["ingredients"]["milk"])
                print("Enjoy your coffee and have a nice day!")

            else:
                print("You do not have enough money")
                print(str(money) + " Has been refunded")
                money=0
                i=i+1
        else:
            print("Not enough ingredients")
            i+=1

# cappuccino
    if coffee=="cappuccino" :
        if int(resources["water"])<int(MENU["latte"]["ingredients"]["water"]):
            print("Not enough water")
            enough = False
        if int(resources["coffee"])<int(MENU["latte"]["ingredients"]["coffee"]) :
            print("Not enough coffee")
            enough = False
        if int(resources["milk"]) < int(MENU["latte"]["ingredients"]["milk"]):
            print("Not enough milk")
            enough = False

        if enough:

            print("Please insert coins")
            quarters = int(input("How many quarters "))
            dimes=int(input("How many dimes "))
            pennies = int(input("How many pennies "))
            nickles = int(input("How many nickles "))
            money+=(quarters*.25)+(dimes*.10)+(nickles*.05)+(pennies*.01)

            if money==MENU["cappuccino"]["cost"]:
                coffeeMoney += money

                int(resources["water"] - MENU["cappuccino"]["ingredients"]["water"])
                int(resources["coffee"] - MENU["cappuccino"]["ingredients"]["coffee"])
                int(resources["milk"] - MENU["cappuccino"]["ingredients"]["milk"])
                print("Enjoy your coffee and have a nice day!")

            elif money>MENU["cappuccino"]["cost"]:
                refund=money-MENU["cappuccino"]["cost"]
                money-=refund
                print(str(refund)+" Has been refunded")
                coffeeMoney+=money

                int(resources["water"] - MENU["cappuccino"]["ingredients"]["water"])
                int(resources["coffee"] - MENU["cappuccino"]["ingredients"]["coffee"])
                int(resources["milk"] - MENU["cappuccino"]["ingredients"]["milk"])
                print("Enjoy your coffee and have a nice day!")

            else:
                print("You do not have enough money")
                print(str(money) + " Has been refunded")
                money=0
                i=i+1

        else:
            print("Not enough ingredients")
            i+=1
#report
    if coffee == "report":
        print("Water: "+str(resources["water"]))
        print("Milk: "+str(resources["milk"]))
        print("Coffee: "+str(resources["coffee"]))
        print(coffeeMoney)
        i = i + 1
#turn off
    if coffee == "off":
        i=0