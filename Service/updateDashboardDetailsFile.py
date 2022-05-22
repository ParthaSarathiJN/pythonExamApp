from Config import connectionFile

def updateDashboardDetailsFunction(updateDetailsList):
    status, value = connectionFile.connection()
    
    databaseObject = value.database()

    data = databaseObject.child('Account/PersonalData').get()

    for eachData in data:
        dbemailID = eachData.val()['email']
        
        if (dbemailID == updateDetailsList[0]):
            
            databaseObject.child('Account/PersonalData').child(eachData.key()).update({'name':updateDetailsList[1], 'nationality':updateDetailsList[3], 'DOB':updateDetailsList[2]})
        
            return True
        
    return False