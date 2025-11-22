def display_menu():
    print(f"Shopping List Manager")
    print(f"1. Add Item")
    print(f"2. Remove Item")
    print(f"3. View List")
    print(f"4. Exit")

def main():
    # Array to store shopping list items
    shopping_list = []

    while True:
        display_menu()  # Calling the display_menu function
        choice = input("Enter your choice: ").strip()  # Choice input as a number (string of digits)

        if choice == '1':
            item = input("Enter the item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"'{item}' added to the list.")
            else:
                print("Item name cannot be empty.")

        elif choice == '2':
            if not shopping_list:
                print("The shopping list is empty.")
                continue
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' removed from the list.")
            else:
                print(f"'{item}' not found in the list.")

        elif choice == '3':
            if not shopping_list:
                print("The shopping list is empty.")
            else:
                print("Shopping list items:")
                for idx, item in enumerate(shopping_list, start=1):
                    print(f"{idx}. {item}")

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
