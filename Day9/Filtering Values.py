def filter_values(numbers, threshold):
    filtered_numbers = [number for number in numbers if number > threshold]
    print(f"Numbers greater than {threshold}: {filtered_numbers}")

numbers = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]
threshold = int(input("Enter the threshold value: "))
filter_values(numbers, threshold)
