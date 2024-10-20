<<<<<<< HEAD
"""Game Functions Module.

This module provides functions for a game, including welcoming
the player, displaying a shop menu, processing item purchases, and
generating random monsters.

Functions:
    print_welcome(name: str, width: int = 20) -> None
    print_shop_menu(item1Name: str, item1Price: float, item2Name: str, item2Price: float) -> None
    purchase_item(itemPrice: float, startingMoney: float, quantityToPurchase: int = 1) -> tuple
    new_random_monster() -> dict

Typical usage example:

    >>> print_welcome("Player")
"""

import random

def print_welcome(name: str, width: int = 20) -> None:
    """Prints a welcome message centered within a specified width.

    Parameters:
        name (str): The name to include in the welcome message.
        width (int): The total width for centering the message (default 20).
=======
#gamefunctions.py
#James Rogan
#9/29/2024

import random

#returns number of items purchased and quantity of money remaining


#defines parameters
def purchase_item(itemPrice , startingMoney , quantityToPurchase=1):
    itemPrice = float(itemPrice)
    startingMoney = float(startingMoney)
    quantityToPurchase = int(quantityToPurchase)

#determines maximum of items one can purchase

    maxItems = int(startingMoney // itemPrice)
    numberBought = min(maxItems, quantityToPurchase)
    remainingMoney = round(startingMoney - (numberBought * itemPrice), 2)

#returns number of items bought and money left over
    
    return numberBought, remainingMoney
    

# creates a random monster, represented as a dictionary with the properties name, description health, power, and money

def new_random_monster():
    monster_manual = [
        {"name": "Beholder",
         "description": "Beholders cast spells through their many eyes.",
         "health": random.randint(150,200),
         "power": random.randint(50,100),
         "money": random.randint (100,1000)
         },
         {"name": "Kobold",
         "description": "Kobolds make up for their physical ineptitude with a cleverness for trap making.",
         "health": random.randint(10,20),
         "power": random.randint(1,10),
         "money": random.randint(1,5)
         },
          {"name": "Tarrasque",
         "description": "The Tarrasque is a legendary creature of immense size and power.",
         "health": random.randint(650,700),
         "power": random.randint(500,1000),
         "money": random.randint(1000,10000)
         }
    ]
#returns random monster
    return random.choice(monster_manual)

#prints three examples for number bought and remaining money given different variables from given ranges
if __name__ == "__main__":
    for i in range(3):
        
        item_price = random.uniform(1.0, 10.0)  
        starting_money = random.uniform(10.0, 50.0)  
        quantity_to_purchase = random.randint(1, 5)  

        number_bought, remaining_money = purchase_item(item_price, starting_money, quantity_to_purchase)
        print(f'Thanks for shopping! Items bought: {number_bought}, Remaining money: {remaining_money:.2f}')

#prints three random monsters from dictionaries
for i in range(3):
    random_monster = new_random_monster()
    print(f'Random Monster {i + 1}:', random_monster)

def print_welcome(name, width=20):
    """Prints a welcome for the supplied 'name' parameter.
    The output is centered within a 20-character field.

    Arguments:
        name (str): the name included in the welcome message.
        width (int): the total width for centering the message (default 20)
>>>>>>> 6925db6a3f6fd2f4ad97bb9e2ba11e96924cb948

    Returns:
        None
    """
<<<<<<< HEAD
    message = f"Hello, {name}!"
    print(message.center(width))

def print_shop_menu(item1Name: str, item1Price: float, item2Name: str, item2Price: float) -> None:
    """Displays a shop menu with item names and prices.

    Parameters:
        item1Name (str): The name of the first item.
        item1Price (float): The price of the first item.
        item2Name (str): The name of the second item.
        item2Price (float): The price of the second item.
=======

    message = f"Hello, {name}!"
    print(message.center(width))
    
    
print_welcome("Bo")
print_welcome("Alexander")
print_welcome("Carl")

def print_shop_menu(item1Name, item1Price, item2Name, item2Price):
    """Prints a shop menu that contains a list of two items and their corresponding prices.
    Arguments:
        item1Name (str): The name of the first item.
        item1Price (float): The price of the first item.
        item2Name (str): The name of the second item.
        item2Price (float): The name of the second item.
>>>>>>> 6925db6a3f6fd2f4ad97bb9e2ba11e96924cb948

    Returns:
        None
    """
<<<<<<< HEAD
=======

>>>>>>> 6925db6a3f6fd2f4ad97bb9e2ba11e96924cb948
    print("/----------------------\\")
    print(f"| {item1Name:<12} ${item1Price:>6.2f} |")
    print(f"| {item2Name:<12} ${item2Price:>6.2f} |")
    print("\\----------------------/")

<<<<<<< HEAD
def purchase_item(itemPrice: float, startingMoney: float, quantityToPurchase: int = 1) -> tuple:
    """Calculates the number of items that can be purchased and remaining money.

    Parameters:
        itemPrice (float): The price of the item.
        startingMoney (float): The initial amount of money.
        quantityToPurchase (int): The desired quantity to purchase.

    Returns:
        tuple: Number of items bought and remaining money.
    """
    maxItems = int(startingMoney // itemPrice)
    numberBought = min(maxItems, quantityToPurchase)
    remainingMoney = round(startingMoney - (numberBought * itemPrice), 2)

    return numberBought, remainingMoney

def new_random_monster() -> dict:
    """Creates and returns a random monster with various attributes.

    Returns:
        dict: A dictionary containing the monster's name, description,
        health, power, and money.
    """
    monster_manual = [
        {
            "name": "Beholder",
            "description": "Beholders cast spells through their many eyes.",
            "health": random.randint(150, 200),
            "power": random.randint(50, 100),
            "money": random.randint(100, 1000)
        },
        {
            "name": "Kobold",
            "description": "Kobolds make up for their physical ineptitude with a cleverness for trap making.",
            "health": random.randint(10, 20),
            "power": random.randint(1, 10),
            "money": random.randint(1, 5)
        },
        {
            "name": "Tarrasque",
            "description": "The Tarrasque is a legendary creature of immense size and power.",
            "health": random.randint(650, 700),
            "power": random.randint(500, 1000),
            "money": random.randint(1000, 10000)
        }
    ]
    return random.choice(monster_manual)

def test_functions():
    """Runs test cases for the module functions."""
    print_welcome("Player")
    print_shop_menu("Potion", 9.27, "Apple", 1.23)
    number_bought, remaining_money = purchase_item(5.00, 20.00, 4)
    print(f'Items bought: {number_bought}, Remaining money: {remaining_money:.2f}')
    random_monster = new_random_monster()
    print(f'Random Monster: {random_monster}')

if __name__ == "__main__":
    test_functions()
=======
print_shop_menu("Potion", 9.267, "Apple", 1.234)
print_shop_menu("Egg", .23, "Elixir", 8.145)
print_shop_menu("Copper Arrow", 3.5, "Iron Arrow", 5.991)
    


>>>>>>> 6925db6a3f6fd2f4ad97bb9e2ba11e96924cb948
