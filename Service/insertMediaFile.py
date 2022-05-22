from Config import connectionFile

def insertMediaFunction(imageData):
    try:
        status, firebase = connectionFile.connection()
        
        storageObject = firebase.storage()
    
        storageObject.child(imageData).put(imageData)
    
        #print("Sent Media")
        
        return True
    
    except:
        #print("Not Sent Media")
        return False
        