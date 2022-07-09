import json
from cryptography.fernet import Fernet

def test_json(data):
	with open(r'data.json', 'r+') as f:
		prev_json = json.loads(f.read())
		data['id'] = len(prev_json) + 1
		prev_json.append(data)
		f.seek(0)
		f.write(json.dumps(prev_json))
		f.truncate()

		menu_input_func()

def menu(menu_input):
	
	if menu_input == '1':
		with open(r'data.json', 'r') as f:
			prev_json = json.loads(f.read())
				
			for i in range(len(prev_json)):
				if i < len(prev_json):
					print(f'''{prev_json[i]['id']}. {prev_json[i]['Title']}''')
			
			pass_list_input()




	elif menu_input == '2':
		title = input("Enter title: ")
		description = input("Enter description: ")
		username = input("Enter username: ")
		password = input("Enter password: ")

		data = {'Title': title, 'Description': description, 'Username': username, 'Password': password}
		test_json(data)

	else:
		print('bye bye...')
		quit()

def password_list(list_input):

	with open(r'data.json', 'r') as f:
		prev_json = json.loads(f.read())

		for i in range(len(prev_json) + 1):
			if i == int(list_input):
				print(f'''\nTitle: {prev_json[i - 1]['Title']}\nDescription: {prev_json[i - 1]['Description']}''')

				show_or_no = input('\nShow username and password? (y/n): ')
				if show_or_no == 'y' and 'yes':
					print(f'''\nTitle: {prev_json[i - 1]['Title']}\nDescription: {prev_json[i - 1]['Description']}\nUsername: {prev_json[i - 1]['Username']}\nPassword: {prev_json[i - 1]['Password']}\n''')
		pass_list_input()

def menu_input_func():
	print('''
1. password lists
2. input new password
3. exit
	''')

	menu_input = input("MENU => ")

	if menu_input == '':
		menu_input_func()

	menu(menu_input)

def pass_list_input():
	
	list_input = input('MENU/PASSWORD LIST => ')
	if list_input == '..':
		menu_input_func()
	elif list_input == '':
		pass_list_input()
	elif list_input == 'ls':
		with open(r'data.json', 'r') as f:
			prev_json = json.loads(f.read())
				
			for i in range(len(prev_json)):
				if i < len(prev_json):
					print(f'''{prev_json[i]['id']}. {prev_json[i]['Title']}''')
			
			pass_list_input()

	password_list(list_input)


menu_input_func()