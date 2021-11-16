while True:
	a = int(input("""
	select a type:-
	(type 1) Convert KG to POUND.
	(type 2) Convert POUND to KG.
	(type 99) To Exit.

"""))

	if a == 1:
		b = float(input("Enter Your KG Value:- "))
		c = round(b * 2.20462, 4)
		print(f"{b} KG is equels to {c} POUND")
	elif a == 2:
		b = float(input("Enter Your Pound Value:- "))
		c = round(b * 0.453592, 4)
		print(f"{b} POUND is equels to {c} KG")

	elif a == 99:
		break  
	else:
		print("Please, Try Again!")	
