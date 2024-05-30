from models.mainModel import Model
from views.mainView import View
from tkinter import PhotoImage
from views.errorMenuFrame import * 
from .timeController import TimeCounter



class ErrorMenuController():
    nbrErrors = 0
    def __init__(self, model: Model, view: View, timer: TimeCounter) -> None:
        
        self.model = model
        self.view = view
        self.timer = timer 
        self.frame = self.view.frames["errormenu"]
        self.frame.back_button.configure(command=lambda: self.back())
        self.frame.reset_button.configure(command=lambda: self.reset())
        self.frame.home_button.configure(command=lambda: self.home())
        errorimage = Image.open("./images/Error_red.png")
        self.errorimage = customtkinter.CTkImage(errorimage, size=errorimage.size)
        
        

    def home(self):
        self.timer.clicked()
        self.view.switchFrame("modeselector")

    def reset(self):
        print("reset")

    def back(self):
        self.timer.clicked()
        self.view.switchFrame(self.model.errormessagemodel.lastFrame)

    def addErrorMessage(self, error):
        errorNbr = self.nbrErrors
        errorNr = error.errorNr
        errorName = error.errorName
        errorDescription = error.errorDescription
        solution=error.errorSolution
        self.frame.scrollableFrame.error = ErrorMessageFrame(errorNr,errorName,errorDescription,solution,self.frame.scrollableFrame)
        self.frame.scrollableFrame.error.grid(row=self.nbrErrors, column=0,padx=10,pady=10)
        self.frame.scrollableFrame.errorMessages.append(self.frame.scrollableFrame.error)
        self.frame.scrollableFrame.error.expand_button.configure(command=lambda: self.expand(errorNbr))
        self.nbrErrors = self.nbrErrors +1        

    

        
        

    def updateErrors(self):
        
        #Remove all existing errors
        for widget in self.frame.scrollableFrame.winfo_children():
            widget.destroy()


        #Add all active Errors

        
        for error in self.model.errormessagemodel.errorMessageList:
            if error.active == True:
                self.addErrorMessage(error)
        # reveal and add error to active errors button
        

        if self.model.errormessagemodel.getActiveErrors() == 1:
            #self.view.frames["mainmenu"].error.configure(text=str(self.model.errormessagemodel.getActiveErrors()) + " Active error")
            self.view.frames["modeselector"].error.configure(text=str(self.model.errormessagemodel.getActiveErrors()) + " Active error",image=self.errorimage)
            self.view.frames["settings"].error.configure(text=str(self.model.errormessagemodel.getActiveErrors()) + " Active error",image=self.errorimage)
            self.view.frames["changeholdopentime"].error.configure(text=str(self.model.errormessagemodel.getActiveErrors()) + " Active error",image=self.errorimage)
            self.view.frames["changespeed"].error.configure(text=str(self.model.errormessagemodel.getActiveErrors()) + " Active error",image=self.errorimage)
            self.view.frames["start"].error.configure(text=str(self.model.errormessagemodel.getActiveErrors()) + " Active error",image=self.errorimage)

        else: 
            #self.view.frames["mainmenu"].error.configure(text=str(self.model.errormessagemodel.getActiveErrors()) + " Active errors")
            self.view.frames["modeselector"].error.configure(text=str(self.model.errormessagemodel.getActiveErrors()) + " Active errors",image=self.errorimage)
            self.view.frames["settings"].error.configure(text=str(self.model.errormessagemodel.getActiveErrors()) + " Active errors",image=self.errorimage)
            self.view.frames["changeholdopentime"].error.configure(text=str(self.model.errormessagemodel.getActiveErrors()) + " Active errors",image=self.errorimage)
            self.view.frames["changespeed"].error.configure(text=str(self.model.errormessagemodel.getActiveErrors()) + " Active errors",image=self.errorimage)
            self.view.frames["start"].error.configure(text=str(self.model.errormessagemodel.getActiveErrors()) + " Active errors",image=self.errorimage)

        #self.view.frames["mainmenu"].error.place(relx=0.05,rely=0.83,anchor=tkinter.NW)
        self.view.frames["modeselector"].error.place(relx=0.05,rely=0.83,anchor=tkinter.NW)
        self.view.frames["settings"].error.place(relx=0.05,rely=0.83,anchor=tkinter.NW)
        self.view.frames["changeholdopentime"].error.place(relx=0.05,rely=0.83,anchor=tkinter.NW)
        self.view.frames["changespeed"].error.place(relx=0.05,rely=0.83,anchor=tkinter.NW)
        self.view.frames["start"].error.place(relx=0.05,rely=0.83,anchor=tkinter.NW)
        if self.model.errormessagemodel.getActiveErrors()== 0:
            #self.view.frames["modeselector"].error.unbind()
            #self.view.frames["modeselector"].error.configure(text="", image=None)
            #self.view.frames["settings"].error.configure(text="", image=None)
            #self.view.frames["changeholdopentime"].error.configure(text="", image=None)
            #self.view.frames["changespeed"].error.configure(text="", image=None)
            #self.view.frames["start"].error.configure(text="", image=None)
            self.view.frames["modeselector"].error.place(relx=1,rely=0.83,anchor=tkinter.NW)
            self.view.frames["settings"].error.place(relx=1,rely=0.83,anchor=tkinter.NW)
            self.view.frames["changeholdopentime"].error.place(relx=1,rely=0.83,anchor=tkinter.NW)
            self.view.frames["changespeed"].error.place(relx=1,rely=0.83,anchor=tkinter.NW)
            self.view.frames["start"].error.place(relx=1,rely=0.83,anchor=tkinter.NW)




        #print("Active errors" , self.model.errormessagemodel.getActiveErrors())
        #print("Errors updated")

    def expand(self, errorNbr):
        #print(errorNbr)
        arrowLeft = Image.open("./images/ArrowLeft.png")
        arrowLeft = customtkinter.CTkImage(arrowLeft, size=arrowLeft.size)
        arrowDown = Image.open("./images/ArrowDown.png")
        arrowDown = customtkinter.CTkImage(arrowDown, size=arrowDown.size)
        if not self.frame.scrollableFrame.errorMessages[errorNbr].expanded:
            self.frame.scrollableFrame.errorMessages[errorNbr].expanded = True
            self.frame.scrollableFrame.errorMessages[errorNbr].configure(height=350)
            self.frame.scrollableFrame.errorMessages[errorNbr].configure(fg_color=("#13517D"))
            self.frame.scrollableFrame.errorMessages[errorNbr].description.place(x = 5, y = 100)
            self.frame.scrollableFrame.errorMessages[errorNbr].solution.place(x=5, y=190)
            self.frame.scrollableFrame.errorMessages[errorNbr].expand_button.configure(image=arrowDown)
        elif self.frame.scrollableFrame.errorMessages[errorNbr].expanded:
            self.frame.scrollableFrame.errorMessages[errorNbr].expanded = False
            self.frame.scrollableFrame.errorMessages[errorNbr].configure(height=100)
            self.frame.scrollableFrame.errorMessages[errorNbr].configure(fg_color="#00A0D0")
            self.frame.scrollableFrame.errorMessages[errorNbr].expand_button.configure(image=arrowLeft)
