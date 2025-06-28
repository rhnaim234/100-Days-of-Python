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
import pyfiglet
ascii_art = pyfiglet.figlet_format("Welcome to the Coffee Machine")
print(ascii_art)


def is_resources_sufficient(ingredients):
    print(f"Ingredients : {drink['ingredients']}")
    for items in ingredients:
        if ingredients[items]>resources[items]:
            print(f"Sorry there is not enough {items}.")
            return False
    return True
profit =0
def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item]-=order_ingredients[item]
    print(f"Here is your {drink_name} ")

def coin_process():
    """Returns the total calculated from coins inserted"""
    print("Please insert coins first")
    total=int(input("How many quarters? "))*0.25
    total += int(input("How many dimes? ")) * 0.1
    total += int(input("How many nickles? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    return total
def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change")
        global profit
        profit+= drink_cost
        return True
    else:
        print("Sorry there is not enough money! Money refunded.")
        return False

while True:
    choice =input("What do you like? (Espresso/ Latte/ Cappuccino\n")
    if choice == "off":
        break
    elif choice == "report":
        print(f"water: {resources['water']} ml")
        print(f"milk: {resources['milk']} ml")
        print(f"coffee: {resources['coffee']}gm")
        print(f"Money: ${profit}")
    elif choice == "latte" or choice == "cappuccino" or choice == "espresso":
        drink=MENU[choice]
        if is_resources_sufficient(drink["ingredients"]):
           payment=coin_process()
           if is_transaction_successful(payment, drink["cost"]):
               make_coffee(choice, drink["ingredients"])
    else:
        print("Sorry wrong input")