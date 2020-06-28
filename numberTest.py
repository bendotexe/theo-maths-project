import random
import time
from sklearn.linear_model import LinearRegression
import numpy as np

def generateQuestion(lowerLimit, upperLimit):

    random.seed()
    a = random.randint(lowerLimit, upperLimit)
    b = random.randint(lowerLimit, upperLimit)
    c = a*b

    questionValues = [a,b,c]

    return questionValues

def modelValues(a,b,c):

    values = [a,b,c]

    for i in range(2,11):
        if a % i == 0:
            values.append(1)
        else:
            values.append(0)

    for i in range(2,11):
        if b % i == 0:
            values.append(1)
        else:
            values.append(0)

    values.append(1) # intercept

    return values

def runGame(lL,uL):

    a,b,c = generateQuestion(lL,uL)
    values = modelValues(a,b,c)

    questionString = f"{a} x {b} = "
    tic = time.perf_counter()
    userAnswer = input(questionString)
    toc = time.perf_counter()

    responseTime = toc - tic
    responseTimePrint = round(responseTime, 2)

    if userAnswer == str(c):
        print(f"correct: answered in {responseTimePrint} seconds")
        correct = 1
    else:
        print(f"wrong: answered in {responseTimePrint} seconds")
        correct = 0.1

    score = correct*100/responseTime

    return [values, score]

questionValues = []
questionResults = []
model = np.zeros(22)

lL = int(input('Enter lower limit: '))
uL = int(input('Enter upper limit: '))

while True:

    for i in range(0,10):

        values, score = runGame(lL,uL)
        questionValues.append(values)
        questionResults.append(score)
        print(model)
        print(values)
        predScore = np.dot(model, values)

        print(score)
        print(predScore)

    reg = LinearRegression().fit(questionValues, questionResults)
    model = reg.coef_
