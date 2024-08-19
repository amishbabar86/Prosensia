# Function to add a new product to the inventory
def add_product(inventory):
    name = input("Enter the product name: ").strip()
    price = float(input("Enter the product price: "))
    quantity = int(input("Enter the product quantity: "))

    # Check if the product is already in the inventory
    for product in inventory:
        if product['name'].lower() == name.lower():
            print(f"Product '{name}' is already in the inventory. Use update function instead.")
            return

    # Add the new product to the inventory
    product = {'name': name, 'price': price, 'quantity': quantity}
    inventory.append(product)
    print(f"Product '{name}' added to inventory.")

# Function to update the quantity of an existing product
def update_quantity(inventory):
    name = input("Enter the product name to update: ").strip()
    
    # Search for the product in the inventory
    for product in inventory:
        if product['name'].lower() == name.lower():
            quantity = int(input("Enter the new quantity: "))
            product['quantity'] = quantity
            print(f"Product '{name}' quantity updated to {quantity}.")
            return
    
    print(f"Product '{name}' not found in the inventory.")

# Function to display all products in the inventory
def display_inventory(inventory):
    if not inventory:
        print("The inventory is empty.")
    else:
        print("\nInventory:")
        for product in inventory:
            print(f"Name: {product['name']}, Price: ${product['price']:.2f}, Quantity: {product['quantity']}")

# Main function to manage the inventory system
def main():
    inventory = []
    
    while True:
        print("\nInventory Management System")
        print("1. Add Product")
        print("2. Update Product Quantity")
        print("3. Display Inventory")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == '1':
            add_product(inventory)
        elif choice == '2':
            update_quantity(inventory)
        elif choice == '3':
            display_inventory(inventory)
        elif choice == '4':
            print("Exiting Inventory Management System.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
