from .observablemodel import ObservableModel
import os
from controllers.timeController import TimeCounter

class LogginModel(ObservableModel):
    secondPassword = ""
    firstPassword = ""
    modeToEnter = None
    is_logged_in = False
    prevmenu = None
    prev_button = None
    next_frame_settings = False
    changepassworditeration = 0
    def __init__(self):
        super().__init__()
        self.is_logged_in=False
        self.current_password=[]
        self.new_password=[]
        self.timer = TimeCounter()
        file = open('password.txt', 'r')
        self.password = file.read()
        file.close()
        
    def add_number(self, number):
        self.timer.clicked()
        self.current_password.append(number)
        if len(self.current_password) == 4:
            self.loggin()

    def add_number_change(self, number):
        self.new_password.append(number)
        if len(self.new_password) == 4:
            self.changePassword()

    def undo2(self):
        if len(self.new_password)>0:
            self.new_password.pop()
            self.trigger_event("undo2")

    def undo(self):
        if len(self.current_password)>0:
            self.current_password.pop()
            self.trigger_event("undo")


    def loggin(self):
        from controllers.mainController import Controller 
        Controller.clicked()
        file = open('password.txt', 'r')
        self.password = file.read()
        file.close()
        current_try=""
        for element in self.current_password:
            current_try += element 
        #print(isinstance(self.password, str))
        #print("Password = ", self.password)
        #print("Your try = ", current_try)
        if(self.password == current_try): 
            self.current_password.clear()
            self.is_logged_in = True
            current_try=""
            if(self.next_frame_settings is True): 
                #print("we are in settingsmenu")
                self.next_frame_settings = False
                self.trigger_event("Authenticated")
                return
            else:
                self.trigger_event("successfull_loggin")
                self.trigger_event("change mode")
                return
        #print("unsuccess")
        self.current_password.clear()
        self.trigger_event("Unsuccessfull_loggin")


    def changePassword(self):
        if self.changepassworditeration == 0:
            #print("in first loop")
            for digit in self.new_password:
                self.firstPassword += digit
            self.changepassworditeration = 1
            self.new_password.clear()
            self.trigger_event("Enter second password")
        elif self.changepassworditeration == 1:
            for digit in self.new_password:
                self.secondPassword += digit
                self.changepassworditeration = 0
            self.new_password.clear()
            #print("in second loop, first entry: "+ self.firstPassword + (" second entry: " + self.secondPassword))
            if self.firstPassword == self.secondPassword:
                self.firstPassword = ""
                os.remove('password.txt')
                myfile = open('password.txt', 'w')
                myfile.write(self.secondPassword)
                #print("success")
                self.trigger_event("password_changed")
                myfile.close()
                self.firstPassword = ""
                self.secondPassword= ""
            else:
                self.firstPassword= ""
                self.secondPassword= ""
                self.trigger_event("changefailed")

    def main_menu(self):
        self.next_frame_settings =True
        return self.next_frame_settings
    
    def logg_out(self):
        self.is_logged_in = False

    def changePrev(self,prev):
        self.prevmenu = prev




