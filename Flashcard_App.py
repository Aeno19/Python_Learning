flashcards = {}

def add_flashcard():
    question = input("Enter the question: ")
    answer = input("Enter the answer: ")
    flashcards[question] = answer
    print("Flashcard added successfully! ")

def view_flashcards():
    if not flashcards:
        print("No flashcards available. ")
    else:
        print("Your flashcards:")
        for question, answer in flashcards.items():
            print(f"Q: {question} | A: {answer}")
        print()

while True:
    print("Flashcard App Options:")
    print("1. Add a flashcard")
    print("2. View all flashcards")
    print("3. Exit")

    choice = input("Choose an option (1-3): ")
    print()

    if choice == "1":
        add_flashcard()
    elif choice == "2":
        view_flashcards()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Error. ")