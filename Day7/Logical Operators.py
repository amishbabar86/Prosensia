num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))
if num1 > 0 and num2 > 0:
    print("Both are positive")
elif num1 > 0 or num2 > 0:
    print("One is positive")
else:
    print("None are positive")
