def guess_number():
    predefined_number = 42
    attempts = 0
    max_attempts = 10
    
    while attempts < max_attempts:
        guess = int(input("Guess the number: "))
        if guess == predefined_number:
            print("Congratulations! You guessed the correct number.")
            break
        attempts += 1
    else:
        print("Sorry, you've reached the maximum number of attempts.")

guess_number()
