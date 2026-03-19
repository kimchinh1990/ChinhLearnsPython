from inventory_manager import InventoryManager

manager = InventoryManager()

while True:
    manager.show_products()
    manager.add_product()
    manager.delete_product()