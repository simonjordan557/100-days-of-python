import sys

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

money = 0
selected_drink = ""

coins = {
    "quarters": {
        "worth": 0.25,
        "balance": 0
    },
    "dimes": {
        "worth": 0.10,
        "balance": 0
    },
    "nickels": {
        "worth": 0.05,
        "balance": 0
    },
    "pennies": {
        "worth": 0.01,
        "balance": 0
    }
}


# TODO: 1 - Function to prompt for user order
def get_user_order():
    customer_choice = input("What would you like? (E)spresso, (L)atte, or (C)appucino? ").lower()
    if customer_choice == "c":
        return "cappuccino"
    elif customer_choice == "l":
        return "latte"
    elif customer_choice == "e":
        return "espresso"
    elif customer_choice == "off":
        return "off"
    elif customer_choice == "report":
        return "report"
    else:
        return False


# TODO: 2 - Function to display current status
def print_status():
    for k, v in resources.items():
        if k == "water" or k == "milk":
            print(f"{k[0].upper()}{k[1:]}:\t{v}ml")
        else:
            print(f"{k[0].upper()}{k[1:]}:\t{v}g")
    print(f"Money:\t${format_decimal(money)}")


def turn_machine_off():
    sys.exit()


# TODO: 3 - Function to prompt for user payment

def get_payment(drink):
    print(f"That will be ${format_decimal(MENU[drink]['cost'])}, please.")
    for k, v in coins.items():
        v["balance"] = int(input(f"How many {k}? "))


def reset_coin_counter():
    global coins
    for k, v in coins.items():
        v["balance"] = 0


def format_decimal(s):
    return "{:.3g}".format(s)


# TODO: 4 - Function to check payment is adequate and give change

def check_payment(drink):
    global coins
    global money
    required_payment = MENU[drink]["cost"]
    total_paid = 0.00
    for k, v in coins.items():
        total_paid += (v["worth"] * v["balance"])
    if total_paid >= required_payment:
        money += required_payment
        print(f"Your change is ${format_decimal(total_paid - required_payment)}. ")
        return True
    else:
        print(f"Insufficient balance. ${format_decimal(total_paid)} returned.")
        return False


# TODO: 5 - Function to pour drink and update totals

def pour_drink(drink):
    global resources
    for k, v in MENU[drink]["ingredients"].items():
        resources[k] -= v
    print(f"Enjoy your {drink}!")


# TODO: 6 - Function to check if adequate resources for drink

def check_resources(drink):
    for k, v in MENU[drink]["ingredients"].items():
        if v > resources[k]:
            return k
    return ""


while True:
    reset_coin_counter()
    selected_drink = get_user_order()
    if not selected_drink:
        print("That is not a valid choice.")
        continue
    elif selected_drink == "off":
        turn_machine_off()
    elif selected_drink == "report":
        print_status()
        continue

    empty_ingredient = check_resources(selected_drink)
    if empty_ingredient:
        print(f"There is not enough {empty_ingredient} to make a {selected_drink}. Please choose something else.")
        continue
    else:
        get_payment(selected_drink)
    if not check_payment(selected_drink):
        continue
    else:
        pour_drink(selected_drink)
