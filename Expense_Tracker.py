expenses = []

def add_expense():
    description = input("Enter a description for the expense: ")
    amount = float(input("Enter the amount: "))
    expenses.append({"description": description, "amount": amount})
    print("Expense added successfully! ")

def view_expenses():
    if not expenses:
        print("No expenses recorded. ")
    else:
        print("Expenses List:")
        for expense in expenses:
            print(f"{expense['description']}: ${expense['amount']:.2f}")
        print()
def calculate_total():
    total = sum(expense['amount'] for expense in expenses)
    print(f"Total expenses: ${total:.2f} ")
while True:
    print("Expense Tracker Options:")
    print("1. Add an expense")
    print("2. View all expenses")
    print("3. Calculate total expenses")
    print("4. Exit")
    choice = input("Choose an option (1-4): ")
    print()
    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        calculate_total()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again. ")