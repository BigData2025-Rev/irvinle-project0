import json
from pathlib import Path
from classes.inventory_manager import InventoryManager

def item_valid_checker(name, price=None, quantity=None):
    ret = True
    if len(name) < 1:
        print("\nName not valid.\n")
        ret = False
    if price != None:
        try:
            float(price)
        except ValueError:
            print("\nPrice not valid.\n")
            ret = False
        else:
            if float(price) < 0:
                print("\nPrice not valid.\n")
                ret = False
    if quantity != None:
        try:
            float(quantity)
        except ValueError:
            print("\nQuantity not valid.\n")
            ret = False
        else:
            if float(quantity) < 0 or float(quantity).is_integer() == False:
                print("\nQuantity not valid.\n")
                ret = False
    return ret

def add_item(inventory_manager):
    name = input("Name of item: ")
    price = input("Price of item: ")
    quantity = input("Quantity of item: ")
    if item_valid_checker(name, price, quantity) == False:
        return
    if name in inventory_manager.inventory:
        print("\nItem is already in the inventory.\n")
    else:
        try:
            inventory_manager.add_data(name, price, quantity)
        except:
            print("\nItem unable to be added.\n")
        else:
            print("\nItem added!\n")

def update_item(inventory_manager):
    name = input("Name of item: ")
    price = input("Price of item: ")
    quantity = input("Quantity of item: ")
    if item_valid_checker(name, price, quantity) == False:
        return
    if name not in inventory_manager.inventory:
        print("\nItem is not in the inventory.\n")
    else:
        try:
            inventory_manager.update_data(name, price, quantity)
        except:
            print("\nItem unable to be updated.\n")
        else:
            print("\nItem updated!\n")

def delete_item(inventory_manager):
    name = input("Name of item: ")
    if item_valid_checker(name) == False:
        return
    if name not in inventory_manager.inventory:
        print("\nItem is not in the inventory.\n")
    else:
        try:
            inventory_manager.delete_data(name)
        except:
            print("\nItem unable to be deleted.\n")
        else:
            print("\nItem deleted!\n")

def print_data(inventory_manager):
    for key, value in inventory_manager.inventory.items():
        print(f"Name: {key}, price: ${value["price"]:.2f}, quantity: {value["quantity"]}")

def save_file(inventory_manager):
    if not inventory_manager.filepath:
        name = input("\nNew file name: ")
        inventory_manager.filepath = f"./data/{name}.json"
    with open(inventory_manager.filepath, 'w') as file:
        json.dump(inventory_manager.inventory, file)
    print("\nFile saved! \n")


def main_menu(inventory_manager):
    while True:
        mm_input = input("\nEnter command:\n\nAdd item[a]\nUpdate item[u]\nDelete item[d]\nPrint data[p]\nSave file[s]\nQuit[q]: ")
        print()
        if (mm_input.lower()) == "q":
            break

        if (mm_input.lower()) == "a":
            add_item(inventory_manager)
        elif (mm_input.lower()) == "u":
            update_item(inventory_manager)
        elif (mm_input.lower()) == "d":
            delete_item(inventory_manager)
        elif (mm_input.lower()) == "p":
            print_data(inventory_manager)
        elif (mm_input.lower()) == "s":
            save_file(inventory_manager)

if __name__ == "__main__":
    Path("data").mkdir(exist_ok=True)

    while True:
        f_input = input("\nInsert inventory file name\nOr press enter for a new file\nOr press q to quit: ")
        if (f_input.lower()) == "q":
            break

        if (f_input) == "":
            im = InventoryManager()
        else:
            filepath = f"./data/{f_input}.json"
            if Path(filepath).exists() == False:
                print("\nFile doesnt exist!")
                continue
            with open(filepath, 'r') as file:
                inventory = json.load(file)
            im = InventoryManager(filepath, inventory)

        main_menu(im)
