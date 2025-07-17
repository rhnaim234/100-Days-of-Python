from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffe_maker=CoffeeMaker()
money_machine=MoneyMachine()
menu=Menu()


while True:
    options=menu.get_items()
    choice=input(f"what do yo like? ({options})").lower()
    if choice=="off":
        break
    elif choice=="report":
        coffe_maker.report()
        money_machine.report()
    elif choice=="latte" or choice == "capuccino" or choice=="espresso":
        drink=menu.find_drink(choice)
        if coffe_maker.is_resource_sufficient(drink):
           if money_machine.make_payment(drink.cost):
               coffe_maker.make_coffee(drink)

    else:
        print("invalid choice")