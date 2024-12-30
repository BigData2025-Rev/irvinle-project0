class InventoryManager:
    def __init__(self, filepath=None, inventory={}):
        self.filepath = filepath
        if filepath:
            self.inventory = inventory
        else:
            self.inventory = {}

    def add_data(self, name, price, quantity):
        if name not in self.inventory:
            self.inventory[str(name)] = {"price": float(price), "quantity": int(quantity)}

    def update_data(self, name, price, quantity):
        if name in self.inventory:
            self.inventory[str(name)] = {"price": float(price), "quantity": int(quantity)}

    def delete_data(self, name):
        if name in self.inventory:
            self.inventory.pop(name)
