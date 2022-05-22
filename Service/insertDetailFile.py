from Config import databaseConnectionFile


def insertDetailFunction(dataDict):
    objFirebase = databaseConnectionFile.databaseConnectionFunction()
    
    try:
        
        objFirebase.post('Account/PersonalData', dataDict)
        
        return True
    
    except:
        
        return False