from questions import get_random_question
from answers import input_answer
 
# qiuz.py
# questions.py
# answers.py
# io_response.py


def run_quiz():
	question = get_random_question()
	question.print()	

	answer = input_answer(question)
	print('ans,', answer)
	if answer.verify(question, answer):
		print('success')
	else: 
		print('false')
	print(answer)
	# answer.verify()
	# answer.display()



if __name__ == '__main__':
	run_quiz()