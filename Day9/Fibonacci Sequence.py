def fibonacci_sequence():
    N = int(input("Enter the number of Fibonacci numbers to generate: "))
    
    if N <= 0:
        print("Please enter a positive integer.")
        return

    fib_sequence = [0, 1]
    for _ in range(2, N):
        next_value = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_value)

    print(f"The first {N} numbers in the Fibonacci sequence are: {fib_sequence[:N]}")

fibonacci_sequence()
