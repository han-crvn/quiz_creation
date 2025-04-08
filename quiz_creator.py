# Import libraries that will be needed.

while True:
    try:
        print("Selection:")
        print("1. Add Category \n2. Access a category \n3. Exit \n")

        # Allow users to interact with the option.
        choice = int(input("Enter a number of your choice: "))
    
        # If users choose 1 allow them to add category.
        if choice == 1:
            
            # Allow users to add the name of the category
            category = input("Enter the name of category: ")

            # Format the category name to its file name.
            file_name = "_".join(category.lower().split()) + ".txt"

            # Create the txt file of category.
            myFile = open(f"category_{file_name}", "w")

            # In the first line of txt file, add the name of category.
            myFile.write(f"===== {category.upper()} =====")
            myFile.close()

        # If users choose 2 allow them to access file and add questions.
        if choice == 2:
            pass
        
        # if users choose 3 they will be able to leave the program.
        elif choice == 3:
            break

    #Catch Invalid input.
    except ValueError:
        print("\nInvalid Input. Please, try again.\n")
