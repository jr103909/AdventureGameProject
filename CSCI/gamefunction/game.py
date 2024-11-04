
"""Game Main File.

This file imports functions from gamefunctions.py and allows for user
interaction to play the game.
"""

from gamefunctions import (
    print_welcome,
    print_shop_menu,
    purchase_item,
    new_random_monster,
    display_fight_statistics,
    get_user_fight_options,
)

def main():
    """Main function to run the game."""
    name = input("Enter your name: ")
    print_welcome(name)

    current_hp = 30
    current_gold = 10
    starting_money = 30.00  # Example starting money
    print(f"You have ${starting_money:.2f} to spend.")

    print_shop_menu("Potion", 9.27, "Apple", 1.23)

    quantity = int(input("How many Potions would you like to buy? "))
    number_bought, remaining_money = purchase_item(9.27, starting_money, quantity)
    print(f'You bought {number_bought} Potions. Remaining money: ${remaining_money:.2f}')

    while True:
        print(f"\nCurrent HP: {current_hp}, Current Gold: {current_gold}")
        choice = input("What would you like to do?\n1) Fight Monster\n2) Sleep (Restore HP for 5 Gold)\n3) Quit\n")

        if choice == '1':
            fight_monster(current_hp, current_gold)
        elif choice == '2':
            current_hp = sleep(current_hp, current_gold)
        elif choice == '3':
            print("Thank you for playing!")
            break
        else:
            print("Invalid choice, please try again.")

def fight_monster(current_hp, current_gold):
    """Function to handle fighting a monster."""
    monster = new_random_monster()
    monster_hp = 20  # Example starting HP for the monster
    print(f"You encounter a {monster['name']}! {monster['description']}")

    while monster_hp > 0 and current_hp > 0:
        damage_to_monster = 5  # Example fixed damage
        damage_to_player = 3  # Example fixed damage

        monster_hp -= damage_to_monster
        current_hp -= damage_to_player

        display_fight_statistics(current_hp, monster_hp)

        action = get_user_fight_options()
        if action == 'run':
            print("You ran away!")
            break

    if current_hp <= 0:
        print("You have been defeated!")
    elif monster_hp <= 0:
        print(f"You defeated the {monster['name']}!")

def sleep(current_hp, current_gold):
    """Function to restore HP."""
    if current_gold >= 5:
        current_hp = min(current_hp + 10, 30)  # Restore 10 HP, max 30
        current_gold -= 5
        print("You slept and restored HP.")
    else:
        print("Not enough gold to sleep.")
    return current_hp

if __name__ == "__main__":
    main()
