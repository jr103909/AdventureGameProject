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
            "health": random.randint(40, 70),
            "power": random.randint(15, 25),
            "money": random.randint(100, 500)
        },
        {
            "name": "Kobold",
            "description": "Kobolds make up for their physical ineptitude with a cleverness for trap making.",
            "health": random.randint(5, 10),
            "power": random.randint(1, 3),
            "money": random.randint(1, 3)
        },
        {
            "name": "Tarrasque",
            "description": "The Tarrasque is a legendary creature of immense size and power.",
            "health": random.randint(400, 600),
            "power": random.randint(60, 100),
            "money": random.randint(500, 1000)
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
        return
    print("Available weapons to equip:")
    for i, weapon in enumerate(weapons, start=1):
        print(f"{i}) {weapon['name']} (Durability: {weapon['currentDurability']})")
    choice = int(input("Choose a weapon to equip (or 0 to cancel): "))
    if choice > 0 and choice <= len(weapons):
        equipped_weapon = weapons[choice - 1]
        print(f"You equipped the {equipped_weapon['name']}!")
    else:
        print("Invalid choice.")

def use_consumable(inventory, current_hp):
    """Uses a consumable item from the inventory."""
    consumables = [item for item in inventory if item['type'] == 'consumable']
    if consumables:
        current_hp = float('inf')  # Restore full HP for simplicity
        inventory.remove(consumables[0])  # Remove the used consumable
        print("You used a Scroll of Death and defeated the monster instantly!")
    else:
        print("You have no Scrolls of Death to use.")
    return current_hp

def print_shop_menu(item1, price1, item2, price2):
    """Display the shop menu with available items and their prices."""
    print(f"\nWelcome to the shop!")
    print(f"{item1}: ${price1:.2f}")
    print(f"{item2}: ${price2:.2f}")

def game_over():
    """Displays a game-over message and exits the game."""
    print("The valiant warrior has fallen! Game Over...")
    exit()

def main_game_loop():
    """Main loop of the game allowing player interactions and game flow."""
    player_hp = 50  # Increased HP
    player_gold = 10
    
    while True:
        print(f"\nCurrent HP: {player_hp}, Current Gold: {player_gold}")
        if player_hp <= 0:
            game_over()
        
        choice = input("What would you like to do?\n1) Fight Monster\n2) Quit\n> ")
        
        if choice == '1':
            player_hp = fight_monster(player_hp, player_gold)
            if player_hp <= 0:
                game_over()
        elif choice == '2':
            print("Thanks for playing!")
            break
