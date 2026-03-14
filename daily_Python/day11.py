from inventory_manager import InventoryManager

manager = InventoryManager()

manager.imported_products = {
    "iphone": 20000000,
    "ipad": 15000000,
    "macbook": 30000000,
    "watch": 10000000,
}

while True:

    manager.show_products()
    manager.add_products()
    manager.delete_product()


