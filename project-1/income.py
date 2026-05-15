from datetime import datetime
def addIncome():
  with open('income.txt',"a") as f:
    try:
      income = int(input("Enter your income: "))
      print(f"Your income is {income}")
      incomeCategoryList = ["Freelancing", "Salary", "Home", "Tuition", "Others"]
      for i in range(len(incomeCategoryList)):
        print(f"{i+1}. {incomeCategoryList[i]}")
      choice = int(input("Select category number: "))
      income_category = incomeCategoryList[choice - 1]
      current_date = datetime.now().strftime("%Y-%m-%d")
      f.write(f"{current_date},{income},{income_category}\n")
      print(f"Income {income} saved successfully!")

    except ValueError:
      print("Error, please enter a numeric value")







