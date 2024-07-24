def find_largest_smallest():
    numbers = [int(x) for x in input("Enter a list of integers separated by spaces: ").split()]
    
    if not numbers:
        print("No numbers entered.")
        return

    largest = numbers[0]
    smallest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number

    for number in numbers:
        if number < smallest:
            smallest = number

    print(f"Largest number: {largest}")
    print(f"Smallest number: {smallest}")

find_largest_smallest()
