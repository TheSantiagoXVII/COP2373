from functools import reduce
#Request the user the espense and the amount.
def get_expenses():
    expenses = []
    while True:
        expense_type = input("Enter the type of expense (or type 'done' to finish): ")
        if expense_type.lower() == 'done':
            break
        try:
            amount = float(input(f"Enter the amount for {expense_type}: "))
            expenses.append((expense_type, amount))
        except ValueError:
            print("Invalid amount. Please enter a number.") # In case the amount introduced is invalid.
    return expenses
#Start the main function where the expenses are going to be classified.
def main():
    expenses = get_expenses()

    if not expenses:
        print("No expenses entered.")
        return

    # Total expense using reduce
    total = reduce(lambda acc, item: acc + item[1], expenses, 0)

    # Highest expense
    highest = reduce(lambda x, y: x if x[1] > y[1] else y, expenses)

    # Lowest expense
    lowest = reduce(lambda x, y: x if x[1] < y[1] else y, expenses)

    # Display results
    print(f"\nTotal Expenses: ${total:.2f}")
    print(f"Highest Expense: {highest[0]} - ${highest[1]:.2f}")
    print(f"Lowest Expense: {lowest[0]} - ${lowest[1]:.2f}")

# Run the program
main()
