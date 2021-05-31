weight = float(input("Please enter your weight: "))
unit = input("(L)bs or (K)gs: ")
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"You are {converted} kilos")
else:
    converted = weight / 0.45
    print(f"You are {converted} pounds")
    