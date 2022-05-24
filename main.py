from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
import random
import sys
#sys.path.append('Service')
from Service import createAccountFile , insertDetailFile, insertMediaFile, loginToAccountFile, loginTimeStoreFile, dashboardRetrieveDetailsFile, updateDashboardDetailsFile, captchaRelatedFile, retrieveSecurityQuestionFile, findNumberOfCorrectAnswersFile, insertMCQAnswerFile
from Mapper import prepareObject
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
from tkinter import messagebox


numberCountForMCQQuestion = 1
answerForMCQOptionList = [None,None,None,None,None]

#len@len.com byt3fmajI

securityQADict = {}



def captchaRefreshFunction():
    global captchaRelatedList
    captchaExpression, LHSvalue, OPvalue, RHSvalue = captchaRelatedFile.captchaExpressionGenerationFunction()
    captchaLabel.configure(text=captchaExpression)
    captchaRelatedList = [captchaExpression, LHSvalue, OPvalue, RHSvalue]
    #print(captchaExpression, LHSvalue, OPvalue, RHSvalue)


def captchaValidateFunction():
    validatedCaptchaValue = captchaRelatedFile.captchaExpressionValidationFunction(captchaRelatedList, captchaUserEntry.get())
    
    if (validatedCaptchaValue):
        LoginLoginButton['state']=NORMAL
        print("Captcha Validated Successfully")
        
    else:
        LoginLoginButton['state']=NORMAL
        print("Captcha Validation Failure")
        print("SET TO TRUE SO NO NEED TO ENTER CAPTCHA IN captchaValidateFunction\n")



def SBQExamStartFunction(emailIDGotten):
    
    def startActualSBQTestFrameFunction():
        
        def nextQuestionSBQFunction():
            
            SBQQuestionAndTextAnswerFrame.place(x=5, y=10, height=600, width=900)
            SBQQuestionSelectoionFrame.place(x=920, y=10, height=600, width=255)
            
            SBQQuestionLabel = Label(SBQQuestionAndTextAnswerFrame, bg="black", fg="white", font=("Fira Code", 14))
            SBQQuestionLabel.configure(text=questionsForSBQ[0])
            SBQQuestionLabel.place(x=20, y=40)
            
            
            
            
            
            def saveEnteredMCQAnswerButtonFunction(answerForPrevMCQ):
                pass
                
                
            """def nextQuestionChooserFunction():
                SBQQuestionLabel.configure(text=questionsForSBQ[])
                
                def saveTheAnswersAndCountMCQFunction():
                    
                    
                    MCQQuestionAndAnswerFrame.place_forget()
                    MCQQuestionSelectorFrame.place_forget()
                    actualMCQTestFrame.place_forget()
                    
                    allEncompassDashboardFrame.place(x=60,y=40, height=800, width=1150)
            """        
                    
                    
            
            
            nextMCQQuestionButton = Button(SBQQuestionAndTextAnswerFrame, text='Next', bg='black', fg='white')
            nextMCQQuestionButton.place(x=220, y=370)
            
            saveMCQQuestionButton = Button(SBQQuestionAndTextAnswerFrame, text='Save', bg='black', fg='white')
            saveMCQQuestionButton.place(x=170, y=370)
            
            
        SBQInstructionsFrame.place_forget()
        
        actualSBQTestFrame.place(x=40, y=30, height=630, width=1200)
        
        questionsForSBQ = ["What is life?", "What is love?", "What is death?", "How was the Universe created?", "Would you choose love over money?"]
        
        
        nextQuestionSBQFunction()
        
    
    allEncompassDashboardFrame.place_forget()

    w.attributes('-fullscreen', True)
    w.configure(background='black')
    
    
    SBQInstructionsFrame.place(x=230, y=30, height=600, width=800)
    
    emailOfUserTakingTestSBQLabel = Label(SBQInstructionsFrame, text = emailIDGotten, bg="black", fg="white", font=("Fira Code", 12))
    emailOfUserTakingTestSBQLabel.place(x=630, y=20)
    
    instructionLabel = Label(SBQInstructionsFrame, text = "Instructions", bg="black", fg="white", font=("Fira Code", 14))
    instructionLabel.place(x=320, y=70)
    instructionLabelDet1 = Label(SBQInstructionsFrame, text = "1.) Read The Instructions.", bg="black", fg="white", font=("Fira Code", 10))
    instructionLabelDet1.place(x=20, y=120)
    instructionLabelDet2 = Label(SBQInstructionsFrame, text = "2.) Write the appropriate answer.", bg="black", fg="white", font=("Fira Code", 10))
    instructionLabelDet2.place(x=20, y=150)
    instructionLabelDet3 = Label(SBQInstructionsFrame, text = "3.) Click \"Save and Next\" to go to next question.", bg="black", fg="white", font=("Fira Code", 10))
    instructionLabelDet3.place(x=20, y=180)
    instructionLabelDet4 = Label(SBQInstructionsFrame, text = "4.) Complete the test before the timer runs out.", bg="black", fg="white", font=("Fira Code", 10))
    instructionLabelDet4.place(x=20, y=210)


    startSBQTestInNewFrameButton = Button(SBQInstructionsFrame, text='Start!', bg='black', fg='white', command=startActualSBQTestFrameFunction)
    w.after(1000, startActualSBQTestFrameFunction)
    startSBQTestInNewFrameButton.place(x=380, y=376)
    

def MCQExamStartFunction(emailIDGotten):
    
    global numberCountForMCQQuestion
    global answerForMCQOptionList
    
    if numberCountForMCQQuestion == 5:
        messagebox.showinfo('Error',"MCQ Test already taken IDIOT!")
        allEncompassDashboardFrame.place(x=60,y=40, height=800, width=1150)
        return 0
    
    def actualStartTestFrameMCQFunction():
        global numberCountForMCQQuestion
        global answerForMCQOptionList
        
        def nextQuestionFunction():
            global numberCountForMCQQuestion
            global answerForMCQOptionList
            
            MCQQuestionAndAnswerFrame.place(x=5, y=10, height=600, width=900)
            
            MCQQuestionSelectorFrame.place(x=920, y=10, height=600, width=255)
            
            
            
            answerForMCQRadioButton = StringVar()
            answerForMCQRadioButton.set(False)
            
            MCQQuestionLabel = Label(MCQQuestionAndAnswerFrame, bg="black", fg="white", font=("Fira Code", 12))
            MCQQuestionLabel.configure(text=QuestionListForMCQ[0])
            MCQQuestionLabel.place(x=20, y=40)
            
            option_01ForMCQRadioButton = Radiobutton(MCQQuestionAndAnswerFrame, text = "1. "+AnswerListForMCQRadio[0][1], variable = answerForMCQRadioButton, value = AnswerListForMCQRadio[0][1])
            option_01ForMCQRadioButton.place(x = 20, y = 90)
            option_02ForMCQRadioButton = Radiobutton(MCQQuestionAndAnswerFrame, text = "2. "+AnswerListForMCQRadio[0][2], variable = answerForMCQRadioButton, value = AnswerListForMCQRadio[0][2])
            option_02ForMCQRadioButton.place(x = 20, y = 130)
            option_03ForMCQRadioButton = Radiobutton(MCQQuestionAndAnswerFrame, text = "3. "+AnswerListForMCQRadio[0][3], variable = answerForMCQRadioButton, value = AnswerListForMCQRadio[0][3])
            option_03ForMCQRadioButton.place(x = 20, y = 170)
            option_04ForMCQRadioButton = Radiobutton(MCQQuestionAndAnswerFrame, text = "4. "+AnswerListForMCQRadio[0][4], variable = answerForMCQRadioButton, value = AnswerListForMCQRadio[0][4])
            option_04ForMCQRadioButton.place(x = 20, y = 210)
            
            
            def saveEnteredMCQAnswerButtonFunction(answerForPrevMCQ):
                global numberCountForMCQQuestion
                global answerForMCQOptionList
                
                
                if answerForPrevMCQ in AnswerListForMCQRadio[int(numberCountForMCQQuestion) - 1]:                    
                    answerForMCQOptionList[int(numberCountForMCQQuestion) - 1] = answerForPrevMCQ
                
                #print(answerForMCQOptionList)
            
            def nextQuestionChooserFunction():
                global numberCountForMCQQuestion
                global answerForMCQOptionList
                
                
                answerForMCQRadioButton = StringVar()
                answerForMCQRadioButton.set(False)
                
                MCQQuestionLabel.configure(text=QuestionListForMCQ[numberCountForMCQQuestion])
                option_01ForMCQRadioButton.configure(text=AnswerListForMCQRadio[numberCountForMCQQuestion][1], value = AnswerListForMCQRadio[numberCountForMCQQuestion][1])
                option_02ForMCQRadioButton.configure(text=AnswerListForMCQRadio[numberCountForMCQQuestion][2], value = AnswerListForMCQRadio[numberCountForMCQQuestion][2])
                option_03ForMCQRadioButton.configure(text=AnswerListForMCQRadio[numberCountForMCQQuestion][3], value = AnswerListForMCQRadio[numberCountForMCQQuestion][3])
                option_04ForMCQRadioButton.configure(text=AnswerListForMCQRadio[numberCountForMCQQuestion][4], value = AnswerListForMCQRadio[numberCountForMCQQuestion][4])
                numberCountForMCQQuestion += 1
                
                
                def saveTheAnswersAndCountMCQFunction():
                    global numberCountForMCQQuestion
                    global answerForMCQOptionList
                    
                    MCQQuestionAndAnswerFrame.place_forget()
                    MCQQuestionSelectorFrame.place_forget()
                    actualMCQTestFrame.place_forget()
                    
                    allEncompassDashboardFrame.place(x=60,y=40, height=800, width=1150)
                    
                    correctMCQAnswerCountForUser = findNumberOfCorrectAnswersFile.findNumberOfCorrectAnswersFunction(numberCountForMCQQuestion, AnswerListForMCQRadio, answerForMCQOptionList)
                    
                    print(correctMCQAnswerCountForUser, answerForMCQOptionList)
                    
                    MCQMarksObtainedLabel.configure(text=correctMCQAnswerCountForUser)
                    
                    MCQQuestionAndAnswerDict = prepareObject.prepareObjectMCQAnswersFunction(emailIDGotten, QuestionListForMCQ, answerForMCQOptionList)

                    if(insertMCQAnswerFile.insertMCQAnswerFunction(MCQQuestionAndAnswerDict)):
                        print("MCQ Answers Recorded in Server")
                    
                    
                if numberCountForMCQQuestion == 5:
                    nextMCQQuestionButton['state']=DISABLED
                    submitMCQAnswerButton = Button(MCQQuestionAndAnswerFrame, text='Submit Test!', bg='black', fg='white', command=saveTheAnswersAndCountMCQFunction)
                    submitMCQAnswerButton.place(x=160, y=420)
            
            
            nextMCQQuestionButton = Button(MCQQuestionAndAnswerFrame, text='Next', bg='black', fg='white', command=nextQuestionChooserFunction)
            nextMCQQuestionButton.place(x=220, y=370)
            
            saveMCQQuestionButton = Button(MCQQuestionAndAnswerFrame, text='Save', bg='black', fg='white', command=lambda:saveEnteredMCQAnswerButtonFunction(answerForMCQRadioButton.get()))
            saveMCQQuestionButton.place(x=170, y=370)
            
            
        MCQInstructionsFrame.place_forget()
        
        actualMCQTestFrame.place(x=40, y=30, height=630, width=1200)
        
        QuestionListForMCQ = ["What is the capital of India?", "Who is Partha\'s role model?", "Who can kill 10 lions with ONE hand", "How many people are needed to change a lightbulb?", "Which is the fatest car?"]
        AnswerListForMCQRadio = [["Delhi", "Bangalore", "Kolkata", "Delhi", "Hyderabad"], ["Modi", "Biden", "Modi", "Osama Bin Laden", "Donald Trump"], ["Partha", "Me", "I", "You", "Partha"], ["1", "0", "1000", "1", "999999"], ["Chiron", "Chiron", "Apache", "Motor Boat", "F-35"]]
        
        nextQuestionFunction()


    allEncompassDashboardFrame.place_forget()

    w.attributes('-fullscreen', True)
    w.configure(background='black')
    
    
    MCQInstructionsFrame.place(x=230, y=30, height=600, width=800)
    
    emailOfUserTakingTest = Label(MCQInstructionsFrame, text = emailIDGotten, bg="black", fg="white", font=("Fira Code", 12))
    emailOfUserTakingTest.place(x=630, y=20)
    
    instructionLabel = Label(MCQInstructionsFrame, text = "Instructions", bg="black", fg="white", font=("Fira Code", 14))
    instructionLabel.place(x=320, y=70)
    instructionLabelDet1 = Label(MCQInstructionsFrame, text = "1.) Read The Instructions.", bg="black", fg="white", font=("Fira Code", 10))
    instructionLabelDet1.place(x=20, y=120)
    instructionLabelDet2 = Label(MCQInstructionsFrame, text = "2.) Choose the correct answer.", bg="black", fg="white", font=("Fira Code", 10))
    instructionLabelDet2.place(x=20, y=150)
    instructionLabelDet3 = Label(MCQInstructionsFrame, text = "3.) Click \"Save and Next\" to go to next question.", bg="black", fg="white", font=("Fira Code", 10))
    instructionLabelDet3.place(x=20, y=180)
    instructionLabelDet4 = Label(MCQInstructionsFrame, text = "4.) Complete the test before the timer runs out.", bg="black", fg="white", font=("Fira Code", 10))
    instructionLabelDet4.place(x=20, y=210)


    startTestMCQNewFrameButton = Button(MCQInstructionsFrame, text='Start!', bg='black', fg='white', command=actualStartTestFrameMCQFunction)
    w.after(1000, actualStartTestFrameMCQFunction)
    startTestMCQNewFrameButton.place(x=380, y=376)
    


def dashboardFunction(emailIDGotten):
    global numberCountForMCQQuestion
    
    def updateDashboardDetailsFunction():
        
        def securityQuestionCheckerValidateFunction():
            
            if(retrieveSecurityQuestionFile.checkSecurityAnswer(securityQuestionEntry.get(), retrieveSecurityAnswerFromFile)):
                print("Security Question Validated")
                dashboardActualUpdateButton['state'] = NORMAL
                
            else:
                print("Wrong Answer Given For Security Question")
        
        def updateActualDashboardDetailsFunction():
            
            updateDetailsList = [emailIDGotten, updateNameEntry.get(), dateDashboardBox.get(), nationalityUpdateCombo.get()]
            
            if (updateDashboardDetailsFile.updateDashboardDetailsFunction(updateDetailsList)):
                print("Details have been successfully updated!")
                dashboardUpdateFrame.place_forget()
                
                dashboardFunction(emailIDGotten)
                
            else:
                print("Details not updated!")
                
            
        
        nationalityList = ['Indian','American','German','French']
        
        dashboardFrame.place_forget()
        MCQandSBQBigFrame.place_forget()
        
        dashboardUpdateFrame = Frame(w, bg='black', bd=5, relief=SUNKEN) #Relief sunken, raised, flat
        dashboardUpdateFrame.place(x=250, y=40, height=800, width=800)
        
        dSecurityQuestionLabel = Label(dashboardUpdateFrame, text = "Security Question", bg="black", fg="white", font=("Arial", 18))
        dSecurityQuestionLabel.place(x=20, y=40)
        
        retrievedSecurityQuestionFromFile, retrieveSecurityAnswerFromFile = retrieveSecurityQuestionFile.retreiveSecurityQuestionFunction(emailIDGotten)
        
        actualSecurityQuestionLabel = Label(dashboardUpdateFrame, bg="black", fg="white", font=("Arial", 18))
        actualSecurityQuestionLabel.configure(text = retrievedSecurityQuestionFromFile)
        actualSecurityQuestionLabel.place(x=20, y=70)
        
        securityQuestionEntry = Entry(dashboardUpdateFrame)
        securityQuestionEntry.place(x=20, y=100)
        
        securityQuestionCheckerButton = Button(dashboardUpdateFrame, text='Validate', bg='black', fg='white', command=securityQuestionCheckerValidateFunction)
        securityQuestionCheckerButton.place(x=160, y=100)
        
        dUpdateNameLabel = Label(dashboardUpdateFrame, text = "Name", bg="black", fg="white", font=("Arial", 18))
        dUpdateNameLabel.place(x=20, y=140)
        
        updateNameEntry = Entry(dashboardUpdateFrame)
        updateNameEntry.insert(0, userDetailsData['name'])
        updateNameEntry.place(x=160, y=140)
        
        DUpdateDOBLabel = Label(dashboardUpdateFrame, text = "DOB", bg="black", fg="white", font=("Arial", 18))
        DUpdateDOBLabel.place(x=20, y=180)
        
        DPrevDOBLabel = Label(dashboardUpdateFrame, text = userDetailsData['DOB'], bg="black", fg="white", font=("Arial", 9))
        DPrevDOBLabel.place(x=120, y=180)
        
        dateDashboardBox = DateEntry(dashboardUpdateFrame)
        dateDashboardBox.place(x=240, y=180)
        
        dUpdateNationalityLabel = Label(dashboardUpdateFrame, text = "Nationality", bg="black", fg="white", font=("Arial", 18))
        dUpdateNationalityLabel.place(x=20, y=220)
        
        nationalityUpdateCombo = ttk.Combobox(dashboardUpdateFrame)
        nationalityUpdateCombo['value'] = ('Indian','American','German','French')
        
        nationalityUpdateCombo.current(nationalityList.index(userDetailsData['nationality']))
        nationalityUpdateCombo.place(x=160, y=220)
        
        dashboardActualUpdateButton = Button(dashboardUpdateFrame, text='Update!', bg='black', fg='white', command=updateActualDashboardDetailsFunction)
        dashboardActualUpdateButton.place(x=380, y=350)
        dashboardActualUpdateButton['state'] = DISABLED
        
    
    signupFrame.place_forget()
    loginFrame.place_forget()
    
    allEncompassDashboardFrame.place(x=60,y=40, height=800, width=1150)
    
    dashboardFrame.place(x=50, y=40, height=700, width=350)
    MCQandSBQBigFrame.place(x=500, y=40, height=700, width=600)
    MCQOnlyFrame.place(x=20, y=40, height=400, width=260)
    SBQOnlyFrame.place(x=300, y=40, height=400, width=260)
    
    boolValue, userDetailsData = dashboardRetrieveDetailsFile.dashboardRetrieveDetailsFunction(emailIDGotten)
    
    
    dNameLabel = Label(dashboardFrame, text = "Name", bg="black", fg="white", font=("Arial", 18))
    dNameLabel.place(x=20, y=300)
    
    actualDNameLabel = Label(dashboardFrame, bg="black", fg="white", font=("Arial", 18))
    actualDNameLabel.configure(text=userDetailsData['name'])
    actualDNameLabel.place(x=150, y=300)
    
    dEmailLabel = Label(dashboardFrame, text = "Email", bg="black", fg="white", font=("Arial", 18))
    dEmailLabel.place(x=20, y=350)
    
    actualDEmailLabel = Label(dashboardFrame, bg="black", fg="white", font=("Arial", 18))
    actualDEmailLabel.configure(text=userDetailsData['email'])
    actualDEmailLabel.place(x=150, y=350)
    
    DDOBLabel = Label(dashboardFrame, text = "DOB", bg="black", fg="white", font=("Arial", 18))
    DDOBLabel.place(x=20, y=400)
    
    actualDDOBLabel = Label(dashboardFrame, bg="black", fg="white", font=("Arial", 18))
    actualDDOBLabel.configure(text=userDetailsData['DOB'])
    actualDDOBLabel.place(x=150, y=400)
    
    dNationalityLabel = Label(dashboardFrame, text = "Nationality", bg="black", fg="white", font=("Arial", 18))
    dNationalityLabel.place(x=20, y=450)
    
    actualDNationalyLabel = Label(dashboardFrame, bg="black", fg="white", font=("Arial", 18))
    actualDNationalyLabel.configure(text=userDetailsData['nationality'])
    actualDNationalyLabel.place(x=150, y=450)
    
    
    dashboardUpdateButton = Button(dashboardFrame, text='Update', bg='black', fg='white', command=updateDashboardDetailsFunction)
    dashboardUpdateButton.place(x=180, y=520)
    
    
    
    #MCQ LABEL AND FUNCTIONS
    MCQDisplayLabel = Label(MCQOnlyFrame, text = "MCQ", bg="black", fg="white", font=("Fira Code", 18))
    MCQDisplayLabel.place(x=95, y=50)
    
    MCQExamStartButton = Button(MCQOnlyFrame, text='Start Test', bg='black', fg='white', command=lambda:MCQExamStartFunction(emailIDGotten))
    MCQExamStartButton.place(x=100, y=140)
    #MCQExamStartButton['state'] = DISABLED
    
    MCQMarksLabel = Label(MCQOnlyFrame, bg="black", fg="white", font=("Arial", 18))
    MCQMarksLabel.configure(text = "Marks Scored")
    MCQMarksLabel.place(x=50, y=250)
    
    
    MarksScoredByUser = 0
    MCQMarksObtainedLabel.configure(text=MarksScoredByUser)
    MCQMarksObtainedLabel.place(x=120, y=290)
    
    
    
    #SBQ LABEL AND FUNCTIONS
    SBQDisplayLabel = Label(SBQOnlyFrame, text = "SBQ", bg="black", fg="white", font=("Arial", 18))
    SBQDisplayLabel.place(x=95, y=50)
    
    SBQExamStartButton = Button(SBQOnlyFrame, text='Start Test', bg='black', fg='white', command=lambda:SBQExamStartFunction(emailIDGotten))
    SBQExamStartButton.place(x=100, y=140)
    
    plagiarismLabel = Label(SBQOnlyFrame, text = "Plagiarism", bg="black", fg="white", font=("Arial", 18))
    plagiarismLabel.place(x=67, y=250)
    
    plagiarismPercentLabel = Label(SBQOnlyFrame, bg="black", fg="white", font=("Arial", 18))
    plagiarismPercentOfUser = 0
    plagiarismPercentLabel.configure(text=plagiarismPercentOfUser)
    plagiarismPercentLabel.place(x=120, y=290)
    
    
    
    #Generate Result 
    GenerateResultButton = Button(MCQandSBQBigFrame, text='Generate Result', bg='black', fg='white')
    GenerateResultButton.place(x=260, y=510)
    
    

def loginToAccount():
    #emailLoginEntryGet = emailLoginEntry.get()
    #passwordLoginEntryGet = passwordLoginEntry.get()
    
    emailLoginEntryGet = 'len@len.com'
    passwordLoginEntryGet = 'byt3fmajI'
    
    if(loginToAccountFile.loginToAccountFunction(emailLoginEntryGet, passwordLoginEntryGet)):
        print("Wrong credentials!")
        print("BUT STILL WORKS AS DEFAULT TRUE IN loginToAccount Function")
        print("Logged in successfully!")
        
        if(loginTimeStoreFile.loginTimeStoreFunction(emailLoginEntryGet)):
            print("Time Logged Successfully")
            
            dashboardFunction(emailLoginEntryGet)
            
        else:
            print("Time Not Logged In Main")
        
    else:
        print("Wrong credentials!")
        
    

def openSignupFrame():
    loginFrame.place_forget()
    signupFrame.place(x=250, y=40, height=800, width=800)


def securityFunction():
    
    def securityDictAdderFunction():
        global securityQADict 
        securityQADict = {"What is your pet name?": securityEntry1.get(),
                          "What is your favorite teacher name?": securityEntry2.get(),
                          "What is your favorite food?": securityEntry3.get(),
                          "Who is your dream girl?": securityEntry4.get(),
                          "What is your life goal?": securityEntry5.get()
                          }
        
        #securityQuestionList = ["What is your pet name?", "What is your favorite teacher name", "What is your favorite food?", "Who is your dream girl?", "What is your life goal?"]
        #securityAnswerList = [securityEntry1.get(),securityEntry2.get(),securityEntry3.get(),securityEntry4.get(),securityEntry5.get()]
        
        securityFrame.place_forget()
        
        #print(securityQuestionList, securityAnswerList)
        securityButton['state']=DISABLED
        submitButton['state']=NORMAL
        
    
    emailEntryGet = emailEntry.get()
    
    if (emailEntryGet == ""):
        print("Email not entered")
    
    else:
    
        securityFrame = Frame(w, bg='black', bd=5, relief=SUNKEN) #Relief sunken, raised, flat
        securityFrame.place(x=400, y=40, height=800, width=800)
        
        securityLabel1 = Label(securityFrame, text = "What is your pet name?", bg="black", fg="white")
        securityLabel1.place(x=20, y=50)
        
        securityEntry1 = Entry(securityFrame)
        securityEntry1.place(x=250, y=50)
    
        securityLabel2 = Label(securityFrame, text = "What is your favorite teacher name?", bg="black", fg="white")
        securityLabel2.place(x=20, y=100)    
    
        securityEntry2 = Entry(securityFrame)
        securityEntry2.place(x=250, y=100)
    
        securityLabel3 = Label(securityFrame, text = "What is your favorite food?", bg="black", fg="white")
        securityLabel3.place(x=20, y=150)
    
        securityEntry3 = Entry(securityFrame)
        securityEntry3.place(x=250, y=150)
        
        securityLabel4 = Label(securityFrame, text = "Who is your dream girl?", bg="black", fg="white")
        securityLabel4.place(x=20, y=200)
    
        securityEntry4 = Entry(securityFrame)
        securityEntry4.place(x=250, y=200)
        
        securityLabel5 = Label(securityFrame, text = "What is your life goal?", bg="black", fg="white")
        securityLabel5.place(x=20, y=250)
    
        securityEntry5 = Entry(securityFrame)
        securityEntry5.place(x=250, y=250)
        
        
        submitSecurityButton = Button(securityFrame, text='Submit', bg='black', fg='white', command=securityDictAdderFunction)
        submitSecurityButton.place(x=380, y=350)
        

def uploadFunction():
    imageSelected = askopenfilename(initialdir="",
                                    filetype=(('imgfile', '*jpg'), ('allfile', '*.*')),
                                    title="Choose a File")
    
    imagePath.set(imageSelected)
    uploadButton['state']=DISABLED
    securityButton['state']=NORMAL
    #print(imageSelected)


def submitDataFunction():
    passwordList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    emailEntryGet = emailEntry.get()
    nameEntryGet = nameEntry.get()
    nationalityComboGet = nationalityCombo.get()
    dateBoxGet = dateBox.get()
    
    passwordGenerated = ""
    
    while(len(passwordGenerated) < 9):
        passwordGenerated += random.choice(passwordList)
    
    #print(emailEntryGet, nameEntryGet, nationalityComboGet, dateBoxGet, passwordGenerated)
    print(emailEntryGet, passwordGenerated)
    if(createAccountFile.createAccountFunction(emailEntryGet, passwordGenerated)):
        print("Account Created")
        
        #Call the function insertDetail to insert data into realtime database
        #Prepare the object
        
        listOfObjects = [emailEntryGet, nameEntryGet, nationalityComboGet,dateBoxGet]
        
        #print(securityAnswerList, securityQuestionList)
        if(insertDetailFile.insertDetailFunction(prepareObject.prepareObjectFunction(listOfObjects, securityQADict))):
            print("Data sent to Realtime Database")
            
            # Insert the image into the storage server
            # path = send from here
            
            if(insertMediaFile.insertMediaFunction(imagePath.get())):
                print("Image inserted successfully")
                
                signupFrame.place_forget()
                loginFrame.place(x=250, y=40, height=800, width=800)
                
            
            else:
                print("Image was not inserted")
            
        else:
            print("Data not sent to Realtime Database")
            
    else:
        print("Account Not Created")
    
    

w = Tk()

w.geometry('1250x1250')

w.state("zoomed")
w.resizable(0,0)

w.configure(background='purple')

signupFrame = Frame(w, bg='black', bd=5, relief=SUNKEN) #Relief sunken, raised, flat
signupFrame.place(x=250, y=40, height=800, width=800)

emailLabel = Label(signupFrame, text = "E-Mail", bg="black", fg="white", font=('ariel'))
emailLabel.place(x=20, y=100)

emailEntry = Entry(signupFrame)
emailEntry.place(x=160, y=100)

nameLabel = Label(signupFrame, text = "Name", bg="black", fg="white", font=('ariel'))
nameLabel.place(x=20, y=160)

nameEntry = Entry(signupFrame)
nameEntry.place(x=160, y=160)

nameLabel = Label(signupFrame, text = "Nationality", bg="black", fg="white", font=('ariel'))
nameLabel.place(x=20, y=220)

nationalityCombo = ttk.Combobox(signupFrame)
nationalityCombo['value'] = ('Indian','American','German','French')
nationalityCombo.current(0)
nationalityCombo.place(x=160, y=220)

dateLabel = Label(signupFrame, text = "D.O.B", bg="black", fg="white", font=('ariel'))
dateLabel.place(x=20, y=280)

dateBox = DateEntry(signupFrame)
dateBox.place(x=160, y=280)

dateLabel = Label(signupFrame, text = "Upload Image", bg="black", fg="white", font=('ariel'))
dateLabel.place(x=20, y=340)

uploadButton = Button(signupFrame, text='Upload', bg='black', fg='white', command=uploadFunction)
uploadButton.place(x=160, y=340)

securityButton = Button(signupFrame, text='Security Questions!', bg='black', fg='white', command=securityFunction)
securityButton.place(x=160, y=380)
securityButton['state']=DISABLED

submitButton = Button(signupFrame, text='Submit', bg='black', fg='white', command=submitDataFunction)
submitButton.place(x=380, y=450)
submitButton['state']=DISABLED



signupFrame.place_forget()



loginFrame = Frame(w, bg='black', bd=5, relief=SUNKEN) #Relief sunken, raised, flat
loginFrame.place(x=250, y=40, height=800, width=800)


emailLoginLabel = Label(loginFrame, text = "E-Mail", bg="black", fg="white", font=('ariel'))
emailLoginLabel.place(x=20, y=100)

emailLoginEntry = Entry(loginFrame)
emailLoginEntry.place(x=160, y=100)

passwordLoginLabel = Label(loginFrame, text = "Password", bg="black", fg="white", font=('ariel'))
passwordLoginLabel.place(x=20, y=160)

passwordLoginEntry = Entry(loginFrame)
passwordLoginEntry.place(x=160, y=160)



captchaLabel = Label(loginFrame, bg='grey', fg='black')
#captchaLabel.configure(text=captchaExpression)
captchaLabel.place(x=20, y=210)


captchaRefreshFunction()

captchaRefreshButton = Button(loginFrame, text='Refresh', bg='black', fg='white', command=captchaRefreshFunction)
captchaRefreshButton.place(x=60, y=210)

captchaValidateButton = Button(loginFrame, text='Validate', bg='black', fg='white', command=captchaValidateFunction)
captchaValidateButton.place(x=160, y=260)

captchaUserEntry = Entry(loginFrame)
captchaUserEntry.place(x=20, y=260)

LoginLoginButton = Button(loginFrame, text='Login', bg='black', fg='white', command=loginToAccount)
LoginLoginButton.place(x=372, y=360)
LoginLoginButton['state'] = DISABLED

newUserLoginFrameButton = Button(loginFrame, text='New User?', bg='black', fg='white', command=openSignupFrame)
newUserLoginFrameButton.place(x=360, y=390)



allEncompassDashboardFrame = Frame(w, bg='black', bd=6, relief=SUNKEN)

dashboardFrame = Frame(allEncompassDashboardFrame, bg='black', bd=5, relief=RAISED)

MCQandSBQBigFrame = Frame(allEncompassDashboardFrame, bg='black', bd=5, relief=RAISED)
MCQOnlyFrame = Frame(MCQandSBQBigFrame, bg='black', bd=4, relief=RAISED)
SBQOnlyFrame = Frame(MCQandSBQBigFrame, bg='black', bd=4, relief=RAISED)

MCQMarksObtainedLabel = Label(MCQOnlyFrame, bg="black", fg="white", font=("Arial", 18))

MCQInstructionsFrame = Frame(w, bg='black', bd=5, relief=SUNKEN)
actualMCQTestFrame = Frame(w, bg='black', bd=5, relief=SUNKEN)
MCQQuestionAndAnswerFrame = Frame(actualMCQTestFrame, bg='black', bd=5, relief=RAISED)
MCQQuestionSelectorFrame = Frame(actualMCQTestFrame, bg='black', bd=5, relief=RAISED)

SBQInstructionsFrame = Frame(w, bg='black', bd=5, relief=SUNKEN)
actualSBQTestFrame = Frame(w, bg='black', bd=5, relief=SUNKEN)
SBQQuestionAndTextAnswerFrame = Frame(actualSBQTestFrame, bg='black', bd=5, relief=RAISED)
SBQQuestionSelectoionFrame = Frame(actualSBQTestFrame, bg='black', bd=5, relief=RAISED)

defaultImageLabel = Label(dashboardFrame, relief=RAISED)


defaultImageOpen = Image.open('C:\\Users\\Partha\\Desktop\\PythonApplication\\Project1\\ryujin.jpg')
heightOfImage, widthOfImage = defaultImageOpen.size

defaultImageOpen = defaultImageOpen.resize((200, 200))
heightOfImage, widthOfImage = defaultImageOpen.size

defaultImagePhoto = ImageTk.PhotoImage(defaultImageOpen)

defaultImageLabel.configure(image = defaultImagePhoto)
defaultImageLabel.place(x=60, y=40, height=heightOfImage, width=widthOfImage)




imagePath = StringVar()

w.mainloop()






