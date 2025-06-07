# shopping_list_manager.py

def display_menu():
    """
    Displays the main menu options to the user.
    """
    print("--- Shopping List Manager ---") # Ensure this line matches exactly
    print("1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Exit")

def shopping_list_manager():
    shopping_list = []

    while True:
        display_menu()  # Call the display_menu function
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(f"'{item}' added to the list.")
        elif choice == '2':
            item = input("Enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' removed from the list.")
            else:
                print(f"'{item}' not found in the list.")
        elif choice == '3':
            if shopping_list:
                print("\n--- Your Shopping List ---")
                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")
            else:
                print("Your shopping list is empty.")
        elif choice == '4':
            print("Exiting Shopping List Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    shopping_list_manager()