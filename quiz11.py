from random import randint
import json

with open('questions.json') as file:
    data = file.read()
    questions = json.loads(data)
answered_questions = list()

def get_question_index(questions):
    curr = randint(0, len(questions)-1)
    if answered_questions == []:
        for i in range(0, len(questions)):
            answered_questions.append(0)
        
    while True:
        curr = randint(0, len(questions)-1)
        if answered_questions.count(2) == len(questions):
            print('Questions is over')
            exit()
        if answered_questions[curr] == 0:
            break
    
        
    answered_questions[curr] = 1 # 1 - in progress, 2 - true
    return(curr)


def printQuestion(questions):
    curr = get_question_index(questions)
    print(answered_questions)
    failed = True
    print_question = False
    print(questions[curr]['content'])
    for i, var in enumerate(questions[curr]['choices']):
        print(str(i)+ ": ", var['content'])
    while failed:
        if print_question:
            print('True answer for', curr, 'question:',true_answer(questions, curr))
        print("Your answer: ", end='')
        ans, index = get_input(questions, curr, ['q', 't', 'i'])
        # print(f'Your answer:{ans}')
        if ans == 'q':
            exit()
        elif ans == 't':
            print_question = True
            # print(true_answer(questions, curr))
        elif ans == 'i':
            info_test(questions)
        elif questions[curr]['choices'][index]['is_correct']:
            failed = False
        else:
            print('Wrong result, try again?')
    answered_questions[curr] = 2
    print('Success! Type \'y\' to more one question, anything to exit: ', end='')
    ans = input()        
    if ans == 'y':
        printQuestion(questions)
    else:
        exit()

def get_input(questions, question, add):
    expected_value = list()
    expected_value.extend(add)
    for i, var in enumerate(questions[question]['choices']):
        # print(var['content'])
        expected_value.append(var['content'][1])
        expected_value.append(var['content'].lower()[1])
    # print(expected_value)
    
    index = ''
    
    success = False
    while not success:
        inp = input()
        if inp not in expected_value:
            print("Unexpected input! Try again: ", end ='')
        else:
            success = True
    for i, var in enumerate(questions[question]['choices']):
        if inp == var['content'][1] or inp == var['content'][1].lower():
            index = i
    return inp, index
            
def true_answer(questions, question):
    for var in questions[question]['choices']:
        if var['is_correct']:
            return(var['content'][1])
def info_test(questions):
    quest = list()

    variants = [0,0,0,0,0]
    trues = list()
    stat = list()
    print('Count of varians: ')
    for i,var in enumerate(questions):
        quest.append(len(questions[i]['choices']))
    for i in range(0, max(quest)+1):
        print(i, quest.count(i))
    print()
    
    for index, var in enumerate(questions):
        for av, item in enumerate(var['choices']):
            if item['is_correct']:
                trues.append(av)
                   
        # a = input()
    for i in range(0, max(quest)):
        stat.append(trues.count(i))
        # print(i, trues.count(i)) # 2165
    print('Count of answers: ', len(questions))
    
    for i, s in enumerate(stat):
        if i == 0: letter = 'A'
        elif i == 1: letter = 'Б'
        elif i == 2: letter = 'В'
        elif i == 3: letter = 'Г'
        elif i == 4: letter = 'Д'
        else: letter = 'other'    
        # print(letter+str(stat[i]), end='')
        print(letter+':'+ str(int(100*s/len(questions)))+ '%   ', end='')
    print()    
    for i, s in enumerate(stat):
        if i == 0: letter = 'A'
        elif i == 1: letter = 'Б'
        elif i == 2: letter = 'В'
        elif i == 3: letter = 'Г'
        elif i == 4: letter = 'Д'
        else: letter = 'other'
        print(letter+':'+str(s),'   ', end='')   
    print()
    print()
    print('Answered questions: ')
    for i, ans in enumerate(answered_questions):
        if ans == 1:
            print(i, 'in progress')
        elif ans == 2:
            print(i, 'answered true')


print('Hello! Your question: (\'q\' to quit, \'t\' - print true answer, \'i\' - print info about test) \n')
printQuestion(questions)
 
# print(true_answer(questions, 0))

# get_input(questions,0, ['y', 'q'])


