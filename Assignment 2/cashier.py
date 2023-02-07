class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        transaction_coins = []  # an array to store the inserted coins
        nickel_input = float(input("How many nickels? ")) * 0.05  # user input for nickels
        quarter_input = float(input("How many quarters? ")) * 0.25  # user input for quarters
        half_dollar_input = float(input("How many half dollars? ")) * 0.50  # user input for half dollars
        dollar_input = float(input("How many dollars? ")) * 1  # user input for dollars
        transaction_coins.append(nickel_input)  # adds all the inserted nickels into the array
        transaction_coins.append(quarter_input)  # adds all the inserted quarters into the array
        transaction_coins.append(half_dollar_input)  # adds all the inserted half dollars into the array
        transaction_coins.append(dollar_input)  # adds all the inserted dollars into the array
        total = sum(transaction_coins)  # sums all the coins in the array
        return total  # returns the sum

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins < cost:  # returns false if  inserted coins is less than the cost of transaction
            return False
        elif coins == cost:  # prints a message & returns true if  inserted money = the meal price
            return f'Thank you, that was the exact amount of coins needed for this order.'
            return True
        elif coins > cost:  # provides change & returns true if  inserted money is more than the price
            change = coins - cost
            return f'Here is your change of ${change}.'
            return True
        else:  # returns false otherwise
            return False
