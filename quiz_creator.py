# Import libraries that will be needed.

while True:
    try:
        print("Selection:")
        print("1. Add Category \n2. Access a category \n3. Exit \n")

        # Allow users to interact with the option.
        choice = int(input("Enter a number of your choice: "))
    
        # If users choose 1 allow them to add category.
        if choice == 1:
            pass
        
        # If users choose 2 allow them to access file and add questions.
        if choice == 2:
            pass
        
        # if users choose 3 they will be able to leave the program.
        elif choice == 3:
            break

    #Catch Invalid input.
    except ValueError:
        print("Invalid Input. Please, try again.")
