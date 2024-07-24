def sum_of_squares():
    N = int(input("Enter the value of N: "))
    total = sum(i**2 for i in range(1, N+1))
    print(f"The sum of the squares of the first {N} natural numbers is: {total}")

sum_of_squares()
