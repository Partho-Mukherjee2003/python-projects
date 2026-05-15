from income import addIncome
from expanse import addExpanse
from reports import allReports

print("-------Finance Tracker Menu________")
print('''
      1. Add Income
      2. Add Expense
      3. View reports
      4. Exit
      ''')
while True:
  choice = int(input("Select an option (1-4):"))

  if choice == 1:
    print('Choice 1:')
    addIncome()

  elif choice == 2:
    print("Choice 2:")
    addExpanse()

  elif choice == 3:
    print("Choice 3:")
    print("____Summary____")
    allReports( )

  elif choice == 4:
    print("Choice 4:")
    print("Thank you")
    break

  else:
    print("Please enter the right choice---")


