from random import randint
questions = [
    {
        "content": "2 + 2 - 4 = ",
        "choices": [
            {"content": "0", "is_correct": True},
            {"content": "24", "is_correct": False},
        ],
    },
    {
        "content": "18 / 2 = ",
        "choices": [
            {"content": "5", "is_correct": False},
            {"content": "9", "is_correct": True},
        ],
    },
]

def printQuestion():
    curr = randint(0,1)
    failed = True
    print(questions[curr]['content'])
    for i, var in enumerate(questions[curr]['choices']):
        print(str(i)+ ": ", var['content'])
    while failed:
        ans = input("Your answer: ")
        
        if not ans.isdigit():
            print('Enter digit only!')
        elif ans.isdigit:
            ans = int(ans)
        if questions[curr]['choices'][ans]['is_correct']:
            failed = False
        else:
            print('Wrong result, try again?')
    ans = input('Success! Type \'y\' to more one question: ')        
    if ans == 'y':
        printQuestion()
    else:
        exit()

print('Hello! Your question: ')
printQuestion()