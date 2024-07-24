def break_and_continue():
    while True:
        user_input = input("Enter a line of text (or 'done' to finish): ")
        if user_input.lower() == 'done':
            break
        if user_input.startswith('#'):
            continue
        print(user_input)

break_and_continue()
