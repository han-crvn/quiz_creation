# Import libraries that will be needed.
import os

while True:
    try:
        print("Selection:")
        print("1. Add Category \n2. Access a category \n3. Exit \n")

        # Allow users to interact with the option.
        choice = int(input("Enter a number of your choice: "))
    
        # If users choose 1 allow them to add category.
        if choice == 1:
            
            # Allow users to add the name of the category
            category = input("\nEnter the name of category: ")

            # Format the category name to its file name.
            file_name = "_".join(category.lower().split()) + ".txt"

            # Create the txt file of category.
            myFile = open(f"category_{file_name}", "w")

            # In the first line of txt file, add the name of category.
            myFile.write(f"===== {category.upper()} =====")
            myFile.close()

            # Add a short description that the file is successfully added.
            print(f"\n{category} is successfully saved as {file_name}.\n")

        # If users choose 2 allow them to access file and add questions.
        elif choice == 2:
            
            # Access the category files.
            categories = [file for file in os.listdir() if file.startswith("category")]

            # Check if their is present categories or not.
            if not categories:
                print("\nThere are currently no categories present in this program.\n")

            if categories:
                print("\nCurrent Categories: ")

                # List down the categories
                for num, file in enumerate(categories, 1):
                    print(f"{num}.) {file}")

            try:
                
                # Allow users to choose category.
                select_category = int(input("\nEnter the number of chosen category: "))

                # Access the category using index.
                file_name = categories[select_category - 1]

                # Add note that the file is successfully chosen.
                print(f"\n{file_name.title()} is successfully chosen.\n")

            except ValueError:
                print("\nInvalid Input. Please, try again.\n")

        # if users choose 3 they will be able to leave the program.
        elif choice == 3:
            break

    #Catch Invalid input.
    except ValueError:
        print("\nInvalid Input. Please, try again.\n")
