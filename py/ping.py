import subprocess
from time import sleep

fromm = '192.168.0.0'.split('.')
too = '192.168.255.255'.split('.')

a = int(fromm[0])
b = int(fromm[1])
c = int(fromm[2])
d = int(fromm[3])

o = int(too[0])
p = int(too[1])
q = int(too[2])
r = int(too[3])

def ping(host):
	command = ['ping', '-c', '1', host]
	subprocess.call(command)

for h in range(a, o+1):
	for i in range(b, p+1):
		for j in range(c, q+1):
			for k in range(d, r+1):

				host = f'{h}.{i}.{j}.{k}'
				print(ping(host))
				sleep(0.01)

