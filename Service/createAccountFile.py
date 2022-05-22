from Config import connectionFile

def createAccountFunction(user,pswd):
    
    status, value=connectionFile.connection()
    #print(status)
    if(status):
        
        try:
            authObj = value.auth()
            authObj.create_user_with_email_and_password(user, pswd)
            
            return True
        
        except:
            return False
        
    else:
        
        return False
    
    