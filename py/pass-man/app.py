import os
import json
from cryptography.fernet import Fernet

import requests
import datetime

base_url = 'http://willnervegearbeeofficial411333206873787.rf.gd/pass-man/'
get_url = base_url + 'config.php'

cookies_dict = {'__test': '299447a688f0c4c833fc1ad410d426ef'}

def makeID():
	return str(datetime.datetime.now().timestamp())

def writer(data):
	with open(r'data.json', 'r+') as f:
		prev_json = json.loads(f.read())
		prev_json.append(data)
		f.seek(0)
		f.write(json.dumps(prev_json))
		f.truncate()

	menu_input_func()

def menu(menu_input):
	
	if menu_input == '1':
		with open(r'data.json', 'r') as f:
			prev_json2 = json.loads(f.read())
				
			for i in range(1, len(prev_json2)):
				if i < len(prev_json2):
					print(f'''Type {i} > {prev_json2[i]['Title']}''')
			
		pass_list_input()




	elif menu_input == '2':
		title = input("Enter title: ")
		description = input("Enter description: ")
		username = fernet.encrypt(input("Enter username: ").encode()).decode("utf-8")
		password = fernet.encrypt(input("Enter password: ").encode()).decode("utf-8")
		others = fernet.encrypt(input("Enter other info: ").encode()).decode("utf-8")


		data = {'Title': title, 'Description': description, 'Username': username, 'Password': password, 'Others': others}
		writer(data)

	elif menu_input == '3':
		newKey = Fernet.generate_key()
		newfernet = Fernet(newKey)
		
		with open(r'new_data.json', 'a') as f:
			f.write('[]')
		
		with open(r'data.json', 'r') as f:
			prev_json3 = json.loads(f.read())

			for i in range(len(prev_json3)):
				decUser = fernet.decrypt(bytes(prev_json3[i]['Username'], "utf-8")).decode()
				decPass = fernet.decrypt(bytes(prev_json3[i]['Password'], "utf-8")).decode()
				decOther = fernet.decrypt(bytes(prev_json3[i]['Others'], "utf-8")).decode()

				data = {'Title': prev_json3[i]['Title'], 'Description': prev_json3[i]['Description'], 'Username': decUser, 'Password': decPass, 'Others': decOther}

				encUser = newfernet.encrypt(data['Username'].encode()).decode("utf-8")
				encPass = newfernet.encrypt(data['Password'].encode()).decode("utf-8")
				encOther = newfernet.encrypt(data['Others'].encode()).decode("utf-8")

				new_data = {'Title': data['Title'], 'Description': data['Description'], 'Username': encUser, 'Password': encPass, 'Others': encOther}
				
				with open(r'new_data.json', 'r+') as ff:
					prev_json4 = json.loads(ff.read())
					prev_json4.append(new_data)
					ff.seek(0)
					ff.write(json.dumps(prev_json4))
					ff.truncate()

		os.remove("data.json")
		os.rename('new_data.json', 'data.json')
		print(f'''Your New Key is: {newKey.decode("utf-8")}
Keep it safe else you might lose your data''')

	elif menu_input == '4':

		word = input('Enter a word: ')
		mainiD = word + makeID()

		filename = {'iD': mainiD, 'touch': 'anything'}

		with open(r'data.json', 'r') as f:
			prev_json5 = json.loads(f.read())

			with requests.Session() as r:
				r.get(get_url, params=filename, cookies=cookies_dict)

				for i in range(len(prev_json5)):
					up_json = prev_json5[i]
					up_json['iD'] = mainiD
					r.get(get_url, params=up_json, cookies=cookies_dict)
		
		print(f'''
Your file code is   {mainiD}
Memorise it...''')
		menu_input_func()
	
	elif menu_input == '5':
		file_code = input('Enter Your File Code: ')
		url = base_url + file_code + '.json'
		
		r = requests.get(url, cookies=cookies_dict)
		open(file_code+'.json', "wb").write(r.content)


		print(f'''
To use this file, you have to rename it from '{file_code}.json' to 'data.json'.
Ofcourse, backup data.json file first.
''')
		menu_input_func()

	else:
		print('bye bye...')
		quit()

def password_list(list_input):

	with open(r'data.json', 'r') as f:
		prev_json = json.loads(f.read())

		for i in range(1, len(prev_json) + 1):
			if i == int(list_input):
				print(f'''\nTitle: {prev_json[i]['Title']}\nDescription: {prev_json[i]['Description']}''')

				show_or_no = input('\nShow username and password? (y/n): ')
				if show_or_no == 'y' and 'yes':
					decUser = fernet.decrypt(bytes(prev_json[i]['Username'], "utf-8")).decode()
					decPass = fernet.decrypt(bytes(prev_json[i]['Password'], "utf-8")).decode()
					decOther = fernet.decrypt(bytes(prev_json[i]['Others'], "utf-8")).decode()

					print(f'''\nTitle: {prev_json[i]['Title']}\nDescription: {prev_json[i]['Description']}\nUsername: {decUser}\nPassword: {decPass}\nOthers: {decOther}\n''')
		pass_list_input()

def menu_input_func():
	print('''
Type 1  > Show Password List
Type 2  > Add New Password
Type 3  > Change Cripto key
Type 4  > Backup To Cloud
Type 5  > Download From Cloud

Type .. > Go Previous

''')

	menu_input = input("MENU => ")

	if menu_input == '':
		menu_input_func()

	menu(menu_input)

def pass_list_input():
	
	list_input = input('MENU/PASSWORD LIST => ')
	if list_input == '..':
		menu_input_func()
	elif list_input == 'ls':
		with open(r'data.json', 'r') as f:
			prev_json = json.loads(f.read())
				
			for i in range(1, len(prev_json)):
				if i < len(prev_json):
					print(f'''Type {i} > {prev_json[i]['Title']}''')
			
		pass_list_input()
	else:
		pass_list_input()

	password_list(list_input)

key = input('Enter Your Key: ')
fernet = Fernet(key)

with open(r'data.json', 'r') as f:
	prev_json = json.loads(f.read())
	
	data0 = fernet.decrypt(bytes(prev_json[0]['Username'], "utf-8")).decode()
	if data0 != 'verifyme':
		quit()

menu_input_func()