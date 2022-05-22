from firebase import firebase


def databaseConnectionFunction():
    
    try:
        objFirebase = firebase.FirebaseApplication('https://firstapplication-41bdb-default-rtdb.firebaseio.com')
        
        return objFirebase
    
    except:
        
        return "null"