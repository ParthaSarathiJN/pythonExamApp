import random
from tkinter import *

def captchaExpressionGenerationFunction():
    
    LHSvalue = StringVar()
    LHSvalue.set(str(random.randint(1, 10)))

    RHSvalue = StringVar()
    RHSvalue.set(str(random.randint(1, 10)))

    OPvalue = StringVar()
    operator = random.choice('+-*')
    OPvalue.set(operator)

    expression = LHSvalue.get() + OPvalue.get() + RHSvalue.get()
    #print(expression)
    return expression, LHSvalue.get(), OPvalue.get(), RHSvalue.get()


def captchaExpressionValidationFunction(captchaRelatedList, captchaUserEntry):
    captchaExpression, LHSvalue, OPvalue, RHSvalue = captchaRelatedList[0], captchaRelatedList[1], captchaRelatedList[2], captchaRelatedList[3]

    
    #print(LHSvalue, OPvalue, RHSvalue)
    result = 9999
    
    if OPvalue == "+":
        result = int(LHSvalue) + int(RHSvalue)
    elif OPvalue == "-":
        result = int(LHSvalue) - int(RHSvalue)
    else:
        result = int(LHSvalue) * int(RHSvalue)
    #print(result)
    
    #print(type(captchaUserEntry), type(result))
    
    if int(captchaUserEntry) == int(result):
        #print("Validated")
        return True
    else:
        #print("Invalid Captcha")
        return False
