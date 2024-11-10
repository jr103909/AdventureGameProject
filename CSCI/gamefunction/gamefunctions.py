import random

def print_welcome(name: str, width: int = 20) -> None:
    """Prints a welcome message centered within a specified width."""
    message = f"Hello, {name}!"
    print(message.center(width))

def new_random_monster() -> dict:
    """Creates and returns a random monster with various attributes."""
    monster_manual = [
        {
            "name": "Beholder",
            "description": "Beholders cast spells through their many eyes.",
            "health": random.randint(40, 70),  # Original health
            "power": random.randint(15, 25),   # Original power
            "money": random.randint(100, 500)  # Original reward
        },
        {
            "name": "Kobold",
            "description": "Kobolds make up for their physical ineptitude with a cleverness for trap making.",
            "health": random.randint(5, 10),  # Original health
            "power": random.randint(1, 3),    # Original power
            "money": random.randint(1, 3)     # Original reward
        },
        {
            "name": "Tarrasque",
            "description": "The Tarrasque is a legendary creature of immense size and power.",
            "health": random.randint(400, 600),  # Original health
            "power": random.randint(60, 100),    # Original power
            "money": random.randint(500, 1000)   # Original reward
        }
    ]
    return random.choice(monster_manual)

def display_fight_statistics(player_hp: int, monster: dict, player_gold: int) -> None:
    """Displays the current fight statistics including player HP and monster details."""
    print(f"\nCurrent HP: {player_hp}, Current Gold: {player_gold}")
    print(f"A wild {monster['name']} appears with {monster['health']} HP!")

def get_user_fight_options() -> int:
    """Prompts the user for their action during a fight and validates input."""
    while True:
        try:
            choice = int(input("What would you like to do?\n1) Fight Monster\n2) Run Away\n3) Use Scroll of Death\n> "))
            if choice in (1, 2, 3):
                return choice
            else:
                print("Invalid choice. Please choose 1, 2, or 3.")
        except ValueError:
            print("Please enter a valid number.")

def purchase_item(item_price: float, player_gold: float, quantity: int) -> tuple:
    """Handles the purchasing of items and returns the number of items bought and remaining gold."""
    total_cost = item_price * quantity
    if total_cost <= player_gold:
        player_gold -= total_cost
        return quantity, player_gold
    else:
        print("Not enough gold to purchase that item.")
        return 0, player_gold  # Return 0 items bought if not enough gold

def equip_item(inventory):
    """Allows the user to equip a weapon from their inventory."""
    weapons = [item for item in inventory if item['type'] == 'weapon']
    if not weapons:
        print("You have no weapons to equip.")
        return None
    print("Available weapons to equip:")
    for i, weapon in enumerate(weapons, start=1):
        print(f"{i}) {weapon['name']} (Durability: {weapon['currentDurability']})")
    choice = int(input("Choose a weapon to equip (or 0 to cancel): "))
    if choice > 0 and choice <= len(weapons):
        equipped_weapon = weapons[choice - 1]
        print(f"You equipped the {equipped_weapon['name']}!")
        return equipped_weapon  # Return the equipped weapon
    else:
        print("Invalid choice.")
        return None

def use_consumable(inventory, current_hp, monster, max_hp):
    """Uses a consumable item from the inventory."""
    consumables = [item for item in inventory if item['type'] == 'consumable']
    if consumables:
        # Use the Scroll of Death to defeat the monster instantly
        current_hp = max_hp  # Restore full HP
        inventory.remove(next(item for item in inventory if item['type'] == 'consumable'))  # Remove the used consumable
        print(f"You used a Scroll of Death and defeated the {monster['name']} instantly!")
        return current_hp, monster['money']  # Return the monster's gold
    else:
        print("You have no Scrolls of Death to use.")
    return current_hp, 0

def print_shop_menu(item1, price1, item2, price2):
    """Display the shop menu with available items and their prices."""
    print(f"\nWelcome to the shop!")
    print(f"{item1}: ${price1:.2f}")
    print(f"{item2}: ${price2:.2f}")

def game_over():
    """Displays a game-over message and exits the game."""
    print("The valiant warrior has fallen! Game Over...")
    exit()

def sleep_and_restore_hp(current_hp, max_hp):
    """Restore the player's HP to full after sleeping."""
    print("You take a restful sleep and restore all your HP!")
    return max_hp  # Restore HP to the player's max HP

def fight_monster(player_hp, player_gold, inventory, max_hp, current_weapon):
    """Function to handle fighting a monster."""
    monster = new_random_monster()
    monster_hp = monster['health']
    print(f"You encounter a {monster['name']}! {monster['description']}")

    initial_hp = player_hp  # Store the initial HP before the fight

    while monster_hp > 0 and player_hp > 0:
        display_fight_statistics(player_hp, monster, player_gold)

        action = get_user_fight_options()
        if action == 1:  # Fight
            if current_weapon:  # If the player has a weapon equipped
                if current_weapon['currentDurability'] > 0:
                    damage_to_monster = random.randint(10, 20)
                    monster_hp -= damage_to_monster
                    current_weapon['currentDurability'] -= 1
                    print(f"You dealt {damage_to_monster} damage to the {monster['name']}! Remaining durability: {current_weapon['currentDurability']}")
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
            player_hp, gold_from_monster = use_consumable(inventory, initial_hp, monster)
            player_gold += gold_from_monster  # Add gold from monster when using Scroll of Death
            print(f"You have {player_gold} gold now!")

    return player_hp, player_gold
