from Config import databaseConnectionFile
from datetime import datetime
from Mapper import prepareObject

def loginTimeStoreFunction(emailID):
    objFirebase = databaseConnectionFile.databaseConnectionFunction()
    
    nowCurrentTime = datetime.now()
    dateTimeDetails = nowCurrentTime.strftime("%d/%m/%Y %H:%M:%S")
    
    loginDetailDict = prepareObject.prepareObjectLoginTimeFunction(emailID, dateTimeDetails)
    
    try:
        
        objFirebase.post('Account/LoginTime', loginDetailDict)
        #print("Login Time Saved!")
        return True
    
    except:
        
        #print("Login Time Not Saved!!")
        return False