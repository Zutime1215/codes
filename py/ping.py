import subprocess

def ping(host):
	command = ['ping', '-c', '5', host]
	subprocess.call(command)

host = 'replit.com'

print(ping(host))