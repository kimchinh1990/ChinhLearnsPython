import json
import os

def load_data():
    base_dir = os.path.dirname(__file__)
    file_path = os.path.join(base_dir, "inventory.json")

    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            data = json.load(file)
    else:
        data = {}
    
    return data

def save_data(imported_products):
    base_dir = os.path.dirname(__file__)
    file_path = os.path.join(base_dir, "inventory.json")
    
    with open(file_path, "w") as file:
        json.dump(imported_products, file, indent=4)
