l = []

messege = input("Enter Your Messege: ")
for i in range(1,len(messege)+1):
	j = i*-1
	k = messege[j]
	l.append(k)


m = "".join(l)

print(m)