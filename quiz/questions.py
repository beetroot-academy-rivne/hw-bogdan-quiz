import json
from random import randint

questions = dict()
answered_questions = list()


def read_from_file(file_name="questions.json"):
    with open(file_name) as file:
        data = file.read()
        questions = json.loads(data)
    for i in range(0, len(questions)):
        answered_questions.append(0)
    return questions


QUESTIONS = read_from_file()


def get_random_question():
    curr = randint(0, len(QUESTIONS) - 1)
    # print(QUESTIONS[curr])
    # for f in QUESTIONS:s
    return Question(QUESTIONS[curr])


class Question:
    def __init__(self, curr):
        self.id = curr["id"]
        self.curr = curr
        self.content = curr["content"]
        self.choices = curr["choices"]
        self.answered_questions = list()
        self.questions = read_from_file()
        self.get_questions()

    def get_questions(self):
        pass

    def print(self):
        print(self.content)

        for i, item in enumerate(self.choices):
            # print(i, item)s
            print(str(i + 1) + ":", item["content"])
