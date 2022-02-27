import json 

data = {}
data['users'] = []

data['users'].append({
	'192.168.1.1': 'Gateway'
	})

	
with open('users.json', 'w') as file:
	json.dump(data, file)
