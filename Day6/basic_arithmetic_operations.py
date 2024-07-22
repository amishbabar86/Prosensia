# basic_arithmetic_operations.py

# Ask the user to input two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Calculate the sum, difference, product, and quotient
sum_result = num1 + num2
difference = num1 - num2
product = num1 * num2

# Handle division by zero
if num2 != 0:
    quotient = num1 / num2
else:
    quotient = "undefined (division by zero)"

# Display the results
print(f"The sum of {num1} and {num2} is: {sum_result}")
print(f"The difference between {num1} and {num2} is: {difference}")
print(f"The product of {num1} and {num2} is: {product}")
print(f"The quotient of {num1} divided by {num2} is: {quotient}")
