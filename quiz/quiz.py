from questions import get_random_question
from answers import Answer

# quiz.py
# questions.py
# answers.py
# io_response.py


def run_quiz():
    while True:
        question = get_random_question()
        question.print()

        while True:
            answer = Answer(question)
            if answer.is_validated and answer.verify(question):
                print("True")
                break
            else:
                print("False")

    # answer.verify()
    # answer.display()


if __name__ == "__main__":
    run_quiz()
