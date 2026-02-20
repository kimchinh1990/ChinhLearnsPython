imported_products = {
    "iphone": 20000000,
    "ipad": 15000000,
    "macbook": 30000000
}

def print_name_products ():
    for product in imported_products:
        print(product)

# def day08_level_1():
#     search_product_name = input("Nhập tên sản phẩm cần tìm: ")
#     for product in imported_products:
#         if product == search_product_name:
#             print("Giá tiền sản phẩm là: ", imported_products[product])
#             found = True
        
#     if not found:   
#         print("Sản phẩm tạm thời hết hàng!")

def day08_level_2():

    while True:
        search_product_name = input("Nhập tên sản phẩm cần tìm: ")
        search_product_name = search_product_name.lower()

        if search_product_name == "exit":
            print("Thoát chương trình.")
            break

        if search_product_name in imported_products:
            print("Giá tiền sản phẩm là: ", imported_products[search_product_name])
        else:
            print("Sản phẩm không tồn tại, vui lòng nhập lại")

def day08_level_3():
     while True:
        search_product_name = input("Nhập tên sản phẩm cần tìm: ")
        search_product_name = search_product_name.lower()

        if search_product_name == "exit":
            print("Thoát chương trình.")
            break

        if search_product_name in imported_products:
            price_product = imported_products[search_product_name]
            print(f"Giá tiền sản phẩm là: {price_product:,} ")
        else:
            print("Sản phẩm không tồn tại, vui lòng nhập lại") 

def add_product():
    new_product_name = input("Nhập tên sản phẩm vừa mới thêm: ")
    new_product_price = int(input("Giá của sản phẩm vừa mới thêm: "))
    
    imported_products[new_product_name] = new_product_price

def delete_product():
    product_to_delete = input("Nhập tên sản phẩm cần xoá: ")
    
    if product_to_delete in imported_products:
            del imported_products[product_to_delete]
    else:
        print("Sản phẩm không tồn tại để xoá.")

def show_menu():
    print("===== MENU =====")
    print("1. Xem sản phẩm")
    print("2. Thêm sản phẩm")
    print("3. Xoá sản phẩm")
    print("4. Thoát") 

def main_menu():
    while True:
        choice = input("Nhập lựa chọn của bạn: ").strip()

        if choice == "1":
            print_name_products()
        elif choice == "2":
            add_product()
        elif choice == "3":
            delete_product()
        elif choice == "4":
            print("Thoát chương trình")
            break

if __name__ == "__main__":
    # print_name_products()
    # day08_level_1()
    # day08_level_2()
    # day08_level_3()

    main_menu()