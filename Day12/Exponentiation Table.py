def exponentiation_table(base, exponent_range):
    return [f"{base}^{i} = {base ** i}" for i in range(1, exponent_range + 1)]


print(exponentiation_table(2, 5))  
