def sum_and_average():
    total = 0
    count = 0
    while True:
        user_input = input("Enter a number (or 'done' to finish): ")
        if user_input.lower() == 'done':
            break
        try:
            number = float(user_input)
            total += number
            count += 1
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    if count == 0:
        print("No numbers entered.")
    else:
        average = total / count
        print(f"Sum: {total}, Average: {average}")

sum_and_average()
