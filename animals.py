
class SpeciesChar:
    def __init__(self, tag, species, gender, build, trait, coat, antlers, temper, health, position):
        self.tag = tag
        self.species = species
        self.gender = gender
        self.build = build
        self.trait = trait
        self.coat = coat if species == "wolf" else None
        self.antlers = antlers if species == "elk" else None
        self.temper = temper
        self.health = health
        self.position = position

import random

def coat_color(one, two):
    coat_colors = {
        "K": {"K": "jet black", "k": "black", "w": "coal", "b": "dark", "o": "russet"},
        "k": {"k": "gray", "w": "silver", "b": "brown", "o": "caramel"},
        "w": {"w": "white", "b": "tan", "o": "rose"}
    }

    return coat_colors.get(one, {}).get(two, "unknown")


def assign_temper(one, two):
    temperament_options = ["kind", "even", "aggressive"]

    if one == "K":
        if two != "k":
            probabilities = [0.7, 0.2, 0.1]
        else:
            probabilities = [0.1, 0.7, 0.2]
    else:
        probabilities = [0.1, 0.2, 0.7]

    return random.choices(temperament_options, probabilities)[0]



