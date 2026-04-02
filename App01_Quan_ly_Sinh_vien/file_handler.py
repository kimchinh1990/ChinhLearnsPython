import json
import os

FILE_NAME = "students.json"

def load_data():

    base_dir = os.path.dirname(__file__)
    file_path = os.path.join(base_dir, FILE_NAME)

    if not os.path.exists(file_path):
        return []

    with open(file_path, "r") as file:
        try:
            return json.load(file)
        except:
            return []

def save_data(students):
    base_dir = os.path.dirname(__file__)
    file_path = os.path.join(base_dir, FILE_NAME)
    
    data = []
    for s in students:
        data.append({
            "student_id": s.student_id,
            "name": s.name,
            "age": s.age,
            "major": s.major,
            "gpa": s.gpa
        })
        
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)