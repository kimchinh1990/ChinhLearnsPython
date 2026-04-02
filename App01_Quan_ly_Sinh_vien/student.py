class Student:
    
    def __init__(self, student_id, name, age, major, gpa):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.major = major
        self.gpa = gpa

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "major": self.major,
            "gpa": self.gpa
        }
    
    @staticmethod
    def from_dict(data):
        return Student(
            data["student_id"],
            data["name"],
            data["age"],
            data["major"],
            data["gpa"]
        )