from Config import connectionFile

def loginToAccountFunction(emailid, password):
    status, value=connectionFile.connection()
    
    #print(status, status)
    
    if(status):
        
        try:
            authObj = value.auth()
            authObj.sign_in_with_email_and_password(emailid, password)
            
            return True
        
        except:
            
            return False
        
    else:
        
        return False


#len@len.com byt3fmajI