
def get_expense():
    expense =input("Enter the expense: ")
    return expense;
def check_expense(expense):
    while True :
        try:
            expense = float(expense)
            if(expense<=0):
                print("Please enter a positive number")
                expense = get_expense()
                continue
            return expense 
        except ValueError:
             print("Please enter a valid number")
             expense = get_expense()
total_expenses = 0
expenses = []
while True:
    expense = check_expense(get_expense())

    expenses.append(expense)

    total_expenses = total_expenses + expense

    print(f"The total expenses = {total_expenses}")

    check=input("Do you want to continue adding? Y/N")

    if(check =='N'):
        total_sum = sum(expenses)
        average = total_sum / len(expenses)
        Largest_expense = max(expenses)
        Smallest_expense = min(expenses)
        Transaction_count = len(expenses)

        print("\n===== Expense Summary =====")
        print(f"The total expenses of this transaction is: {total_expenses}")
        print(f"Average expense: {average}")
        print(f"Largest expense: {Largest_expense}")
        print(f"Smallest expense: {Smallest_expense}")
        print(f"Number of transactions: {Transaction_count}")

        print("Good bye")
        break





