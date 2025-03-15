# Ask for a valid number input
while True:
    user_input = input("Please enter a positive number: ")
    
    try:
        number = float(user_input)
        if number > 0:
            print(f"Thank you! You entered {number}.")
            break  # Exit the loop if a valid number is entered
        else:
            print("The number must be positive. Try again.")
    except ValueError:
        print("That's not a valid number. Please try again.")
