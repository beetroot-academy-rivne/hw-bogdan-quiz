

class Answer:
    def __init__(self, question):
        self.input_answer(question)

    def input_answer(self, question):
        error = False
        expected_values = list()
        letters_map = {"А": 1, "Б": 2, "В": 3, "Г": 4, "Д": 5}
        letters = ["А", "Б", "В", "Г", "Д"]

        for index, item in enumerate(question.choices):
            expected_values.append(str(index + 1))
            expected_values.append(letters[index])

        # expected_values.extend(list(letter.keys()))
        for i, item in enumerate(question.choices):
            if item["is_correct"]:
                print("True answer:", i + 1, item["content"])

        ans = input("Enter your choice: ").upper().strip()
        result = False
        if ans not in expected_values:
            error = True

        elif ans in expected_values:
            if ans.isalpha():
                # print(ans)
                ans = letters_map[ans]
            # print(ans)
            result = "+++"
        # print(question.choices)
        if not error:
            self.is_validated = True
            self.question = question
            self.answer = ans
        else:
            self.is_validated = False
            print("Unexpected value, try again!")

    def verify(self, question):
        return question.choices[int(self.answer) - 1]["is_correct"]
