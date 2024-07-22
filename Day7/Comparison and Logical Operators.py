number = int(input("Enter an integer: "))
if number > 0:
    if number % 2 == 0:
        print("Positive and even")
    else:
        print("Positive but odd")
else:
    print("Negative")
