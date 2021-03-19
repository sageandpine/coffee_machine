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

def coffee_maker():
    ON = True
    while ON:
        resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }
        ##TODO Turn off the Coffee Machine by entering "off" to the prompt at anytime
        def turn_off_machine():
            print("Powering Down.... X.X x.x x.X X.x -.- zzzzzzzzzzz")
            return not ON
        ##TODO When user enters "report" to the prompt a report should print that shows resources
        def resource_return():
            return resources

        ##TODO Program calculate the value of coins inserted
        def insert_coins():
            print("Insert coins to pay---")
            quarters = int(input("How many Quarters?  "))
            if quarters == 'return':
                print(resource_return())
            elif quarters == 'off':
                turn_off_machine()
            dimes = int(input("How many Dimes?  "))
            if dimes == 'return':
                print(resource_return())
            elif dimes == 'off':
                turn_off_machine()
            nickels = int(input("How many Nickel?  "))
            if nickels == 'return':
                print(resource_return())
            elif nickels == 'off':
                turn_off_machine()
            pennies = int(input("How many Pennies?  "))
            if pennies == 'return':
                print(resource_return())
            elif pennies == 'off':
                turn_off_machine()
            q_amount = quarters * 0.25
            d_amount = dimes * 0.10
            n_amount = nickels * 0.05
            p_amount = pennies * 0.01
            total = q_amount + d_amount + n_amount +p_amount
            ##TODO "The change should be rounded 2 decimal points
            return round(total, 2)


        ##TODO Prompt User by asking "What would you like? (espresso/latte/cappuccino):"
        drink_choice = input("Welcome to the coffee maker! What would you like? (espresso/latte/cappuccino): ").lower()
        if drink_choice == 'return':
            print(resource_return())
        elif drink_choice == 'off':
            turn_off_machine()

        ##TODO Check user input to decide what to do next
        ##TODO Check if resources sufficient
         ##TODO If there are enough resources User prompted to insert coins
                    ##TODO quarters nickles dimes pennies

        def check_resources(drink_choice):
            ##TODO If transaction successful and there are sufficient ingredients then:
            ##TODO Deduct ingredients from machines resources.
            if resources["water"] < MENU[drink_choice]["ingredients"]["water"]:
                print("Not enough water, refund issued")
                coffee_maker()
            elif resources["milk"] < MENU[drink_choice]["ingredients"]["milk"]:
                print("Not enough milk, refund issued")
                coffee_maker()
            elif resources["coffee"] < MENU[drink_choice]["ingredients"]["coffee"]:
                print("Not enough coffee, refund issued")
                coffee_maker()

            else:
                print(f"Your {drink_choice} costs ${MENU[drink_choice]['cost']} ")
                insert_coins()

        print(f"A {drink_choice} costs {MENU[drink_choice]['cost']} ")
        paid = insert_coins()

        def check_money(paid):
            sub = {}
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
                print(f"Here is ${round(change, 2)} in change")
                sub["water"] = resources["water"] - MENU[drink_choice]["ingredients"]["water"]
                sub["milk"] = resources["milk"] - MENU[drink_choice]["ingredients"]["milk"]
                sub["coffee"] = resources["coffee"] - MENU[drink_choice]["ingredients"]["coffee"]
                ## TODO If user has enough money then cost of the drink gets added to the profit
                sub["profit"] = MENU[drink_choice]['cost']
                return sub
            else:
                print("You don't have enough money. Money refunded!")
                coffee_maker()
                ##TODO If not Print "Sorry that's not enough money. Money

        print(f"You put in: ${paid}")
        resources = check_money(paid)
        print(f"Here is your {drink_choice}, Enjoy!")

        ##TODO Prompt should show every action complete

    ## TODO Make Coffee
    coffee_maker()
coffee_maker()