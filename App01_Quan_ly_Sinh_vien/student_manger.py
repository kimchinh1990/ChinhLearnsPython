from student import Student

class StudentManager:
   
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def show_students(self):
        if not self.students:
            print("Danh sách trống")
            return

        print(f"{'MSSV':^5} | {'Họ và tên':^20} | {'Tuổi':^5} | {'Chuyên ngành':^25} | {'Điểm TK':^10}")
        for s in self.students:
            print(f"{s.student_id:^5} | {s.name:<20} | {s.age:^5} | {s.major:^25} | {s.gpa:^10}")

    def find_student(self, student_id):
        for s in self.students:
            if s.student_id == student_id:
                return s
        return None 
    
    def delete_student(self, student_id):
        student = self.find_student(student_id)
        if student:
            print(f"SV {student.name} bị buộc thôi học.")
            self.students.remove(student)
        else:
            print("Không tìm thấy SV trong danh sách.")
        

        
        