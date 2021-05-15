arr = []


for i in range(15):
  if i % 2 == 1:
    a = list(range(1, 10))
    arr.append(a)
  else:
    arr.append([i])

# print(arr)

for i in range(len(arr)):
  print(arr[i])
