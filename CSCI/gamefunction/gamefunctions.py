
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
            choice = int(input("What would you like to do?\n1) Fight Monster\n2) Run Away\n> "))
            if choice in (1, 2):
                return choice
            else:
                print("Invalid choice. Please choose 1 or 2.")
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

def fight_monster(player_hp: int, player_gold: int) -> int:
    """Handles the logic for fighting a monster."""
    monster = new_random_monster()
    monster_health = monster['health']
    
    while player_hp > 0 and monster_health > 0:
        display_fight_statistics(player_hp, monster, player_gold)  # Include player_gold here

        action = get_user_fight_options()
        
        if action == 1:  # Fight
            damage_to_monster = random.randint(10, 20)  # Damage dealt to monster
            damage_to_player = monster['power']
            monster_health -= damage_to_monster
            player_hp -= damage_to_player
            
            print(f"You dealt {damage_to_monster} damage to the {monster['name']}!")
            print(f"The {monster['name']} dealt {damage_to_player} damage to you!")
            
            # Display current HP after the attack
            print(f"Current HP: {player_hp}, {monster['name']} HP: {monster_health}")
            
            # Check if the monster is defeated
            if monster_health <= 0:
                print(f"You defeated the {monster['name']}!")
                player_gold += monster['money']  # Gain money after defeating the monster
                return player_hp  # Return current HP after victory

        elif action == 2:  # Run Away
            print("You ran away safely!")
            return player_hp  # Return current HP after fleeing
        
        # Check if player is still alive to present sleep option
        if player_hp > 0:
            sleep_choice = input("Would you like to sleep to restore HP for 5 Gold? (y/n) ").lower()
            if sleep_choice == 'y' and player_gold >= 5:
                player_hp = min(player_hp + 10, 50)  # Restore HP, max 50
                player_gold -= 5
                print("You slept and restored 10 HP!")
            elif sleep_choice == 'y':
                print("Not enough gold to sleep.")
    
    if player_hp <= 0:
        print("You have been defeated!")
    return player_hp

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
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    print_welcome("Player")
    main_game_loop()
