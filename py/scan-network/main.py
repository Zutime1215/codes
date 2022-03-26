import subprocess as sp
from time import sleep

fromm = '172.16.12.0'.split('.')
too = '172.16.12.255'.split('.')

all_ip = []

a = int(fromm[0])
b = int(fromm[1])
c = int(fromm[2])
d = int(fromm[3])

o = int(too[0])
p = int(too[1])
q = int(too[2])
r = int(too[3])

for h in range(a, o+1):
	for i in range(b, p+1):
		for j in range(c, q+1):
			for k in range(d, r+1):

				all_ip.append(f'{h}.{i}.{j}.{k}')
				sleep(0.01)

for ip in all_ip:
	status,result = sp.getstatusoutput("ping -c1 -w1 " + ip)    

	if status == 0:
		with open(f"{all_ip[0]}-{all_ip[-1]}.txt", "a") as ipis:
			ipis.write(ip + '\n')
			print(f"found {ip}")