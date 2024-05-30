from .observablemodel import ObservableModel

class ErrorMessage:
    errorNr = None
    errorName = None
    errorDescription = None
    active = False
    errorSolution = " "

    def __init__(self, errorNr, errorName, errorDescription, errorSolution):
        self.errorNr = errorNr
        self.errorName = errorName
        self.errorDescription = errorDescription
        self.errorSolution = errorSolution


class ErrorMessageModel(ObservableModel):
    errorMessageList = []
    lastFrame = None
    def __init__(self):
        super().__init__()
        self.errorMessageList.append(ErrorMessage("0","","",""))
        self.errorMessageList.append(ErrorMessage("1", "Error 1", "Description: \n This is error 1", "Solution: \n Solution to error 1"))
        self.errorMessageList.append(ErrorMessage("2", "Error 2", "Description: \n This is error 2", "Solution: \n Solution to error 2"))
        #print("Error message model initiated")
        



    def newErrorList(self, errorList):
        for error in self.errorMessageList:
            error.active = False
        for error in errorList:
                self.errorMessageList[error].active = True
        self.trigger_event("errorsChanged")

    def getActiveErrors(self): 
        nbr = 0
        for error in self.errorMessageList: 
            if error.active:
                nbr +=1
        return nbr
    
    def trigger(self):
        self.trigger_event("alertmodechanged")
