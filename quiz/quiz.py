from questions import get_random_question
from answers import input_answer
 
# qiuz.py
# questions.py
# answers.py
# io_response.py


def run_quiz():
	
	while True:
		question = get_random_question()
		question.print()	

		while True:
			answer = input_answer(question)	
			if not answer:
				print('Unexpected value, try again!')
			elif answer.verify(question, answer):
				print('True')
				break
			else: 
				print('False')

	# answer.verify()
	# answer.display()



if __name__ == '__main__':
	run_quiz()