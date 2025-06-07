def display_menu():
    """Displays the shopping list manager menu options"""
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def get_numeric_choice(prompt, min_val, max_val):
    """Gets and validates numeric input from user"""
    while True:
        choice = input(prompt)
        if choice.isdigit():
            num = int(choice)
            if min_val <= num <= max_val:
                return num
        print(f"Invalid input. Please enter a number between {min_val} and {max_val}.")

def main():
    """Main function to manage the shopping list"""
    shopping_list = []  # Initialize empty shopping list array
    
    while True:
        display_menu()  # Call the menu display function
        
        # Get validated numeric choice
        choice = get_numeric_choice("Enter your choice (1-4): ", 1, 4)

        if choice == 1:
            # Add item
            item = input("Enter the item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"'{item}' added to shopping list.")
            else:
                print("Item name cannot be empty.")
                
        elif choice == 2:
            # Remove item
            if not shopping_list:
                print("Shopping list is empty.")
                continue
                
            print("Current items:")
            for i, item in enumerate(shopping_list, 1):
                print(f"{i}. {item}")
                
            item_num = get_numeric_choice(
                "Enter item number to remove (0 to cancel): ",
                0, len(shopping_list)
            )
            
            if item_num > 0:
                removed = shopping_list.pop(item_num-1)
                print(f"Removed '{removed}' from shopping list.")
                
        elif choice == 3:
            # View list
            if shopping_list:
                print("\nCurrent Shopping List:")
                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")
            else:
                print("Your shopping list is empty.")
                
        elif choice == 4:
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()