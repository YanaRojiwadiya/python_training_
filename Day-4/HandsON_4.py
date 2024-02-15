"""Scenario: Bookstore Inventory Management
Problem: You are managing the inventory of a bookstore. You need to create a Python program that allows you to add new books to the inventory and
display the current inventory.

Description: 
-Program should contain add_book function which ask user name of book and in second line quantity of book. Add it in inventory dictionary
-display_inventory: Print all books currently in dict
-update_book_quantity: input book_name and updated quantity and update in dictionary.
-Application should keep running until user wants to exit

Main Options:
1. Add a book to inventory
2. Display current inventory
3. Update book quantity
4. Exit"""

inventory = {}

def add_book():
    book_name = input("enter the name of the book: ")
    quantity = int(input("quantity of the book: "))
    inventory[book_name] = quantity
    print("book added successfully")

def display_inventory():
    print("current Inventory:")
    for book, quantity in inventory.items():
        print(f"{book}: {quantity}")

def update_book_quantity():
    book_name = input("name of the book: ")
    if book_name in inventory:
        new_quantity = int(input("enter the new quantity: "))
        inventory[book_name] = new_quantity
        print("quantity updated")
    else:
        print("Book not found in inventory.")

while True:
    print("\nOptions:")
    print("1. Add a book to inventory")
    print("2. Display current inventory")
    print("3. Update book quantity")
    print("4. Exit")

    choice = input("select option: ")

    if choice == '1':
        add_book()
    elif choice == '2':
        display_inventory()
    elif choice == '3':
        update_book_quantity()
    elif choice == '4':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please choose from option 1 to 4")

    
    
