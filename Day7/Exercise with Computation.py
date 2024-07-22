hours_worked = float(input("Enter hours worked: "))
hourly_rate = float(input("Enter hourly rate: "))
if hours_worked > 40:
    extra_hours = hours_worked - 40
    gross_pay = (40 * hourly_rate) + (extra_hours * 1.5 * hourly_rate)
else:
    gross_pay = hours_worked * hourly_rate
print("Gross pay: $", gross_pay)
