def fibonacci(n, depth=0, max_depth=20):
    if depth > max_depth:
        return "Depth limit reached, returning approximate value"
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1, depth + 1, max_depth) + fibonacci(n - 2, depth + 1, max_depth)

def main():
    print("Fibonacci(10):", fibonacci(10))
    print("Fibonacci(30) with depth limit 5:", fibonacci(30, max_depth=5))

main()
