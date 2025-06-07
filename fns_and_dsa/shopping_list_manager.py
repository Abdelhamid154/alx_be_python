# shopping_list_manager.py

def display_menu():
    print("\nShopping List Manager")
    print("1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Exit")

def add_item(shopping_list):
    item = input("Enter item to add: ").strip()
    if item:
        shopping_list.append(item)
        print(f"{item} added.")
    else:
        print("Item name cannot be empty.")

def remove_item(shopping_list):
    item = input("Enter item to remove: ").strip()
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} removed.")
    else:
        print(f"{item} not found in the list.")

def view_list(shopping_list):
    if not shopping_list:
        print("Your shopping list is empty.")
    else:
        print("Your Shopping List:")
        for i, item in enumerate(shopping_list, start=1):
            print(f"{i}. {item}")

def main():
    shopping_list = []

    while True:
        display_menu()
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_item(shopping_list)
        elif choice == "2":
            remove_item(shopping_list)
        elif choice == "3":
            view_list(shopping_list)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
