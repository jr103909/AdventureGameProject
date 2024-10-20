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

    Returns:
        None
    """
    message = f"Hello, {name}!"
    print(message.center(width))

def print_shop_menu(item1Name: str, item1Price: float, item2Name: str, item2Price: float) -> None:
    """Displays a shop menu with item names and prices.

    Parameters:
        item1Name (str): The name of the first item.
        item1Price (float): The price of the first item.
        item2Name (str): The name of the second item.
        item2Price (float): The price of the second item.

    Returns:
        None
    """
    print("/----------------------\\")
    print(f"| {item1Name:<12} ${item1Price:>6.2f} |")
    print(f"| {item2Name:<12} ${item2Price:>6.2f} |")
    print("\\----------------------/")

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
