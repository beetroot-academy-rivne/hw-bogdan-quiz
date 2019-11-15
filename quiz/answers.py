
def input_answer(question):
	expected_values = list()
	letter = {'А': 1, 'Б':2, 'В': 3, 'Г': 4, 'Д': 5}

	for i, item in enumerate(question.choices):
		expected_values.append(str(i+1))
		  
	expected_values.extend(list(letter.keys()))
	for i, item in enumerate(question.choices):
		if item['is_correct']:
			print("True answer:",i+1, item['content'])
	
	ans  = input('Enter your choice: ').upper().strip()
	result = False
	print(expected_values)
	if ans in expected_values:
		if ans.isalpha():		
			# print(ans)
			ans = letter[ans]
		# print(ans)
		result = '+++'
	# print(question.choices)
	return Answer(question, ans)
class Answer:
	def __init__(self, question, ans):
		self.question = question
		self.answer = ans
		print(type(self.answer))
	def verify(self, question, ans):
		print(self.answer)
		return question.choices[int(self.answer)-1]['is_correct']
