from data import question_data
from question_model import Question
from quiz_brain import Brain


score = 0
allq=0
for i in question_data:
    question = Question(list(i.values())[0],list(i.values())[1])
    brain = Brain(question.questions())
    allq+=1
    if brain.check(allq):
        score+=1
        print('correct!')
        print(f'Your current score is: {score}/{allq}')

    else:
        print('wrong!')
        print(f'Your current score is: {score}/{allq}')

print('complete!')
print(f'Your final score is {score}/{allq}')