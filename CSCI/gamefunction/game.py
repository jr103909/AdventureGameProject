"""Game Main File.

This file imports functions from gamefunctions.py and allows for user
interaction to play the game.
"""

import random
import os
from gamefunctions import (
    print_welcome,
    print_shop_menu,
    purchase_item,
    new_random_monster,
    display_fight_statistics,
    get_user_fight_options,
    equip_item,
    use_consumable,
    sleep_and_restore_hp,  
    load_game,             
    save_game,             
)

def main():
    """Main function to run the game."""
    # Ask the user if they want to load a game or start a new one
    choice = input("Welcome to the Adventure Game! Do you want to (1) Start a new game or (2) Load a saved game? ")
    
    if choice == '2':
        filename = input("Enter the name of the save file to load: ")
        saved_data = load_game(filename)
        if saved_data:
            # Restore the player data from the loaded game
            name = saved_data["name"]
            current_hp = saved_data["current_hp"]
            current_gold = saved_data["current_gold"]  # Get the saved gold amount
            max_hp = saved_data["max_hp"]
            inventory = saved_data["inventory"]
            current_weapon = saved_data["current_weapon"]
        else:
            # If no valid save file was found, start a new game
            name = input("Enter your name: ")
            current_hp = 30
            current_gold = 10  # Default starting gold for a new game
            max_hp = 30
            inventory = []
            current_weapon = None
            print_welcome(name)
    else:
        # Start a new game
        name = input("Enter your name: ")
        current_hp = 30
        current_gold = 10  # Default starting gold for a new game
        max_hp = 30
        inventory = []
        current_weapon = None
        print_welcome(name)

    # Use current_gold from the saved data (if loading a game)
    print(f"You have ${current_gold:.2f} to spend.")  # Show the gold that was loaded from the save
    print_shop_menu("Sword", 15.00, "Scroll of Death", 5.00)

    # Purchasing items
    choice = input("What would you like to buy? (1 for Sword, 2 for Scroll of Death, 0 for nothing): ")
    if choice == '1':
        quantity = int(input("How many Swords would you like to buy? "))
        number_bought, remaining_money = purchase_item(15.00, current_gold, quantity)
        for _ in range(number_bought):
            inventory.append({"name": "Sword", "type": "weapon", "maxDurability": 10, "currentDurability": 10})
    elif choice == '2':
        quantity = int(input("How many Scrolls of Death would you like to buy? "))
        number_bought, remaining_money = purchase_item(5.00, current_gold, quantity)
        for _ in range(number_bought):
            inventory.append({"name": "Scroll of Death", "type": "consumable"})
    elif choice == '0':
        print("You chose not to buy anything.")
    else:
        print("Invalid choice. Please choose a valid option.")

    while True:
        print(f"\nCurrent HP: {current_hp}, Current Gold: {current_gold}")
        choice = input("What would you like to do?\n1) Fight Monster\n2) Equip Item\n3) Visit Shop\n4) Sleep\n5) Save and Quit\n6) Quit\n")

        if choice == '1':
            # When the player chooses to fight, call fight_monster
            current_hp, current_gold = fight_monster(current_hp, current_gold, inventory, max_hp, current_weapon)
        elif choice == '2':
            current_weapon = equip_item(inventory)  # Equip item and update current_weapon
        elif choice == '3':
            print_shop_menu("Sword", 15.00, "Scroll of Death", 5.00)
            choice = input("What would you like to buy? (1 for Sword, 2 for Scroll of Death, 0 for nothing): ")
            if choice == '1':
                quantity = int(input("How many Swords would you like to buy? "))
                number_bought, remaining_money = purchase_item(15.00, current_gold, quantity)
                for _ in range(number_bought):
                    inventory.append({"name": "Sword", "type": "weapon", "maxDurability": 10, "currentDurability": 10})
            elif choice == '2':
                quantity = int(input("How many Scrolls of Death would you like to buy? "))
                number_bought, remaining_money = purchase_item(5.00, current_gold, quantity)
                for _ in range(number_bought):
                    inventory.append({"name": "Scroll of Death", "type": "consumable"})
            elif choice == '0':
                print("You chose not to buy anything.")
        elif choice == '4':
            current_hp = max_hp  # Restore full HP when sleeping
            print("You slept and restored your health!")
        elif choice == '5':
            # Save the game before quitting
            save_filename = input("Enter the filename to save your game: ")
            player_data = {
                "name": name,
                "current_hp": current_hp,
                "current_gold": current_gold,  # Save the correct current_gold
                "max_hp": max_hp,
                "inventory": inventory,
                "current_weapon": current_weapon
            }
            save_game(save_filename, player_data)
            print("Game saved successfully.")
            break
        elif choice == '6':
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

    return player_hp, player_gold

if __name__ == "__main__":
    main()
