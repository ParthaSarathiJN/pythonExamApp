def prepareObjectFunction(listOfObjects, securityQADict):
    noOfElement = len(listOfObjects)
    
    listDict = list(securityQADict.keys())
    
    #print(listDict)
    
    dataDict = {
        'email': listOfObjects[0],
        'name': listOfObjects[1],
        'nationality': listOfObjects[2],
        'DOB': listOfObjects[3],
        listDict[0]: securityQADict[listDict[0]],
        listDict[1]: securityQADict[listDict[1]],
        listDict[2]: securityQADict[listDict[2]],
        listDict[3]: securityQADict[listDict[3]],
        listDict[4]: securityQADict[listDict[4]]
        }
    
    return dataDict

def prepareObjectLoginTimeFunction(emailID, loginTime):
    
    loginTimeDict = {
        'email': emailID,
        'loginTime': loginTime
        }
    
    return loginTimeDict

def prepareObjectMCQAnswersFunction(emailID, QuestionListForMCQ, answerListForMCQ):
    
    MCQQuestionAndAnswerDict = {
        'email':emailID,
        QuestionListForMCQ[0]:answerListForMCQ[0],
        QuestionListForMCQ[1]:answerListForMCQ[1],
        QuestionListForMCQ[2]:answerListForMCQ[2],
        QuestionListForMCQ[3]:answerListForMCQ[3],
        QuestionListForMCQ[4]:answerListForMCQ[4]
        }
        
    #print(MCQQuestionAndAnswerDict)
    
    return MCQQuestionAndAnswerDict