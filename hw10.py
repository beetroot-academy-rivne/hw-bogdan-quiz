# Write a Python function to check whether a string is a pangram or not. Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
# For example : "The quick brown fox jumps over the lazy dog"
def check_pangram(sentence):
	alphabet = ['a','b','c','d','e','f','g','h','o','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	for letter in sentence:

		if letter in alphabet:
			alphabet.remove(letter)	
	print(alphabet)
	if not alphabet:
		print('This sentence is pangram')
	else:
		print('This sentence is not pangram')
check_pangram('The quick brown fox jumps over the lazy dog')

# Write a Python program to print the even numbers from a given list.
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Result : [2, 4, 6, 8]
def get_even(l1):
	even = list()
	for num in l1:
		if not num == '' and not num == ' ':
			if not int(num) % 2:
				even.append(num)
	print('Expected Result:', even)
l1 = list(input('Sample List: '))
print(l1)
get_even(l1)


# Write a Python function that takes a list and returns a new list with unique elements of the first list.
# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]
def del_duplicates(l1):
	result = list()
	for i in l1:
		if not i in result and not i == '' and not i == ' ' :
			result.append(i)
	print('Unique List:',result)
l1 = list(input('Sample list: '))
del_duplicates(l1)

# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters. Go to the editor
def calculate_cases(sentence):
	lower = 0
	upper = 0
	for i in sentence:	
		if i.islower():
			lower += 1
		elif i.isupper():
			upper += 1
	print('No. of Upper case characters :',upper)
	print('No. of Lower case characters :', lower)
sentence = input('Sample string: ')
calculate_cases(sentence)

# 1. A simple function
def favorite_movie(movie_name):
	print('My favourite movie is', movie_name)
favorite_movie('Rembo')

# 2. Creating a dictionary.
def make_country(name, capital):
	country = dict()
	country['name'] = name
	country['capital'] = capital
	print(country)
make_country('Ukraine', 'Kyiv')

# 3. A simple calculator
def make_operation(operation, *nums):
	result = nums[0]
	print(nums[0])
	if operation == '+':
		for i, num in enumerate(nums):
			if i > 0:
				result += num
				print(result, num)
	elif operation == '-':
		for i, num in enumerate(nums):
			if i > 0:
				result -= num
	elif operation == '*':
		for i, num in enumerate(nums):
			if i > 0:
				result *= num
	elif operation == '/':
		
		for i,num in enumerate(nums):
			if i > 0:
				result /= num

	return result
print(make_operation('/', 12,6,3))

