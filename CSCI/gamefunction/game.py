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
    equip_item,
    use_consumable,
)

def main():
    """Main function to run the game."""
    name = input("Enter your name: ")
    print_welcome(name)

    current_hp = 30
    current_gold = 10
    starting_money = 30.00
    print(f"You have ${starting_money:.2f} to spend.")

    inventory = []  # Initialize inventory

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
        choice = input("What would you like to do?\n1) Fight Monster\n2) Equip Item\n3) Quit\n")

        if choice == '1':
            current_hp = fight_monster(current_hp, current_gold, inventory)
        elif choice == '2':
            equip_item(inventory)
        elif choice == '3':
            print("Thank you for playing!")
            break
        else:
            print("Invalid choice, please try again.")

def fight_monster(current_hp, current_gold, inventory):
    """Function to handle fighting a monster."""
    monster = new_random_monster()
    monster_hp = monster['health']
    print(f"You encounter a {monster['name']}! {monster['description']}")
    
    initial_hp = current_hp  # Store the initial HP before the fight

    while monster_hp > 0 and current_hp > 0:
        display_fight_statistics(current_hp, monster, current_gold)

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
            current_hp -= damage_to_player
            print(f"The {monster['name']} dealt {damage_to_player} damage to you!")

            if monster_hp <= 0:
                print(f"You defeated the {monster['name']}!")
                current_gold += monster['money']  
            if current_hp <= 0:
                print("You have been defeated!")
                break
        elif action == 2:  # Run Away
            print("You ran away safely!")
            break
        elif action == 3:  # Use Scroll of Death
            current_hp = initial_hp  # Restore to initial HP
            inventory.remove(next(item for item in inventory if item['type'] == 'consumable'))  # Remove the used scroll
            print("You used a Scroll of Death and restored your HP!")

    return current_hp

if __name__ == "__main__":
    main()
