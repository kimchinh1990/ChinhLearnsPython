import json
import os

def load_data(filename):

    base_dir = os.path.dirname(__file__)
    file_path = os.path.join(base_dir, filename)

    if not os.path.exists(file_path):
        return {}

    with open(file_path, "r", encoding="utf-8") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return {}

def save_data(filename, data):

    base_dir = os.path.dirname(__file__)
    file_path = os.path.join(base_dir, filename)

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
