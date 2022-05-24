from Config import databaseConnectionFile


def insertMCQAnswerFunction(dataDict):
    objFirebase = databaseConnectionFile.databaseConnectionFunction()
    
    try:
        
        objFirebase.post('Account/MCQAnswers', dataDict)
        
        return True
        
    except:
        
        return False