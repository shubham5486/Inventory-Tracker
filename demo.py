class InventoryTracker:
    def __init__(self):
        self.inventory = {}

    def add_product(self, product_name, quantity):
        if product_name in self.inventory:
            self.inventory[product_name] += quantity
        else:
            self.inventory[product_name] = quantity
        print(f"Added {quantity} of {product_name} to the inventory.")

    def remove_product(self, product_name, quantity):
        if product_name in self.inventory and self.inventory[product_name] >= quantity:
            self.inventory[product_name] -= quantity
            print(f"Removed {quantity} of {product_name} from the inventory.")
        else:
            print(f"Not enough {product_name} in the inventory.")

    def check_inventory(self):
        print("Current inventory:")
        for item_name, quantity in self.inventory.items():
            print(f"{item_name}: {quantity}")

tracker = InventoryTracker()
tracker.add_product("television", 50)
tracker.add_product("refrigerator", 20)
tracker.remove_product("television", 10)
tracker.check_inventory()