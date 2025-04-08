# Import libraries that will be needed.
import os

while True:
    try:
        print("\nSelection:")
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

                while True:

                    # Allow users to create question.
                    question = input("Enter the question: ")

                    # Add the question in file.
                    access_file = open(file_name, "a")
                    access_file.write(f"\nQuestion: {question}\n")
                    access_file.close()

                    # Allow users to add choices.
                    for i in range(4):
                        choice = input(f"Choice {chr(65 + i )}:")

                        # Add the choices in file.
                        access_file = open(file_name, "a")
                        access_file.write(f"{chr(65 + i)}.) {choice}\n")
                        access_file.close()

                    # Allow users to input the correct answer
                    answer = input("Enter the correct letter(answer): ")

                    # Add the answer in file.
                    if answer == "A" or answer == "B" or answer == "C" or answer == "D":
                        access_file = open(file_name, "a")
                        access_file.write(f"Answer: {answer}\n\n")
                        access_file.close()

                    # Catch the invalid answer.
                    else:
                        print("Input a valid letter\n")

                    # Inform the users that the message is successfully added.
                    print("The question set is successfully added.\n")

                    # Ask users if they want to add more.
                    try:
                        ask_user = int(input("Do you want to input another set of question (1 = Yes, 2 = No): "))

                        # Validate their decision
                        if ask_user == 1:
                            continue
                        elif ask_user == 2:
                            break

                    except ValueError:
                        print("\n Invalid input. Please try, again.\n")

            except ValueError:
                print("\nInvalid Input. Please, try again.\n")

        # if users choose 3 they will be able to leave the program.
        elif choice == 3:
            print("Goodbye!")
            break

    #Catch Invalid input.
    except ValueError:
        print("\nInvalid Input. Please, try again.\n")
