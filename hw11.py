import json
def get_user_info():
	user = dict()
	user['name'] = input('Enter your name: ')
	user['last_name'] = input('Enter your last name: ')
	user['phone_number'] = input('Enter your phone number: ')
	user['address'] = input('Enter your address: ')
	save_data(user)

def save_data(user):
	with open('user.json', 'w') as user_file:
		json.dump(user, user_file)
		# for data in user:
		# 	user_file.write(user[data])
		# 	user_file.write('\n')


def print_user_info():
	with open('user.json') as user_file:
		user = json.load(user_file)
	for k,v in user.items():
		print(k, ':', v)

get_user_info()

print_user_info()


# with open ('week.txt') as week_file:
# 	weekdays = [day.rstrip() for day in week_file.readlines()]

# print(weekdays)

# username = input('Hey, what\'s your name?: ')

# with open('user_info.txt', 'w') as file_object:
# 	file_object.write(username)

# with open('user_info.txt') as file_object:
# 	username = file_object.read()

# print('Hello, and welcome back,', username)