# Bài 01 - ngày 05

# in ra 5 * i = 

def bang_cuu_chuong():
    for i in range(1, 11):
        print(f"5 * {i} = {5*i}")

def hoi_mat_khau():
    correct_password = "123456"
    password_attempt_count = 0
    max_attempts = 3
    while password_attempt_count < max_attempts:
        entered_password = input("Nhập mật khẩu của bạn:")
        if correct_password == entered_password:
            print("Đăng nhập thành công!")
            break
        else:
            password_attempt_count += 1
            print("Sai mật khẩu, hãy thử lại!")
            print(f"Còn {max_attempts - password_attempt_count} lần thử")
    
    if password_attempt_count == 3:
        print("Tài khoản đã bị khoá!")

if __name__ == "__main__":
    #bang_cuu_chuong()
    hoi_mat_khau()
