class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    
    def __str__(self):
        return f"{self.real} + {self.imag}i"

    @staticmethod
    def add(c1, c2):
        return ComplexNumber(c1.real + c2.real, c1.imag + c2.imag)

    @staticmethod
    def subtract(c1, c2):
        return ComplexNumber(c1.real - c2.real, c1.imag - c2.imag)

    @staticmethod
    def multiply(c1, c2):
        real = c1.real * c2.real - c1.imag * c2.imag
        imag = c1.real * c2.imag + c1.imag * c2.real
        return ComplexNumber(real, imag)

    @staticmethod
    def divide(c1, c2):
        if c2.real == 0 and c2.imag == 0:
            raise ValueError("Cannot divide by zero")
        denom = c2.real ** 2 + c2.imag ** 2
        real = (c1.real * c2.real + c1.imag * c2.imag) / denom
        imag = (c1.imag * c2.real - c1.real * c2.imag) / denom
        return ComplexNumber(real, imag)

def main():
    c1 = ComplexNumber(1, 2)  # 1 + 2i
    c2 = ComplexNumber(3, 4)  # 3 + 4i
    
    try:
        print("Addition:", ComplexNumber.add(c1, c2))
        print("Subtraction:", ComplexNumber.subtract(c1, c2))
        print("Multiplication:", ComplexNumber.multiply(c1, c2))
        print("Division:", ComplexNumber.divide(c1, c2))
    except ValueError as e:
        print(e)

main()
