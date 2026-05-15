def allContract():
  confirm = input("Are you really want to see all contract (y / n): ")
  if confirm.lower() == "y":
    try:
      with open('contract.txt') as f:
        content = f.read()
        if content:
          print("_____All contract_____")
          print(content)
        else:
          print(" Empty ")
    except Exception as e:
      print(e)
