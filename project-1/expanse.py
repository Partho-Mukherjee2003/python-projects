from datetime import datetime
def addExpanse():
  with open('Expense.txt',"a") as f:
    try:
      expense = int(input("Enter your expense: "))
      print(f"Your income is {expense}")
      expenseCategoryList = ["Food", "Rent", "Transport", "Shopping", "Bills", "Health"]
      for i in range(len(expenseCategoryList)):
        print(f"{i+1}. {expenseCategoryList[i]}")
      choice = int(input("Select category number: "))
      expense_category = expenseCategoryList[choice - 1]
      current_date = datetime.now().strftime("%Y-%m-%d")
      f.write(f"{current_date},{expense},{expense_category}\n")
      print(f"Expense {expense} saved successfully!")

    except ValueError:
      print("Error, please enter a numeric value")

