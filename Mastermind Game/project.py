import random

# Generate a random 4-digit number between 1000 and 9999
num = random.randrange(1000, 10000)

# Prompt the player to make their first guess
n = int(input("Guess the 4-digit number:"))

# Check if the player guessed correctly on the first try
if n == num:
    print("Great! You guessed the number in just 1 try! You're a Mastermind!")
else:
    ctr = 1  # Initialize the counter to count the number of attempts
    
    # Loop until the player guesses the number correctly
    while n != num:
        count = 0  # Reset the count of correct digits for each guess
        
        # Convert both the guess and the number to strings for digit comparison
        n_str = str(n)
        num_str = str(num)
        
        # Check each digit to see if it matches the corresponding digit in the generated number
        for i in range(4):
            if n_str[i] == num_str[i]:  # If the digit and position match
                count += 1  # Increment the count of correct digits
        
        # Provide feedback to the player
        if count > 0:
            print(f"Not quite the number. But you did get {count} digit(s) correct!")
        else:
            print("None of the numbers in your input match.")
        
        # Prompt the player to make another guess
        n = int(input("Enter your next choice of numbers: "))
        ctr += 1  # Increment the counter for each guess
    
    # If the player eventually guesses correctly, print the success message
    print("You've become a Mastermind!")
    print(f"It took you only {ctr} tries.")
