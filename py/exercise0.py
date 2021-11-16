out = []
interro = ("how", "why", "what", "when")

while True:
	a = input("Say Something: ")
	b = a.capitalize()

	if a.startswith(interro):
		c = b + '? '
	else:
		c = b + '. '


	if a == "/end":
		break
	else:
		out.append(c)
		continue


d = "".join(out)
print(d)
