existing_expenses_list = []
new_expenses_list = []

def addExpense():
    print("Please enter your expense details below.")
    expDate = input("Date of expense (YYYY-MM-DD) format: ")
    expCagtegory = input("Category: ")
    expAmount = input("Amount: ")
    expDescription = input("Description: ")

    expense = {"date": expDate, "category": expCagtegory, "amount": expAmount, "description": expDescription}
    new_expenses_list.append(expense)

def viewExpenses():
    print("showing all the expenses")
    print("\nExisting Expenses:")
    print("Date\t\tCategory\tAmount\t\tDescription")
    print("-" * 60)
    if len(existing_expenses_list) == 0:
        print("###### No existing expenses found")
    else:
        for expense in existing_expenses_list:
            print(f"{expense['date']}\t{expense['category']}\t\t{expense['amount']}\t\t{expense['description']}")

    print("\nNew Expenses:")
    print("Date\t\tCategory\tAmount\t\tDescription")
    print("-" * 60)
    if len(new_expenses_list) == 0:
        print("###### No new expenses added")
    else:
        for expense in new_expenses_list:
            print(f"{expense['date']}\t{expense['category']}\t\t{expense['amount']}\t\t{expense['description']}")

def trackBudget():
    print("Showing your expenses tracking")
    budget = input("Please enter your budget amount: ")
    totalExpense = 0
    for expense in existing_expenses_list:
        totalExpense += expense["amount"] 
    for expense in new_expenses_list:
        totalExpense += expense["amount"] 
    
    if totalExpense > budget:
        print("You have exceeded your budget")
    else:
        print(f"You have {budget - totalExpense} left for the month")

def saveExpenses():
    print("Saving all the expenses")
    with open("expense_tracker.csv", "a") as file:
        for record in new_expenses_list:
            file.write(f"{record['date']},{record['category']},{record['amount']},{record['description']}\n")


def mainMenu():
    while True:
        print("Welcome to Personal Expense Tracker. Please choose one of the below options.")
        print("1. Add expense\n2. View expenses\n3. Track budget\n4. Save expenses\n5. Exit")
        action = int(input("Please enter your option: "))
        if 5 == action:
            saveExpenses()
            print("Closing the personal expense tracker. Have a good day!")
            break
        elif 1 == action:
            addExpense()
        elif 2 == action:
            viewExpenses()
        elif 3 == action:
            trackBudget()
        elif 4 == action:
            saveExpenses()
        else:
            print("Invalid value enterted. Please enter a valid value.")
    

mainMenu()