# divide_two_numbers.py

# Ask the user to input two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Divide the first number by the second number and handle division by zero
if num2 != 0:
    quotient = num1 / num2
    print(f"The result of dividing {num1} by {num2} is: {quotient}")
else:
    print("Error: Division by zero is not allowed.")
