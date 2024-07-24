def compute_pay(hours, rate):
    if hours > 40:
        overtime = hours - 40
        pay = (40 * rate) + (overtime * rate * 1.5)
    else:
        pay = hours * rate
    return pay

# Testing the function with 45 hours at a rate of 10
print(compute_pay(45, 10))
