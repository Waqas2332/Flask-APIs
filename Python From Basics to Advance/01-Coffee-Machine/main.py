MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk":0
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
    "money": 0
}


while True:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    price = {}
    if choice.lower() == "report":
        for key, value in resources.items():
            if key == "coffee":
                print(f"{key.title()}: {value}g")
            elif key == "money":
                print(f"{key.title()}: ${value}")
            else:
                print(f"{key.title()}: {value}ml")
# taking money for the coffee
    elif choice.lower() in MENU.keys():
        print("Please insert coins.")
        price["quarters"] = int(input("How many quarters?: "))
        price["dimes"] = int(input("How many dimes?: "))
        price["nickles"] = int(input("How many nickles?: "))
        price["pennies"] = int(input("How many pennies?: "))

        total_price = round((price["quarters"] * .25) + (price["dimes"] * .10) + \
            (price["nickles"] * .05) + (price["pennies"] * 0.01),2)

# checking wether money is enough or not
        if total_price < MENU[choice]["cost"]:
            print("Sorry, that's not enough money. Money refunded")
            continue


# checking if material is sufficient or not
        elif MENU[choice]["ingredients"]["water"] <= resources["water"] and MENU[choice]["ingredients"]["milk"] <= resources["milk"] and MENU[choice]["ingredients"]["coffee"] <= resources["coffee"]:
            resources["water"] -= MENU[choice]["ingredients"]["water"]
            resources["coffee"] -= MENU[choice]["ingredients"]["coffee"]
            resources["milk"] -= MENU[choice]["ingredients"]["milk"]

            resources["money"] += MENU[choice]["cost"]
            
            print(f"Here is ${round((price["quarters"] * .25) + (price["dimes"] * .10) + \
            (price["nickles"] * .05) + (price["pennies"] * 0.01),2) - MENU[choice]["cost"]} in change.")
            
            print(f"Here is your {choice} ☕ Enjoy!")
        
        else:
            if MENU[choice]["ingredients"]["milk"] > resources["milk"]:
                print("Sorry, there is not enough milk.")
            elif MENU[choice]["ingredients"]["water"] > resources["water"]:
                print("Sorry, there is not enough water.")
            else:
                print("Sorry, there is not enough coffee")
    elif choice == "off":
        break
    else:
        continue