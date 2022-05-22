from Config import connectionFile

def dashboardRetrieveDetailsFunction(emailIDGotten):
    status, value = connectionFile.connection()
    
    databaseObject = value.database()

    firebaseData = databaseObject.child('Account/PersonalData').get()
    
    for eachData in firebaseData:
        eachEmail = eachData.val()['email']
        
        if (eachEmail == emailIDGotten):
            firebaseData = eachData.val()
            break
    
    #print(firebaseData)
    
    
    return True, firebaseData