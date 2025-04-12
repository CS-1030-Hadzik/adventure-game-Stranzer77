"""
Adventure Game
Author: Scott Hadzik
Version: Final
Description:
A text-based adventure game where the player explores a mysterious forest,
collects items, and either wins or loses based on their decisions.
"""

import sys

# Define a class to store player info
class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = []  # Things the player finds
        self.health = 100  # Player starts with 100 health
        self.has_map = False
        self.has_lantern = False

# Function to welcome the player
def welcome_player():
    print("Welcome to the Adventure Game!")
    print("Your journey begins here...")
    name = input("What is your name, adventurer? ")
    print(f"\nWelcome, {name}! Your journey begins now.")
    return Player(name)

# Describe the beginning place
def describe_area():
    print("""
    You find yourself in a dark forest.
    The sound of rustling leaves fills the air.
    A faint path lies ahead, leading deeper into the unknown...
""")

# Add item to player's inventory
def add_to_inventory(player, item):
    if item not in player.inventory:
        player.inventory.append(item)
        print(f"You picked up a {item}!")

# Show inventory
def show_inventory(player):
    print(f"Inventory: {player.inventory}")

# If the player stays still, they lose health
def stay_still(player):
    print("You stay where you are. The cold saps your energy. You lose 10 health.")
    player.health -= 10
    check_lose(player)

# First path - dark woods
def explore_dark_woods(player):
    print(f"{player.name}, you step into the dark woods...")
    if "lantern" not in player.inventory:
        add_to_inventory(player, "lantern")
        player.has_lantern = True

# Second path - mountain pass
def explore_mountain_pass(player):
    print(f"{player.name}, you head toward the mountain pass...")
    if "map" not in player.inventory:
        add_to_inventory(player, "map")
        player.has_map = True

# Third path - cave
def explore_cave(player):
    if player.has_lantern:
        print(f"{player.name}, you bravely enter the dark cave, your lantern lighting the way.")
        print("Inside the cave, you find hidden treasure!")
        if "treasure" not in player.inventory:
            add_to_inventory(player, "treasure")
    else:
        print("It's too dark to explore the cave without a lantern.")
        player.health -= 10
        check_lose(player)

# Fourth path - hidden valley
def explore_hidden_valley(player):
    print(f"{player.name}, you study the map carefully...")
    if player.has_map:
        print("You discover a hidden path to a beautiful secret valley filled with rare herbs!")
        if "rare herbs" not in player.inventory:
            add_to_inventory(player, "rare herbs")
    else:
        print("You wander in circles. You can’t find the valley without a map.")
        player.health -= 10
        check_lose(player)