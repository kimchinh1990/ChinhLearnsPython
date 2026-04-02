from student import Student
from student_manger import StudentManager
from file_handler import load_data, save_data


stu001_Chinh = Student("BK001", "Trần Kim Chính", 20, "CS", 2.0)

data = {
    "student_id": "BK016",
    "name": "Ngô Minh Hoàng",
    "age": 18,
    "major": "AI",
    "gpa": 4.0
}

stu002_MinhHoang = stu001_Chinh.from_dict(data)

stu003_TanLoi = Student("BK003", "Lê Tấn Lợi", 20, "CS", 3.5)
stu004_TanCong = Student("BK004", "Nguyễn Tấn Công", 20, "CS", 3.8)
stu005_CaoCuong = Student("BK005", "Phạm Cao Cường", 20, "CE", 4.0)

# add student
class2028 = StudentManager()

class2028.add_student(stu001_Chinh)
class2028.add_student(stu002_MinhHoang)
class2028.add_student(stu003_TanLoi)
class2028.add_student(stu004_TanCong)
class2028.add_student(stu005_CaoCuong)

class2028.show_students()

# find student

print(class2028.find_student("BK016").name)

# delete student
class2028.delete_student("BK011")

print("CLASS 2030")
class2030 = StudentManager()
class2030.show_students()

student_data = load_data()
# print(student_data)

for item in student_data:
    class2030.add_student(Student.from_dict(item))

class2030.delete_student("S001")
class2030.show_students()

save_data(class2030.students)




