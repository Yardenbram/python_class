while True:
    user_input = input("Enter a number (or type 'exit' to quit): ")
    if user_input.lower() == 'exit':
        break
    try:
        number = int(user_input)
        if number % 2 == 0:
            print("Even")
        else:
            print("Odd")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
