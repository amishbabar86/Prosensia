import cmath

def complex_operations(complex_str, other_complex):
    try:
        complex_num = complex(complex_str)
        other_complex_num = complex(other_complex)

        addition = complex_num + other_complex_num
        subtraction = complex_num - other_complex_num
        multiplication = complex_num * other_complex_num
        division = complex_num / other_complex_num

        return addition, subtraction, multiplication, division
    except ValueError as e:
        return f"Error: {e}"


result = complex_operations("2+3j", "1+2j")
print(result) 
