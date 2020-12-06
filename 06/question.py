END_OF_QUESTION = "\n"

def generateQuestions(lines):
    questions = []
    currentQuestion = []
    for line in lines:
        if line == END_OF_QUESTION:
            joinedQuestion = " ".join(currentQuestion)
            questions.append(joinedQuestion)
            currentQuestion = []
        else:
            currentQuestion.append(line.strip())

    joinedQuestion = " ".join(currentQuestion)
    questions.append(joinedQuestion)

    return questions

def answerGroupQuestion(question):
    answers = question.split(" ")
    specificAnswers = {}
    for answer in answers:
        for q in answer:
            if q not in specificAnswers:
                specificAnswers[q] = True

    return len(specificAnswers.keys())

def allGroupQuestions(question):
    answers = question.split(" ")
    specificAnswers = {}
    for answer in answers:
        for q in answer:
            if q not in specificAnswers:
                specificAnswers[q] = 1
            else:
                specificAnswers[q] += 1

    count = 0
    for question in specificAnswers:
        if specificAnswers[question] == len(answers):
            count += 1

    return count

with (open('input.txt', 'r')) as file:
    lines = file.readlines()
    questions = generateQuestions(lines)
    print(questions)
    answerSize = [allGroupQuestions(question) for question in questions]
    print(sum(answerSize))
