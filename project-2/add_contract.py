def addContract ():
  contract = {}
  name = input("Enter your contract name: ")
  number = input("Enter your contract number: ")
  contract[ name ] = number
  confirm = input("Are you sure to add this contract( y / n ):")
  if confirm.lower() == "y":
    try:
      with open("contract.txt" , "a") as f:
        f.write( str(contract) + "\n" )
    except Exception as e :
      print(e)

