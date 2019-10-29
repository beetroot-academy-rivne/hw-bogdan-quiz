# Write a Python function to display products with price less or equal form user input

products = {
'SMART WATCH': 550,
'PHONE' : 1000,
'PLAYSTATION': 500,
'LAPTOP' : 1550,
'MUSIC PLAYER' : 600,
'TABLET' : 400
}

def user_filter(products:dict, price:int, mode:int): #1 equal, 2 less, 3 over
	new = dict()
	for prod in products:
		if mode == 1:
			if products[prod] == price:
				new[prod] = products[prod] 
		elif mode == 2:
			if products[prod] < price:
				new[prod] = products[prod]
		elif mode == 3:
			if products[prod] > price:
				new[prod] = products[prod]
	return(new)
print(user_filter(products, 550, 3))

# Get first and second best scores students
def get_best_scores(d1, num):
	c = dict()
	while len(c) < 2:
		for i, item in enumerate(d1):
			if i == 0: maxn = d1[item]
			if d1[item] > maxn:
				maxn = d1[item]
				c[item] = d1[item]
				d1[item] =  0

	print(c)

d1 = {'Student': 10, 'student1': 40, 'student3': 30}
get_best_scores(d1, 2)

# Write a Python function to get first, second best scores from the list.
# List may contain duplicates.
def get_best_score(l1,nums):
	c = list()
	while len(c) < nums:
		maxn = l1[0]
		for i, item in enumerate(l1):
			if maxn <= item:
				maxn= item
				c.append(item)
				l1.remove(item)
			c = set(c)
			c = list(c)
	return(c)
l1 = [85,85,86,84,83,25,56]
print(get_best_score(l1, 2))

##Write a Python function to shuffle and print a specified list.
from random import choice
def shuffle_list(l1:list):
	new = list()
	uniq = list()
	for i in range(0, len(l1)):
		c =  choice(l1)
		print(c)
		new.append(c)
		l1.remove(c)
		uniq.append(c)
	return(uniq)
print(shuffle_list(l1))

# Write a Python function that takes two lists and returns True if they have at least one common member.
def check_coll(a,b):
	result = False
	for i in a:
		if i in b:
			result = True
	return(result)
a = [7,8,9,1]
b = [1,2,3,4,5,6]
print(check_coll(a,b))

# ЗАДАЧА 4:
## Написати програму-гру, яка вміє загадувати натуральне число від 1 до 100. Програма повинна загадати число, та запитувати у користувача правильну відповідь, поки він не відгадає, обмеживши 10 спробами. На кожній ітерації писати - "Холодно" (Модуль різниці - більший 15), "Тепло" (Модуль різниці - від 5 до 15), або "Гаряче" (Модуль різниці - менший 5), в залежності від того, на скільки користувач близький до відповіді.
from math import fabs
from random import randint

number = randint(1,100)
u_input = int(input("Enter your integer: "))
while u_input != number:
	if fabs((u_input - number)) > 15:
		print('Cold')
		u_input = int(input("Enter your integer: "))
	elif fabs((u_input - number)) < 15 and fabs((u_input - number)) > 5:
		print('Warm')
		u_input = int(input("Enter your integer: "))
	elif fabs((u_input - number)) < 5:
		print('Hot')
		u_input = int(input("Enter your integer: "))
print('Success')


# ЗАДАЧА 3:
# Розробити функцію counter(a, b),
# Яка приймає 2 аргументи -- цілі невід'ємні числа a та b, та повертає число -- кількість різних цифр числа b, які містяться у числі а.
# Наприклад:
# Виклик функції: counter(12345, 567)
# Повертає: 1
# Виклик функції: counter(1233211, 12128)
# Повертає: 2
# Виклик функції: counter(123, 45)
# Повертає: 0
a = '1233211'
b = '12128'
def counter (a,b):
	c =  list()
	for n in b:
		if n in a and n not in c:
			c.append(n)
	print(len(c))
counter(a,b)

# ЗАДАЧА 2:
# Написати функцію, яка перетворює рядок в словник, де ключ - буква, а значення - її кількість в рядку.
# Наприклад, з вхідними даними : 'beetrootacademy'
# Очікується: {'a': 2, 'b': 1, 'c': 1, 'd': 1, 'e': 3, 'm': 1, 'o': 2, 'r': 1, 't': 2, 'y': 1}
def count_letter(word:str):
	d1 = dict()
	for letter in word:
		if not letter.isspace() :
			d1[letter] = word.count(letter)
	return(d1)
word = "beetrootacademy"
print(count_letter(word))

# ЗАДАЧА 1:
# Написати функцію, яка друкує усі унікальні значення в словнику. Приклад вхідних даних: [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"}, {"VIII":"S007"}]

d1 = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"}, {"VIII":"S007"}]
def get_uniq_values(d1):
	uniq = list()
	for i in d1:
		for value in i:
			if i[value] not in uniq:
				uniq.append(i[value])
	return('Uniq: ', uniq)
print(get_uniq_values(d1))
l1 = [1,2,3,4,5,7]


