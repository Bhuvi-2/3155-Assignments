
class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for ingredient, amount in ingredients.items():  # for loop to traverse through the ingredients
            if self.machine_resources[ingredient] < amount:  # checks if the available ingredients are less than
                return False                                # required amount and returns false if it is, true otherwise
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        for ingredient, amount in order_ingredients.items():  # for loop to traverse through the ingredients
            self.machine_resources[ingredient] -= amount  # subtracts the amount of ingredients used to make the item
