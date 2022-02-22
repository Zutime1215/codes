from datetime import datetime, timedelta

date_format = '%d:%m:%Y'
# date_format = '%m%d%Y'

i = 1
j = 0
while True:
	future = datetime.today() + timedelta(i)
	future = future.strftime(date_format)

	if j == 25:
		break

	if int(future[0]) == int(future[9]) and int(future[1]) == int(future[8]) and int(future[3]) == int(future[7]) and int(future[4]) == int(future[6]):
		print(future)
		i = i+1
		j = j+1	

	else:
		i = i+1
		continue
