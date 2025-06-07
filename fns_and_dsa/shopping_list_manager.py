def display_menu():
    """Display the main menu options"""
    print("\n=== Shopping List Manager ===")
    print("1. Add item to shopping list")
    print("2. Remove item from shopping list")
    print("3. View current shopping list")
    print("4. Exit program")

def add_item(shopping_list):
    """Add an item to the shopping list"""
    item = input("Enter the name of the item to add: ").strip()
    if item:  # Only add if the input isn't empty
        shopping_list.append(item)
        print(f"'{item}' has been added to your shopping list.")
    else:
        print("Item name cannot be empty. Please try again.")

def remove_item(shopping_list):
    """Remove an item from the shopping list"""
    if not shopping_list:
        print("Your shopping list is empty - nothing to remove!")
        return
    
    print("Current shopping list:")
    display_list(shopping_list)
    
    item = input("Enter the name of the item to remove: ").strip()
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"'{item}' has been removed from your shopping list.")
    else:
        print(f"'{item}' was not found in your shopping list.")

def display_list(shopping_list):
    """Display all items in the shopping list"""
    if not shopping_list:
        print("Your shopping list is currently empty.")
    else:
        print("\n--- Your Shopping List ---")
        for index, item in enumerate(shopping_list, start=1):
            print(f"{index}. {item}")

def main():
    """Main program function"""
    shopping_list = []  # Start with an empty list
    
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == '1':
            add_item(shopping_list)
        elif choice == '2':
            remove_item(shopping_list)
        elif choice == '3':
            display_list(shopping_list)
        elif choice == '4':
            print("\nThank you for using Shopping List Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()