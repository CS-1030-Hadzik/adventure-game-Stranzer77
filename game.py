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
