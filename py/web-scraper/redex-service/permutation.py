from itertools import permutations

result = list(permutations('abcdefghijklmnopqrstuvwxyz0123456789', 2))

for i in result:
	ii = i[0] + i[1] + '\n'
	with open("apis.txt", "a") as apis:
		apis.write(ii)