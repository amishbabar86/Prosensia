def memoized_fibonacci(n, cache=None):
    if cache is None:
        cache = {0: 0, 1: 1}
    if n in cache:
        return cache[n]
    if len(cache) > 1000:  # Iterative fallback for large cache
        return iterative_fibonacci(n)
    cache[n] = memoized_fibonacci(n - 1, cache) + memoized_fibonacci(n - 2, cache)
    return cache[n]

def iterative_fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def main():
    print("Memoized Fibonacci(10):", memoized_fibonacci(10))
    print("Memoized Fibonacci(100):", memoized_fibonacci(100))

main()
