import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make a instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()


def main():
    while True:  # while loop to reiterate back to the main menu of options after each action
        selection = input("What would you like? (small/medium/large/off/report) ")  # asks the user what they want to do
        if selection == "off":  # turns of the machine if user wants to turn off the machine
            print("Turning off machine...")
            break
        elif selection == "report":  # prints a report of the remaining resources
            print(resources)
        elif selection in recipes:  # if the user orders a sandwich
            recipe = recipes[selection]  # stores which size sandwich they ordered & maps it to the recipe
            if sandwich_maker_instance.check_resources(
                    recipe["ingredients"]):  # if there are enough ingredients to make the item
                cost = recipe["cost"]  # gets the cost of this item and stores it
                coins = cashier_instance.process_coins()  # takes the money from the user
                if cashier_instance.transaction_result(coins, cost):  # makes the sandwich & prints a message
                    sandwich_maker_instance.make_sandwich(selection, recipe["ingredients"])
                    print(cashier_instance.transaction_result(coins, cost))
                    print("Your " + selection + " sandwich is ready. Enjoy!")
                else:  # error message for insufficient money
                    print("Sorry, that's not enough money for this item. Your money has been refunded.")
            else:  # error message for insufficient ingredients
                print("Sorry, there are not enough ingredients to make your item at this time.")
        else:  # error message for an invalid selection from the menu of options
            print("Invalid selection. Please choose a valid option.")


if __name__=="__main__":
    main()
