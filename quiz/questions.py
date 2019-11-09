import json
from random import randint

questions = dict()
answered_questions = list()

def read_from_file(file_name='questions.json'):
	with open(file_name) as file:
	    data = file.read()
	    questions = json.loads(data)
	for i in range(0, len(questions)):
	    answered_questions.append(0)
	return questions
def get_random_question():
	questions = read_from_file()
	curr = randint(0, len(questions)-1)
	# print(questions[curr])
	for f in questions:
		print (f['id'])
	return(Question(questions[curr]))
class Question:
	def __init__(self, curr):
		self.id =  441# curr['id'] 181
		self.curr = curr
		self.answered_questions = list()
		self.questions = read_from_file()
		self.get_questions()
		
	def get_questions(self):
		pass	
	def print(self):
		print(self.id, self.curr, '\n')
		print(181, self.curr, '\n')
		print(self.questions[self.id]['content'])

		# for i, item in enumerate(self.questions[self.id]['choices']):
			# print(i, item)
			# print(str(i)+':', item['content'])
