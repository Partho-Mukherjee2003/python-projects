def delete_contract():
  target = input("Kake delete korte chan? (Name): ")

  with open("contract.txt", "r") as f:
        all_lines = f.readlines()
  remaining_contracts = []
  found = False

  for line in all_lines:
        if target.lower() in line.lower():
            found = True
            print(f"Deleting: {line.strip()}")
        else:
            remaining_contracts.append(line)
  if found:
        with open("contract.txt", "w") as f:
            f.writelines(remaining_contracts)
        print("Delete Succesfully")
  else:
        print("This name not found")
