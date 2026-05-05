"""Inventory Management System

Features:
- Add/update/delete items
- Store in dictionary
- Save/load from file
"""

import json


def load_inventory(file_name="inventory.json"):
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def save_inventory(inventory, file_name="inventory.json"):
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(inventory, file, indent=2)


def main():
    inventory = load_inventory()

    while True:
        print("\n1. Add/Update  2. Delete  3. View  4. Save & Exit")
        choice = input("Choose: ").strip()

        if choice == "1":
            item = input("Item name: ").strip()
            qty = int(input("Quantity: "))
            inventory[item] = qty
            print("Item added/updated.")
        elif choice == "2":
            item = input("Item name to delete: ").strip()
            if item in inventory:
                del inventory[item]
                print("Item deleted.")
            else:
                print("Item not found.")
        elif choice == "3":
            print("Inventory:", inventory)
        elif choice == "4":
            save_inventory(inventory)
            print("Inventory saved.")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
