from add_contract import addContract
from all_contract import allContract
from search_contract import search_contract
from delete_contract import delete_contract
print('''
======= Contact Book =======
1. Add Contact
2. View All Contacts
3. Search Contact
4. Delete Contact
5. Exit
============================''')

while True:
  choise = int(input("Choice your option: "))

  if choise == 1:
    print("Choice: 1")
    addContract()

  elif choise == 2:
    print("choice: 2")
    allContract()

  elif choise == 3:
    print("choice: 3")
    search_contract()

  elif choise == 4:
    print("choice: 4")
    delete_contract()

  elif choise == 5:
    print("Thank you :) ")
    break
