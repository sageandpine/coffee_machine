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


##TODO Turn off the Coffee Machine by entering "off" to the prompt at anytime
def turn_off_machine():
    print("Powering Down.... X.X x.x x.X X.x -.- zzzzzzzzzzz")


##TODO When user enters "report" to the prompt a report should print that shows resources
def resource_return():
    print(resources)

##TODO Program calculate the value of coins inserted
def take_money(quarters, dimes, nickels, pennies):
    q_amount = quarters * 0.25
    d_amount = dimes * 0.10
    n_amount = nickels * 0.05
    p_amount = pennies * 0.01
    total = q_amount + d_amount + n_amount +p_amount
    return round(total, 2)


##TODO Prompt User by asking "What would you like? (espresso/latte/cappuccino):"
drink_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

if drink_choice == 'return':
    resource_return()
elif drink_choice == 'off':
    turn_off_machine()

##TODO Check user input to decide what to do next
##TODO Check if resources sufficient
 ##TODO If there are enough resources User prompted to insert coins
            ##TODO quarters nickles dimes pennies

def check_resources(drink_choice):
    ##TODO If transaction successful and there are sufficient ingredients then:
    ##TODO Deduct ingredients from machines resources.
    sub = {}
    if resources["coffee"] < MENU[drink_choice]["ingredients"]["coffee"]:
        return "Not enough coffee, refund issued"
    elif resources["water"] < MENU[drink_choice]["ingredients"]["water"]:
        return "Not enough water, refund issued"
    else:
        sub["water"] = resources["water"] - MENU[drink_choice]["ingredients"]["water"]
        sub["milk"] = resources["milk"]
        sub["coffee"] = resources["coffee"] - MENU[drink_choice]["ingredients"]["coffee"]
        ## TODO If user has enough money then cost of the drink gets added to the profit
        sub["profit"] = MENU[drink_choice]['cost']
        return sub

    elif resources["water"] < MENU[drink_choice]["ingredients"]["water"]:
        return "Not enough water, refund issued"
    elif resources["milk"] < MENU[drink_choice]["ingredients"]["milk"]:
        return "Not enough milk, refund issued"
    elif resources["coffee"] < MENU[drink_choice]["ingredients"]["coffee"]:
        return "Not enough coffee, refund issued"
    else:
        print(f"Your {drink_choice} costs ${MENU[drink_choice]['cost']} ")
        print("Insert coins to pay---")
        quarters = int(input("How many Quarters?  "))
        dimes = int(input("How many Dimes?  "))
        nickles = int(input("How many Nickel?  "))
        pennies = int(input("How many Pennies?  "))

        paid = take_money(quarters,dimes,nickles,pennies)

        print(f"Paid ${paid}")
        if paid == MENU[drink_choice]['cost']:
            sub["water"] = resources["water"] - MENU[drink_choice]["ingredients"]["water"]
            sub["milk"] = resources["milk"] - MENU[drink_choice]["ingredients"]["milk"]
            sub["coffee"] = resources["coffee"] - MENU[drink_choice]["ingredients"]["coffee"]
            ## TODO If user has enough money then cost of the drink gets added to the profit
            sub["profit"] = MENU[drink_choice]['cost']
            return sub
        elif paid > MENU[drink_choice]['cost']:
            change = paid - MENU[drink_choice]['cost']
            ##TODO Check if there is enough money to purchase the drink selected.
            ## TODO If user puts too much money the machine should offer change
            ## TODO Message "Here is $2.45 in change."
            print(f"Here is ${change} in change")
            sub["water"] = resources["water"] - MENU[drink_choice]["ingredients"]["water"]
            sub["milk"] = resources["milk"] - MENU[drink_choice]["ingredients"]["milk"]
            sub["coffee"] = resources["coffee"] - MENU[drink_choice]["ingredients"]["coffee"]
            ## TODO If user has enough money then cost of the drink gets added to the profit
            sub["profit"] = MENU[drink_choice]['cost']
            return sub
        else:
            print("You don't have enough $$$. Money refunded!")
            ##TODO If not Print "Sorry that's not enough money. Money refunded.

print(f"Before selection you have: {resources}")
print(f"Choice resources = {MENU[drink_choice]}")
resources = check_resources(drink_choice)
print(f"Adjusted numbers after a latte: {resources}")

##TODO Once resources are deducted tell user "Here is your x. Enjoy!"
print(f"Here is your {drink_choice}, Enjoy!")

def take_money():





##TODO Prompt should show every action complete

##TODO Prompt should show again to serve next customer

## TODO Reflect new balance the next report triggered

##TODO "The change should be rounded 2 decimal points

## TODO Make Coffee