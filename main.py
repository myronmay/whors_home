import subprocess, json
from colorama import Fore

with open('users.json', 'r') as file:
	data = json.load(file)

dict = []

for a in range(0, len(data['users'])):
	ip = list(data['users'][a].keys())
	low_ip = int(ip[0].replace('192.168.1.', ""))
	res = subprocess.getoutput("ping -c1 192.168.1.%d | grep 'ttl'" % low_ip)
	if res != "":
		print(Fore.GREEN + "Online (%s) => %d <=" % (data['users'][a][ip[0]], low_ip))
	else:
		print(Fore.RED + "OFFLINE (%s) => %d <=" % (data['users'][a][ip[0]], low_ip))