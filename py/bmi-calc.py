print("To know your BMI")
a = float(input("Enter Your Weight(KG): "))
b = float(input("Enter Your Height(foot part): "))
c = float(input("Enter Your Height(inch part): "))

d = (((b*12)+c)*2.54)/100

e = a/d**2


print(f"Your BMI is {e}")