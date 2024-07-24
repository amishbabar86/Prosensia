def remove_duplicates(numbers):
    unique_numbers = list(set(numbers))
    print(f"List after removing duplicates: {unique_numbers}")

numbers = [int(x) for x in input("Enter a list of integers separated by spaces: ").split()]
remove_duplicates(numbers)
