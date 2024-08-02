# Initialize the inventory as an empty list
inventory = []

def add_product():
    """Add a new product to the inventory."""
    product_name = input("Enter product name: ")
    product_id = input("Enter product ID: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price: "))

    # Create a dictionary for the new product
    product = {
        'name': product_name,
        'id': product_id,
        'quantity': quantity,
        'price': price
    }

    # Add the product to the inventory
    inventory.append(product)
    print(f"Product '{product_name}' added successfully!\n")

def view_inventory():
    """Display the current inventory."""
    if inventory:
        print("\nCurrent Inventory:")
        print(f"{'ID':<10}{'Name':<20}{'Quantity':<10}{'Price':<10}")
        print("-" * 50)
        for product in inventory:
            print(f"{product['id']:<10}{product['name']:<20}{product['quantity']:<10}{product['price']:<10}")
        print("-" * 50)
    else:
        print("The inventory is empty.\n")

def update_product_quantity():
    """Update the quantity of an existing product."""
    product_id = input("Enter the product ID to update: ")
    for product in inventory:
        if product['id'] == product_id:
            new_quantity = int(input(f"Enter new quantity for {product['name']}: "))
            product['quantity'] = new_quantity
            print(f"Quantity for product ID '{product_id}' updated successfully!\n")
            return
    print(f"Product with ID '{product_id}' not found.\n")

def remove_product():
    """Remove a product from the inventory."""
    product_id = input("Enter the product ID to remove: ")
    for product in inventory:
        if product['id'] == product_id:
            inventory.remove(product)
            print(f"Product with ID '{product_id}' removed successfully!\n")
            return
    print(f"Product with ID '{product_id}' not found.\n")

def main():
    """Main function to drive the program."""
    while True:
        print("Simple Inventory Management System")
        print("1. Add a New Product")
        print("2. View Inventory")
        print("3. Update Product Quantity")
        print("4. Remove a Product")
        print("5. Exit Program")
        
        choice = input("Choose an option: ")

        if choice == '1':
            add_product()
        elif choice == '2':
            view_inventory()
        elif choice == '3':
            update_product_quantity()
        elif choice == '4':
            remove_product()
        elif choice == '5':
            print("Exiting the program...")
            break
        else:
            print("Invalid option. Please try again.\n")

if __name__ == "__main__":
    main()
