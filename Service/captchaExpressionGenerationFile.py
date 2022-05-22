import random
from tkinter import *

def captchaExpressionGenerationFunction():
    
    LHS = StringVar()
    LHS.set(str(random.randint(1, 10)))

    RHS = StringVar()
    RHS.set(str(random.randint(1, 10)))

    op = StringVar()
    operator = random.choice('+-*')
    op.set(operator)

    expression = LHS.get() + op.get() + RHS.get()
    print(expression)
    return expression