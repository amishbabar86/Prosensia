# Function to add a new expense
def add_expense(expenses):
    while True:
        try:
            amount = float(input("Enter the expense amount: "))
            if amount <= 0:
                print("Amount must be positive. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid amount. Please enter a number.")
    
    category = input("Enter the expense category (e.g., food, transportation, entertainment): ").strip().lower()
    description = input("Enter a brief description of the expense: ").strip()
    
    expense = {
        'amount': amount,
        'category': category,
        'description': description
    }
    expenses.append(expense)
    print("Expense added successfully!\n")

# Function to display a summary of expenses
def display_summary(expenses):
    summary = {}
    for expense in expenses:
        category = expense['category']
        amount = expense['amount']
        if category in summary:
            summary[category] += amount
        else:
            summary[category] = amount

    if summary:
        print("\nExpense Summary:")
        for category, total in summary.items():
            print(f"{category.capitalize()}: ${total:.2f}")
    else:
        print("No expenses recorded yet.\n")

# Main function to manage the program flow
def main():
    expenses = []
    
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add an expense")
        print("2. View expense summary")
        print("3. Exit")
        choice = input("Choose an option (1/2/3): ").strip()

        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            display_summary(expenses)
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

# Run the main function
if __name__ == "__main__":
    main()
