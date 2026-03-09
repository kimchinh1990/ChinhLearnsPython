import json
import os 

from file_handler import load_data, save_data

# Hàm tiện ích
def is_duplicate(new_product_name):
    
    new_product_name = new_product_name.strip().lower()
    # Phần ChatGPT code
    for product_name in imported_products:
        if new_product_name == product_name.strip().lower():
            print("Sản phẩm đã tồn tại trong kho.")
            return True
    
    return False 

def show_menu():
    print("===== MENU =====")
    print("1. Xem sản phẩm")
    print("2. Thêm sản phẩm")
    print("3. Tìm sản phẩm")
    print("4. Xoá sản phẩm")
    print("5. Thoát chương trình")

def print_name_products ():
    product_index = 1
    for product in imported_products:
        print(f"{product_index}.{product} - {imported_products[product]:,} VND")
        product_index += 1

def add_product():
    new_product_name = input("Nhập tên sản phẩm vừa mới thêm: ")
    new_product_name = new_product_name.strip().lower()

    if is_duplicate(new_product_name):
        return 

    # kiểm tra sản phẩm tồn tại hay chưa
    while True:
        try:
            new_product_price = int(input("Giá của sản phẩm vừa mới thêm: "))
            if new_product_price <= 0:
                continue 
            break
        except ValueError:
            print("Giá tiền của sản phẩm phải là số.")
        
    imported_products[new_product_name] = new_product_price

    save_data(imported_products)

def delete_product():
    product_to_delete = input("Nhập tên sản phẩm cần xoá: ")
    product_to_delete = product_to_delete.strip().lower()
    
    if product_to_delete in imported_products:
        del imported_products[product_to_delete]
        print("Đã xoá sản phẩm bạn yêu cầu")
    else:
            print("Sản phẩm không tồn tại để xoá.")

    save_data()

def find_product_by_name():
    search_product_name = input("Nhập tên sản phẩm bạn muốn tìm: ")
    search_product_name = search_product_name.strip().lower()

    if search_product_name in imported_products:
        print(f"Sản phẩm cần tìm {search_product_name} của bạn hiện đang có trong kho.")
        print(f"Giá của nó là: {imported_products[search_product_name]:,} VND")
    else:
        print("Xin lỗi! Không tìm thấy sản phẩm bạn yêu cầu.")

def calculate_total_inventory_value():
    total_inventory_value = 0
    for product in imported_products:
        total_inventory_value += imported_products[product]
    
    print(f"Tổng giá trị sản phẩm trong kho: {total_inventory_value:,} VND")

def main_menu():
    while True:
        show_menu()

        choice = input("Nhập lựa chọn của bạn: ").strip()

        if choice == "1":
            print_name_products()
        elif choice == "2":
            add_product()
        elif choice == "3":
            find_product_by_name()
        elif choice == "4":
            delete_product()
        elif choice == "5":
            print("Thoát chương trình")
            break
        else:
            print("Lựa chọn của bạn không hợp lệ. Xin mời nhập từ 1 đến 4.")

if __name__ == "__main__":
    # print_name_products()
    # calculate_total_inventory_value()
    imported_products = load_data()
    main_menu()
