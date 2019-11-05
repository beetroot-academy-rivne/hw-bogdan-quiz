#Beetroot python
# task 1
# Create new class SortedList, by extending standard list functionality to keep it sorted 
# on creation, appending new elements, adding another list
# e.g. sorted_list = SortedList([2, 3, 1])
# sorted_list -> [1, 2, 3]
# use following function to test your new class
# test_sorted_list(SortedList) -> 'Congrads!'

class SortedList(list):
	 def __init__(self, l1):
	 	self.l1 = sorted(l1)
	 def __repr__(self):
	 	return(str(self.l1))
	 def __add__(self, el):
	 	return(SortedList(self.l1 + el))
	 def append(self, el):
	 	self.l1.append(el)
	 	self.l1 = sorted(self.l1)

def test_sorted_list(s_list_class):
	errors_list = []

	s_list = s_list_class([1, 3, 5, 6, 4, 2])
	expected_list = [1, 2, 3, 4, 5, 6]
	if s_list != SortedList(expected_list):
		errors_list.append('List not sorted on creation')

	s_list.append(-1)
	expected_list.insert(0, -1)

	if s_list != SortedList(expected_list):
		errors_list.append('List is not sorted on append')

	s_list = s_list + [10, -5]
	expected_list = [-5, -1, 1, 2, 3, 4, 5, 6, 10] 
	if s_list != SortedList(expected_list):
		errors_list.append('List is not sorted on summation')

	if errors_list:
		print('Please, update SortedList to fix following errors:')
		for err in errors_list: print(err)
	else:
		print('Congrads!')
test_sorted_list(SortedList)
s_list = SortedList([1, 3, 5, 6, 4, 2])

# task 2
# Create new class NewDict that will provide an empty list as a default value for a non-existing key
# Instead of rising KeyError as a regular dictionary will.  
# Data type like that would let us easily deal with different kind of collections
# Hint: accessing dictionary via square parentness syntax `dictionary[key]` 
# uses __getitem__ magic method
# you will need to find the method for setting dictionary item like `dictionary[key] = val`
# school = NewDict()
# school['students'].extend('Alex', 'Ira', 'Bohdan') # regular dictionary would rise KeyError
# school 
# {'students': ['Alex', 'Ira', 'Bohdan']}
# Check your implementation using `test_new_dictionary(NewDict)`

class NewDict(dict):
	"""docstring for NewDict"""
	def __init__(self):
		self.d1 = dict()
		self.keys = list()
	def extend(self, l1):
		key = self.__getitem__()
		self.d1[self.__getitem__()] = list()
	# def __getitem__(self, item='None'):
		# new = NewDict()
		# self.keys.append(item)
		# return(new)
school = NewDict()
print(school['student'], type(school))


	
def test_new_dictionary(new_dict_class):
	city_list = [('TX','Austin'), ('TX','Houston'), ('NY','Albany'), 
				 ('NY', 'Syracuse'), ('NY', 'Buffalo'), ('NY', 'Rochester'), 
				 ('TX', 'Dallas'), ('CA','Sacramento'), ('CA', 'Palo Alto'), 
				 ('GA', 'Atlanta')]

	expected_dict = {'NY': ['Albany', 'Syracuse', 'Buffalo', 'Rochester'],
					 'CA': ['Sacramento', 'Palo Alto'],
					 'GA': ['Atlanta'],
					 'TX': ['Austin', 'Houston', 'Dallas']}

	cities_by_state = new_dict_class()
	for state, city in city_list:
		cities_by_state[state].append(city)

	if cities_by_state != expected_dict:
		print('Sorry, something went wrong. Try again.')
	else:
		print('Updated dictionary works as a charm! Great job!')

# task3
# Update the quiz program using classes
# class Questions with `questions_list` attribute, `get_random`, `get_by_id`, methods
# class User with `name`, `password` and `score` attributes 
# class Question with `id`, `choices`, `content`, `correct_choice` attributes
# both `User` and `Questins` classes have `from_file` method to create user object 
# by reading information from json file (list of questions in json file for Question, use questions file you have)
# Connect everything with `run_quiz(question_obj, user_obj)` function
# Feel free to add/modify/change example classes as you wish
# Only requirement is to impelement `from_file` functionality
# And operate with Question class instances inside Questions class	
