"""
THE ANIMAL SIMULATOR GAME 2.0
by: Talyn
created on: 03/06/2025
last edited on: 03/13/2025
"""

import random
import json
from database import (
    clear_data,
    has_existing_data,
    create_grid,
    add_animal,
)
from animals import SpeciesChar, assign_temper, coat_color

"""COLOR CODE"""


def comp(text):
    print("\033[94m" + text + "\033[0m")  # 94 = Blue, 0 = Reset color


def quest(prompt, color_code="\033[92m"):  # 92 = green
    return input(f"{color_code}{prompt}\033[0m")


def shoot(text):
    print("\033[91m" + text + "\033[0m")  # 91 = red, yada yada


def initialize_animals():
    # Keep track of the next available ID for wolves and elk
    wolf_count = 1  # Start with W1
    elk_count = 1  # Start with E1

    wolves = int(quest("How many wolves will you start with? (up to 3):"))
    for i in range(1, wolves + 1):
        gender = quest(f"What is wolf {i}'s gender? (male or female)").lower()
        build = quest("What is this wolf's build? (small, medium, large)").lower()
        one = quest("What color coat does it have? (black, gray, white)").lower()
        two = quest("Any tint? (none, warm, earth, light)").lower()
        if one == "black":
            one = "K"
        elif one == "white":
            one = "w"
        else:
            one = "k"
        if two == "warm":
            two = "o"
        elif two == "earth":
            two = "b"
        elif two == "light":
            two = "w"
        else:
            two = one
        trait = (one, two)
        health = "healthy"
        temper = assign_temper(one, two)
        position = (random.randint(0, 10), random.randint(0, 10))
        coat = coat_color(one, two)
        tag = f"W{wolf_count}"
        add_animal(tag, "wolf", gender, build, trait, coat, None, temper, health, position)
        wolf_count += 1

    elk = int(quest("How many elk will you start with? (up to 3):"))
    for i in range(1, elk + 1):
        gender = quest(f"What is elk {i}'s gender? (male or female)").lower()
        build = quest("What is this elk's build? (small, medium, large)").lower()
        antlers = quest("What size antlers? (small, medium, large)")
        one = random.choice("K", "k")
        if one == "K":
            two = random.choice("K", "k")
        else:
            two = "k"
        trait = (one, two)
        temper = assign_temper(one, two)
        health = "healthy"
        position = (random.randint(0, 10), random.randint(0, 10))
        tag = f"E{elk_count}"
        add_animal(tag, "wolf", gender, build, trait, None, antlers, temper, health, position)
        elk_count += 1


def start_sim():
    choice = quest("Would you like to (C) continue, or (R) reset?").lower()
    if choice == "c":
        # just use the current creatures.db info
        if not has_existing_data():
            shoot("oops, looks like there's nothing to continue. Let's make a new one!")
            initialize_animals()
        comp("Resuming the simulation...")
    elif choice == "r":
        clear_data()
        initialize_animals()
    else:
        shoot("invalid choice.")
        start_sim()


if __name__ == "__main__":
    comp("Welcome to the Animal Simulator!")
    shoot("Throughout the game, make sure to spell correctly. Otherwise it'll crash!")
    start_sim()
