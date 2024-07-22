try:
    number = int(input("Enter an integer: "))
    print("You entered:", number)
except ValueError:
    print("Invalid input, please enter a numeric value.")
