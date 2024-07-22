# gross_pay.py

# Ask the user for the number of hours worked
hours_worked = float(input("Enter the number of hours worked: "))

# Ask the user for the hourly wage rate
hourly_rate = float(input("Enter the hourly wage rate: "))

# Calculate the total pay
gross_pay = hours_worked * hourly_rate

# Display the total pay
print(f"The total pay is: {gross_pay:.2f}")
