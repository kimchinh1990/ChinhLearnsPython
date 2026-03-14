class InventoryManager:

    def __init__(self):
        self.imported_products = {}

    def show_products(self):

        if not self.imported_products:
            print("Kho trống")
            return

        for index, (product_name, product_price) in enumerate(self.imported_products.items(),start=1):
            print(f"{index:>3}-{product_name:<10} {product_price:>10,}")

    def add_products(self):

        new_product_name = input("Nhập tên sản phẩm vừa mới thêm: ")
        new_product_name = new_product_name.strip().lower()

        if new_product_name in self.imported_products:
            print("Sản phẩm đã tồn tại.")
            return 

        new_product_price = int(input("Nhập giá sản phẩm vừa mới thêm: "))
        
        self.imported_products[new_product_name] = new_product_price
        print("Đã thêm sản phẩm.")

    def delete_product(self):
        
        product_to_delete = input("Nhập tên sản phẩm cần xoá: ")
        product_to_delete = product_to_delete.strip().lower()

        if product_to_delete not in self.imported_products:
            print("Không tìm thấy sản phẩm.")
            return
        
        del self.imported_products[product_to_delete]
        print("Đã xoá sản phẩm.")
        
