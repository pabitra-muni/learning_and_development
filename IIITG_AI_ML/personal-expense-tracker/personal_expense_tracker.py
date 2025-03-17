existing_expenses_list = []
new_expenses_list = []

def addExpense():
    print("#################################")
    print("Please enter your expense details below.")
    print("#################################")
    expDate = input("Date of expense (YYYY-MM-DD) format: ")
    expCagtegory = input("Category: ")
    expAmount = float(input("Amount: "))
    expDescription = input("Description: ")

    expense = {"date": expDate, "category": expCagtegory, "amount": expAmount, "description": expDescription}
    new_expenses_list.append(expense)
    print(">>>>> Your expense details added successfully")

def viewExpenses():
    print("#################################")
    print("showing all the expenses")
    print("#################################")
    print("\nExisting Expenses:")
    print("Date\t\tCategory\t\tAmount\t\tDescription")
    print("-" * 60)
    if len(existing_expenses_list) == 0:
        print("No existing expenses found")
    else:
        for expense in existing_expenses_list:
            print(f"{expense['date']}\t{expense['category']}\t\t\t{expense['amount']}\t\t{expense['description']}")

    print("\nNew Expenses:")
    print("Date\t\tCategory\t\tAmount\t\tDescription")
    print("-" * 60)
    if len(new_expenses_list) == 0:
        print("No new expenses added")
    else:
        for expense in new_expenses_list:
            print(f"{expense['date']}\t{expense['category']}\t\t\t{expense['amount']}\t\t{expense['description']}")

    print("#################################")
def trackBudget():
    print("#################################")
    print("Showing your expenses tracking")
    print("#################################")
    budget = float(input("Please enter your budget amount: "))
    totalExpense = 0
    for expense in existing_expenses_list:
        totalExpense += expense["amount"] 
    for expense in new_expenses_list:
        totalExpense += expense["amount"] 
    
    if totalExpense > budget:
        print(">>>> You have exceeded your budget")
    else:
        print(f">>>>> You have {budget - totalExpense} left for the month")
    print("#################################")

def saveExpenses():
    print("#################################")
    print("Saving all the expenses")
    print("#################################")
    with open("expense_tracker.csv", "a") as file:
        for record in new_expenses_list:
            file.write(f"{record['date']},{record['category']},{record['amount']},{record['description']}\n")
    print("Your new expeses saved successfully")
    print("#################################")
    reset()

def reset():
    existing_expenses_list.clear()
    new_expenses_list.clear()
    loadExistingExpenses()

def loadExistingExpenses():
    try:
        with open("expense_tracker.csv", "r") as file:
            for line in file:
                if line.strip():  # Skip empty lines
                    date, category, amount, description = line.strip().split(",")
                    expense = {
                        "date": date,
                        "category": category, 
                        "amount": float(amount),
                        "description": description
                    }
                    existing_expenses_list.append(expense)
    except FileNotFoundError:
        # Create the file if it doesn't exist
        open("expense_tracker.csv", "w").close()

def mainMenu():
    loadExistingExpenses()
    while True:
        print("#################################")
        print("Welcome to Personal Expense Tracker. Please choose one of the below options.")
        print("#################################")
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