# Import libraries that will be needed.
import os
import time

# Add variables for score and total of quiz.
score = 0
total = 0
local_time = time.ctime()

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
            
            # Access the txt file of categories.
            categories = [file for file in os.listdir() if file.startswith("category")]

            # Check if there is a txt file created.
            if not categories:
                print("\nThere are currently no categories present in this program.\n")
                break

            if categories:
                print("\nCurrent Categories: ")

                # List down the categories.
                for num, file in enumerate(categories, 1):
                    print(f"{num}.) {file}")

                try:
                    # Allow users to input their choice.
                    select_category = int(input("\nEnter the number of the chosen category (enter 0 to exit): "))

                    # Allow users to go back in menu.
                    if select_category == 0:
                        break
                    
                    if 1 <= select_category <= len(categories):
                        
                        # Access the file chosen.
                        file_name = categories[select_category - 1]

                        # Add note that the file successfully access.
                        print(f"\n{file_name} is successfully chosen.\n")

                        # Allow users to input their name.
                        name = input("Enter your name: ")

                        # Access the question set of the categories.
                        read_category = open(file_name, "r")
                        access_data = read_category.read().strip().split("\n\n")
                        read_category.close()
                        
                        # Strip the file category.
                        for data in access_data:
                            lines = data.strip().split("\n")

                            if not lines:
                                continue
                            
                            # Check if there is a questions.
                            question_lines = [line for line in lines if line.startswith("Question:")]
                            if not question_lines:
                                continue
                            
                            # Strip down the questions, choices, and answers.
                            question = question_lines[0][9:].strip()
                            choices = [line for line in lines if line.startswith(("A.", "B.", "C.", "D."))]
                            answer_lines = [line for line in lines if line.startswith("Answer:")]

                            if not answer_lines:
                                continue
                            
                            # Strip answers.
                            answer = answer_lines[0][-1].strip().upper()

                            # Print the question.
                            print("\n" + question)

                            # Print the choices
                            for choice_text in choices:
                                print(choice_text)
                            
                            # Allow users to input their answers.
                            guess = input("Your answer (A/B/C/D): ").strip().upper()

                            # Check if their answers is correct or not, if right  +1 to the score.
                            if guess == answer:
                                    print("Correct!\n")
                                    score += 1
                            else:
                                print(f"Wrong! The correct answer is {answer}.\n")

                            # Add the total items of questions.
                            total += 1

                            # Average of their score.
                            average = (score / total) * 100

                            # Print the users score.
                            print(f"Score: {score}/{total}")
                            print(f"Average: {average:.0f} %\n")

                            # Record the data in data_information.txt.
                            add_data = open("data_information.txt", "a")
                            add_data.write(f"Name: {name.title()}\n")
                            add_data.write(f"Category: {file_name.replace('category_', '').replace('.txt', '').title()}\n")
                            add_data.write(f"Time: {local_time}\n")
                            add_data.write(f"Score: {score}\n")
                            add_data.write(f"Average: {average} %\n\n")
                            add_data.close()
                            
                            # Exit option 1.
                            break

                    # Catch invalid option.
                    else:
                        print("\nInvalid number! Try again.")
                        continue

                # Catch invalid input.
                except ValueError:
                    print("\nInvalid input! Try again.")

        # If users choose option 2, allow users to leave the program.
        if choice == 2:
            break
    
    # Catch invalid input.
    except ValueError:
        print("\nInvalid input! try again.")