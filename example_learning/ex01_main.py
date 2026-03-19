import os
import json

current_dir = os.path.dirname(__file__)
file_name = os.path.join(current_dir, "ex01_data.json")

with open(file_name, "r") as file:
    data = json.load(file)

print(data)

data["áo khoác"] = 200000
data["dép"] = 80000

with open(file_name, "w") as file:
    json.dump(data, file)
        