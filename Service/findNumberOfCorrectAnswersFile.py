def findNumberOfCorrectAnswersFunction(numberCountForMCQQuestion, AnswerListForMCQRadio, answerForMCQOptionList):
    
    correctMCQAnswerCountForUser = 0
    
    for allSingleOption in range(numberCountForMCQQuestion):    
        if AnswerListForMCQRadio[allSingleOption][0] == answerForMCQOptionList[allSingleOption]:
            correctMCQAnswerCountForUser += 1
    return correctMCQAnswerCountForUser