# Import libraries that will be needed.
import os
import time

# Add variables for score and total of quiz.
score = 0
total = 0

# Short Greetings.
print("Hello to Quizzo!")

# Allow users to choose between the options.
while True:
    
    # Print the menu.
    print("\n==== MENU ====")
    print("\n1. Choose quiz category. \n2. Exit.")

    try:
        # Allow users  to choose from the options.
        choice = int(input("\nEnter your choice: "))

        # If users choose option 1, allow users to choose and answer the quiz.
        if choice == 1:
            pass

        # If users choose option 2, allow users to leave the program.
        if choice == 2:
            break
    
    # Catch invalid input.
    except ValueError:
        print("\nInvalid input! try again.")