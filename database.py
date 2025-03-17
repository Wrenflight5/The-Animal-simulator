import json
import random
from animals import SpeciesChar

DB_FILE = "species.db"

def load_db():
    try:
        with open(DB_FILE, "r") as file:
            return json.load(file)  # Load JSON data into a dictionary
    except FileNotFoundError:
        return {"animals": [], "events": []}  # Default empty structure
    except json.JSONDecodeError:
        return {"animals": [], "events": []}  # Handle corrupted JSON

def has_existing_data():
    data = load_db()  # Get the JSON data as a dictionary
    return bool(data["animals"]) or bool(data["events"])  # Returns True if any animals or events exist


def save_db(data):
    with open(DB_FILE, "w") as file:
        json.dump(data, file, indent=4)
        
def add_animal(tag, species, gender, build, trait, coat, antlers, temper, health, position):
    new_animal = SpeciesChar(tag, species, gender, build, trait, coat, antlers, temper, health, position)
    data = load_db()

    data["animals"].append({
        "tag": tag,
        "species": species,
        "gender": gender,
        "build": build,
        "trait": trait,
        "coat": coat,
        "antlers": antlers,
        "temper": temper,
        "health": health,
        "position": position
    })
    save_db(data)

def create_grid(rows=10, cols=10):
    grid = [
        [None, None, None, None, None, None, None, None, None, None],  # Row 1
        [None, None, None, None, None, None, None, None, None, None],  # Row 2
        [None, None, None, None, None, None, None, None, None, None],  # Row 3
        [None, None, None, None, None, None, None, None, None, None],  # Row 4
        [None, None, None, None, None, None, None, None, None, None],  # Row 5
        [None, None, None, None, None, None, None, None, None, None],  # Row 6
        [None, None, None, None, None, None, None, None, None, None],  # Row 7
        [None, None, None, None, None, None, None, None, None, None],  # Row 8
        [None, None, None, None, None, None, None, None, None, None],  # Row 9
        [None, None, None, None, None, None, None, None, None, None]   # Row 10
    ]

def clear_data():
    save_db({"animals": [], "events": [], "grid": []})
    

