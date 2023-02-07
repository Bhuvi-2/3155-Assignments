# Data #

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  # slice
            "ham": 4,  # slice
            "cheese": 4,  # ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  # slice
            "ham": 6,  # slice
            "cheese": 8,  # ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  # slice
            "ham": 8,  # slice
            "cheese": 12,  # ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  # slice
    "ham": 18,  # slice
    "cheese": 24,  # ounces
}


##


class SandwichMachine:

    # main constructor
    def __init__(self, machine_resources):
        self.machine_resources = machine_resources  # assigns machine_resources to itself
        self.recipes = recipes  # assigns recipes to the predefined sandwich recipes

    # method to check if there are enough resources to make the sandwich
    def check_resources(self, ingredients):
        for ingredient, amount in ingredients.items():  # for loop to traverse through the ingredients
            if self.machine_resources[ingredient] < amount:  # checks if the available ingredients are less than
                return False                                # required amount and returns false if it is, true otherwise
        return True

    # method to process the inserted coins
    def process_coins(self):
        transaction_coins = []  # an array to store the inserted coins
        nickel_input = float(input("How many nickels? ")) * 0.05         # user input for nickels
        quarter_input = float(input("How many quarters? ")) * 0.25       # user input for quarters
        half_dollar_input = float(input("How many half dollars? ")) * 0.50  # user input for half dollars
        dollar_input = float(input("How many dollars? ")) * 1            # user input for dollars
        transaction_coins.append(nickel_input)      # adds all the inserted nickels into the array
        transaction_coins.append(quarter_input)     # adds all the inserted quarters into the array
        transaction_coins.append(half_dollar_input)  # adds all the inserted half dollars into the array
        transaction_coins.append(dollar_input)      # adds all the inserted dollars into the array
        total = sum(transaction_coins)  # sums all the coins in the array
        return total    # returns the sum

    # method to verify the transaction and compare the inserted coins to the transaction cost
    def transaction_result(self, inserted_coins, transaction_price):
        if inserted_coins < transaction_price:  # returns false if  inserted coins is less than the cost of transaction
            return False
        elif inserted_coins == transaction_price:  # prints a message & returns true if  inserted money = the meal price
            return f'Thank you, that was the exact amount of coins needed for this order.'
            return True
        elif inserted_coins > transaction_price:  # provides change & returns true if  inserted money is more than the price
            change = inserted_coins - transaction_price
            return f'Here is your change of ${change}.'
            return True
        else:               # returns false otherwise
            return False

    # method to actually make the sandwich
    def make_sandwich(self, sandwich_size, order_ingredients):
        for ingredient, amount in order_ingredients.items():    # for loop to traverse through the ingredients
            self.machine_resources[ingredient] -= amount    # subtracts the amount of ingredients used to make the item

# main code to interact with the user
sandwich_machine = SandwichMachine(resources)  # makes an instance of the SandwichMachine class with the resources
while True:     # while loop to reiterate back to the main menu of options after each action
    selection = input("What would you like? (small/medium/large/off/report) ")  # asks the user what they want to do
    if selection == "off":  # turns of the machine if user wants to turn off the machine
        print("Turning off machine...")
        break
    elif selection == "report":   # prints a report of the remaining resources
        print(sandwich_machine.machine_resources)
    elif selection in sandwich_machine.recipes:     # if the user orders a sandwich
        recipe = sandwich_machine.recipes[selection]  # stores which size sandwich they ordered & maps it to the recipe
        if sandwich_machine.check_resources(recipe["ingredients"]):  # if there are enough ingredients to make the item
            cost = recipe["cost"]   # gets the cost of this item and stores it
            coins = sandwich_machine.process_coins()    # takes the money from the user
            if sandwich_machine.transaction_result(coins, cost):  # makes the sandwich & prints a message
                sandwich_machine.make_sandwich(selection, recipe["ingredients"])
                print(sandwich_machine.transaction_result(coins, cost))
                print("Your " + selection + " sandwich is ready. Enjoy!")
            else:   # error message for insufficient money
                print("Sorry, that's not enough money for this item. Your money has been refunded.")
        else:       # error message for insufficient ingredients
            print("Sorry, there are not enough ingredients to make your item at this time.")
    else:  # error message for an invalid selection from the menu of options
        print("Invalid selection. Please choose a valid option.")
