expenses = []

def add_expense():
    expense = float(input("Enter an expense amount: $"))
    expenses.append(expense)

def display_expenses():
    print("\nExpenses:")
    for expense in expenses:
        print(f"${expense:.2f}")

def show_total():
    total = sum(expenses)
    print(f"\nTotal expenses: ${total:.2f}")

while True:
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. Display Expenses")
    print("3. Show Total")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        display_expenses()
    elif choice == "3":
        show_total()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")