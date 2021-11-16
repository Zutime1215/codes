from time import sleep
import random

x = 1
y = 1000
z = 0
print(f"Guess a number from 1 to {y}.\n")
sleep(5)

while True:
	a = random.randint(x, y)
	print(f"(1)Is {a} the number? If {a} is your guessed number, type 99.")
	print(f"""(2)If {a} is Greater-than your guessed number, type 1,
(3)If {a} Less-than your guessed number, type 2\n""")

	b = int(input("your answer--> "))
	z = z+1
	if b == 1:
		y = a-1
	elif b == 2:
		x = a+1
	elif b == 99:
		print(f"It took {z} loops. The End")

		break
