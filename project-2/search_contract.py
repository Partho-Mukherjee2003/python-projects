def search_contract():
  name = input("Enter the search name: ")
  found = False
  try:
    with open("contract.txt" , "r") as f:
      for line in f:
        if name.lower() in line.lower():
          print("Contract Found :")
          print( line )
          print( line.strip() )
          found = True
      if found == False:
        print("This contract is not in here")
  except Exception as e:
    print(e)
