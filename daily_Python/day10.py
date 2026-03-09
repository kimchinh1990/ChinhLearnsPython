# my_file = open("test.txt", "w")
# my_file.write("Chào Chính")
# my_file.close()

# my_file1 = open("test.txt", "r")
# data = my_file1.read()
# print(data)
# my_file1.close()

# my_file = open("test.txt", "w")
# my_file.write("Chào Chính")
# my_file.close()

# my_file2 = open("test.txt", "a")
# my_file2.write("\nTrần")
# my_file2.write("\nKim")
# my_file2.close()

# with open("test.txt", "r") as my_file3:
#     my_data = my_file3.read()
#     print(my_data)

with open("hello.txt", "w") as file:
    file.write("Tôi đang học Python")

with open("hello.txt", "a") as file:
    file.write("\nDay 10 - File handling")



