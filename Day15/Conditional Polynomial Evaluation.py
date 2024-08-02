def evaluate_polynomial(coeffs, x):
    if not coeffs:
        return 0
    degree = len(coeffs) - 1
    result = 0
    
    if degree == 0:
        result = coeffs[0]
    elif degree == 1:
        result = coeffs[0] * x + coeffs[1]
    elif degree == 2:
        result = coeffs[0] * x**2 + coeffs[1] * x + coeffs[2]
    else:
        for i, coeff in enumerate(coeffs):
            result += coeff * x**(degree - i)
    
    return result

def main():
    print("Linear polynomial (2x + 3):", evaluate_polynomial([2, 3], 5))
    print("Quadratic polynomial (x^2 + 2x + 1):", evaluate_polynomial([1, 2, 1], 3))
    print("Cubic polynomial (x^3 - 2x^2 + x - 1):", evaluate_polynomial([1, -2, 1, -1], 2))

main()
