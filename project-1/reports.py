def allReports():
  total_income = 0
  income_count = 0

  with open("income.txt","r") as f:
    for line in f:
      if line.strip():
        parts =  line.strip().split(",")
        intParts = int(parts[1])
        total_income += intParts
        income_count += 1


  print (f"Total income = {total_income}")
  print (f"Income count = {income_count}")


  total_expence = 0
  expence_count = 0
  expence_report = {}
  with open("Expense.txt","r") as f:
    for line in f:
      if line.strip():
        parts = line.strip().split(",")
        intParts = int(parts[1])
        total_expence += intParts
        expence_count += 1
        category = parts[2]
        amount = intParts
        if category in expence_report:
          expence_report[category] += amount
        else:
          expence_report[category] = amount

  for category , amount in expence_report.items():
          print(f" {category}: {amount} TK")

  print (f"Total expence = {total_expence}")
  print (f"Expence counnt = {expence_count}")

  print(f"Current balance = {total_income - total_expence}")






