from fastapi import FastAPI

app = FastAPI()


########################################### SCHEDULE ENDPOINTS ###############################################

#Get schedule dates:
@app.get("/scheduledates/")
def get_schedule_dates(service_type, location):

    #dates = scheduleService.GetAvailableDates(service_type, location)
    dates_times = 0
    return dates_times

#Schedule for an exam
@app.post("/schedulexam/")
def schedule_exam(userid, service_type, location, date, time):
    
    #result = scheduleService.ScheduleExam(userid, service_type, location, date, time) 
    result = True
    return result

########################################### DOCUMENT PROCESS ENDPOINTS ###############################################

#Send documents for validation
@app.post("/docs/")
def process_documents(docs):
    
    #valid = processingService.ProcessDocuments(docs) 
    valid = 1
    return valid

########################################### USER ENDPOINTS ###############################################

#User SignIn
@app.patch("/signin/")
def user_signin(email, password):
    
    #isValid = userService.SignIn(email, password) 
    isValid = 1
    return isValid

#User SignOut
@app.patch("/signout/")
def user_signout(userid):
    
    #result = userService.SignOut(userid) 
    result = 1
    return result

#User SignUp
@app.post("/signup/")
def user_signup(email, password, dateOfBirth, identityDoc, firstName, lastName):
    
    #result = userService.SignUp(email, password, dateOfBirth, identityDoc, firstName, lastName) 
    result = 1
    return result

#User SignUp
@app.get("/profile/")
def get_user(userid):
    
    #result = userService.GetUser(userid) 
    result = 1
    return result



