score = 0
def question(questions,answers,score,i):
    answer = input(questions[i]+" ")
    if answer.lower() == answers[i]:
        score = score+1
        print("Correct!")
        print("Score now equals",score)
    else:
        print("Incorrect!")
        print("Score still equals",score)
    return score
questions = ["What is 2+2?","What is the capital of France?","What color is the sky?"]
answers = ["4","paris","blue"]
for i in range(len(questions)):
    score = question(questions,answers,score,i)
print("Final score:",score)



