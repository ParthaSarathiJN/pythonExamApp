from Service import dashboardRetrieveDetailsFile
import random

def retreiveSecurityQuestionFunction(emailIDGotten):
    valueForStatus, retreivedDetailsForSecurity = dashboardRetrieveDetailsFile.dashboardRetrieveDetailsFunction(emailIDGotten)
    print(retreivedDetailsForSecurity)
    securityQuestionUpdateListTemp = list(retreivedDetailsForSecurity.keys())
    securityQuestionUpdateListActual = [securityQuestionUpdateListTemp[1], securityQuestionUpdateListTemp[2], securityQuestionUpdateListTemp[3], securityQuestionUpdateListTemp[4], securityQuestionUpdateListTemp[5]]

    securityQuestion = random.choice(securityQuestionUpdateListActual)
    
    return securityQuestion, retreivedDetailsForSecurity[securityQuestion]

def checkSecurityAnswer(userAnswer, actualAnswer):
    if (userAnswer == actualAnswer):
        #print("Correct ansewr")
        return True
    
    else:
        #print("Wrong answer")
        return False