""" 10 Quizzes about Python """
questions = {"Who created the Python language?": 
             "A. Guido Van Rossum\nB. Alan Cooper\nC. Ada Lovelace\nD. Anders Hejlsberg", 
             "What was Python named after?": 
             "A. The Snake\nB. Monty Python's Flying Circus\nC. It came out of nowhere\nD. None of the Above", 
             "Why was the Python language made?": 
             "A. Code Readability and Easy Syntax\nB. To make programming hard\nC. No Idea\nD. None of the Above",
             "Has Python ever overtaken a language that can actually be spoken in real life in terms of popularity?": 
             "A. Maybe\nB. No\nC. Yes", 
             "What language was it?": 
             "A. German\nB. Italian\nC. Filipino\nD. French",
             "Does Python need a compiler?": 
             "A. Maybe\nB. Yes\nC. No", 
             "Is Python one of Google's official programming languages?": 
             "A. Yes\nB. Maybe\nC. No",
             "Python is a ____ level programming language?": 
             "A. High\nB. Low\nC. Middle", 
             "What is Python's first ever name?": 
             "A. CPython\nB. Python C\nC. PythonJava\nD. Python3",
             "When was Python created?": "A. 1889\nB. 2005\nC. 1993\nD. 1991"}

possible_answers = ['A,B,C,D', 'A,B,C,D', 'A,B,C,D', 'A,B,C', 'A,B,C,D', 'A,B,C', 'A,B,C', 'A,B,C', 'A,B,C,D', 'A,B,C,D']
answers = ['A', 'B', 'A', 'C', 'D', 'C', 'A', 'A', 'A', 'D']

def check_answer(player_answer, answer, possible_answer):
    possible_answers = possible_answer.split(',')
    if player_answer == "" or player_answer not in possible_answers:
        return None
    if player_answer == answer:
        print("Correct!")
        return True
    print("Incorrect!")
    return False

count = 0
amount_of_corrects = 0
amount_of_incorrects = 0
for question in questions.keys():
    answer = answers[count]
    possible_answer = possible_answers[count]
    print(f'\n{question}\n{questions[question]}\n')
    while True:
        player_answer = input("Your Answer : ")
        result = check_answer(player_answer, answer, possible_answer)
        if result == None:
            print("Give an answer! Make sure it is a valid answer!\n")
            continue
        break
    match result:
        case True:
            amount_of_corrects += 1
        case False:
            amount_of_incorrects += 1
    count += 1

if amount_of_corrects > 0 and amount_of_incorrects > 0:
    print(f'You have answered {amount_of_corrects} questions correctly.')
    print(f'You have answered {amount_of_incorrects} questions incorrectly.')
elif amount_of_incorrects > 0:
    print('YOU HAVE ANSWERED EVERYTHING WRONG.')
elif amount_of_corrects > 0:
    print('YOU HAVE SUCCESSFULLY PASSED THE QUIZ.')
