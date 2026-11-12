# Store all expense amounts entered by the user.
expenses = []

def add_expense():
    # AI-assisted improvement: input validation prevents the program
    # from crashing when the user enters something other than a number.
    while True:
        try:
            expense = float(input("Enter an expense amount: $"))

            if expense < 0:
                print("Please enter a positive amount.")
            else:
                expenses.append(expense)
                print(f"${expense:.2f} was added.")
                break

        except ValueError:
            print("Invalid input. Please enter a number.")

def display_expenses():
    # Tell the user when there are no expenses instead of showing an empty list.
    if not expenses:
        print("\nNo expenses have been entered.")
        return

    print("\nExpenses:")
    for expense in expenses:
        print(f"${expense:.2f}")

def show_total():
    total = sum(expenses)
    print(f"\nTotal expenses: ${total:.2f}")

def show_statistics():
    # AI-assisted feature: calculate additional information from the expense list.
    if not expenses:
        print("\nNo expenses have been entered.")
        return

    average = sum(expenses) / len(expenses)
    highest = max(expenses)

    print("\nExpense Statistics")
    print(f"Average expense: ${average:.2f}")
    print(f"Highest expense: ${highest:.2f}")

def search_expenses_by_range():
    # Validate both amounts and ensure the range is in ascending order.
    while True:
        try:
            minimum = float(input("Enter the minimum amount: $"))
            maximum = float(input("Enter the maximum amount: $"))

            if minimum < 0 or maximum < 0:
                print("Please enter amounts that are zero or greater.")
                continue

            if minimum > maximum:
                print("The minimum amount cannot be greater than the maximum.")
                continue

            break
        except ValueError:
            print("Invalid input. Please enter valid numbers.")

    matching_expenses = [
        expense for expense in expenses
        if minimum <= expense <= maximum
    ]

    if not matching_expenses:
        print("\nNo expenses were found in that range.")
        return

    print(f"\nExpenses from ${minimum:.2f} to ${maximum:.2f}:")
    for expense in matching_expenses:
        print(f"${expense:.2f}")

# Repeat the menu until the user selects Exit.
while True:
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. Display Expenses")
    print("3. Show Total")
    print("4. Show Statistics")
    print("5. Search Expenses by Range")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        display_expenses()
    elif choice == "3":
        show_total()
    elif choice == "4":
        show_statistics()
    elif choice == "5":
        search_expenses_by_range()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please choose 1 through 6.")