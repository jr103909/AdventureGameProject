"""Game Main File.

This file imports functions from gamefunctions.py and allows for user
interaction to play the game.
"""

from gamefunctions import print_welcome, print_shop_menu, purchase_item, new_random_monster

def main():
    """Main function to run the game."""
    name = input("Enter your name: ")
    print_welcome(name)

    starting_money = 30.00  # Example starting money
    print(f"You have ${starting_money:.2f} to spend.")

    print_shop_menu("Potion", 9.27, "Apple", 1.23)

    quantity = int(input("How many Potions would you like to buy? "))
    number_bought, remaining_money = purchase_item(9.27, starting_money, quantity)
    print(f'You bought {number_bought} Potions. Remaining money: ${remaining_money:.2f}')

    random_monster = new_random_monster()
    print(f"You encounter a {random_monster['name']}! {random_monster['description']}")

if __name__ == "__main__":
    main()
