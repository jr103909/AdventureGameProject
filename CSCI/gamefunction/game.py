"""Game Main File.

This file imports functions from gamefunctions.py and allows for user
interaction to play the game.
"""

import random

from gamefunctions import (
    print_welcome,
    print_shop_menu,
    purchase_item,
    new_random_monster,
    display_fight_statistics,
    get_user_fight_options,
    equip_item,
    use_consumable,
    sleep_and_restore_hp,  # Assuming you added the sleep function in gamefunctions.py
)

def main():
    """Main function to run the game."""
    name = input("Enter your name: ")
    print_welcome(name)

    current_hp = 30
    current_gold = 10
    max_hp = 30  # Add a max_hp variable for the player's health
    starting_money = 30.00
    print(f"You have ${starting_money:.2f} to spend.")

    inventory = []  # Initialize inventory
    current_weapon = None  # No weapon initially

    print_shop_menu("Sword", 15.00, "Scroll of Death", 5.00)

    # Purchasing items
    choice = input("What would you like to buy? (1 for Sword, 2 for Scroll of Death): ")
    if choice == '1':
        quantity = int(input("How many Swords would you like to buy? "))
        number_bought, remaining_money = purchase_item(15.00, starting_money, quantity)
        for _ in range(number_bought):
            inventory.append({"name": "Sword", "type": "weapon", "maxDurability": 10, "currentDurability": 10})
    elif choice == '2':
        quantity = int(input("How many Scrolls of Death would you like to buy? "))
        number_bought, remaining_money = purchase_item(5.00, starting_money, quantity)
        for _ in range(number_bought):
            inventory.append({"name": "Scroll of Death", "type": "consumable"})

    while True:
        print(f"\nCurrent HP: {current_hp}, Current Gold: {current_gold}")
        choice = input("What would you like to do?\n1) Fight Monster\n2) Equip Item\n3) Visit Shop\n4) Sleep\n5) Quit\n")

        if choice == '1':
            # When the player chooses to fight, we call fight_monster
            current_hp, current_gold = fight_monster(current_hp, current_gold, inventory, max_hp, current_weapon)
        elif choice == '2':
            current_weapon = equip_item(inventory)  # Equip item and update current_weapon
        elif choice == '3':
            print_shop_menu("Sword", 15.00, "Scroll of Death", 5.00)
            choice = input("What would you like to buy? (1 for Sword, 2 for Scroll of Death): ")
            if choice == '1':
                quantity = int(input("How many Swords would you like to buy? "))
                number_bought, remaining_money = purchase_item(15.00, starting_money, quantity)
                for _ in range(number_bought):
                    inventory.append({"name": "Sword", "type": "weapon", "maxDurability": 10, "currentDurability": 10})
            elif choice == '2':
                quantity = int(input("How many Scrolls of Death would you like to buy? "))
                number_bought, remaining_money = purchase_item(5.00, starting_money, quantity)
                for _ in range(number_bought):
                    inventory.append({"name": "Scroll of Death", "type": "consumable"})
        elif choice == '4':
            current_hp = max_hp  # Restore full HP when sleeping
            print("You slept and restored your health!")
        elif choice == '5':
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice, please try again.")

def fight_monster(player_hp, player_gold, inventory, max_hp, current_weapon):
    """Function to handle fighting a monster."""
    monster = new_random_monster()  # Get a random monster
    monster_hp = monster['health']
    print(f"You encounter a {monster['name']}! {monster['description']}")

    initial_hp = player_hp  # Store the initial HP before the fight

    while monster_hp > 0 and player_hp > 0:
        display_fight_statistics(player_hp, monster, player_gold)

        action = get_user_fight_options()
        if action == 1:  # Fight
            if "Sword" in [item['name'] for item in inventory]:
                sword = next(item for item in inventory if item['name'] == "Sword")
                if sword['currentDurability'] > 0:
                    damage_to_monster = random.randint(10, 20)
                    monster_hp -= damage_to_monster
                    sword['currentDurability'] -= 1
                    print(f"You dealt {damage_to_monster} damage to the {monster['name']}! Remaining durability: {sword['currentDurability']}")
                else:
                    print("Your sword is dull and cannot be used!")
                    continue
            else:
                damage_to_monster = 5
                monster_hp -= damage_to_monster

            damage_to_player = monster['power']
            player_hp -= damage_to_player
            print(f"The {monster['name']} dealt {damage_to_player} damage to you!")

            if monster_hp <= 0:
                print(f"You defeated the {monster['name']}!")
                player_gold += monster['money']  # Add gold from monster
            if player_hp <= 0:
                print("You have been defeated!")
                break
        elif action == 2:  # Run Away
            print("You ran away safely!")
            break
        elif action == 3:  # Use Scroll of Death
            player_hp, gold_from_monster = use_consumable(inventory, player_hp, monster, max_hp)  # Fix here!
            player_gold += gold_from_monster  # Add gold from monster when using Scroll of Death
            print(f"You have {player_gold} gold now!")

            # Monster is defeated instantly
            monster_hp = 0  # Set monster HP to 0 to end the fight

    return player_hp, player_gold


if __name__ == "__main__":
    main()
