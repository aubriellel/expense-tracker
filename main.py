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


def remove_expense():
    if not expenses:
        print("\nNo expenses have been entered.")
        return

    print("\nExpenses:")
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. ${expense:.2f}")

    try:
        choice = int(input("Enter the number of the expense to remove: "))

        if 1 <= choice <= len(expenses):
            removed_expense = expenses.pop(choice - 1)
            print(f"${removed_expense:.2f} was removed.")
        else:
            print("Invalid expense number.")

    except ValueError:
        print("Invalid input. Please enter a number.")


# Repeat the menu until the user selects Exit.
while True:
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. Display Expenses")
    print("3. Show Total")
    print("4. Show Statistics")
    print("5. Remove Expense")
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
        remove_expense()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please choose 1 through 6.")