
def list_3_so():
    numbers = [1, 2, 3]
    i = 1
    total = 0
    for num in numbers:
        print(f"Số thứ {i} là {num}")
        i += 1
        total += num

    print(f"Tổng {i-1} số là {total}")

def list_5_so():
    numbers = []

    for _ in range(5):
        num = int(input("Nhập số: "))
        numbers.append(num)
    
    print(f"Tổng các số đã nhập: {sum(numbers)}")
    print(f"Số lớn nhất là: {max(numbers)}")
    print(f"Số nhỏ nhất là: {min(numbers)}")

if __name__ == "__main__":
    #list_3_so()
    list_5_so()
