from models.mainModel import Model
from views.mainView import View
from models.logginModel import LogginModel
from .timeController import TimeCounter
import time
from views.ColorTheme import ColorTheme

class LogginController():
    lastButtonPressed = None
    def __init__(self, model: Model, view: View, timer : TimeCounter) -> None:
        self.model = model
        self.view = view
        self.timer = timer
        self.frame = self.view.frames["loggin"]
        self.bind_buttons()

    def bind_buttons(self):
        
        self.frame.button1.configure(command=lambda button=self.frame.button1:self.number_button_action(button))
        self.frame.button2.configure(command=lambda button=self.frame.button2:self.number_button_action(button))
        self.frame.button3.configure(command=lambda button=self.frame.button3:self.number_button_action(button))
        self.frame.button4.configure(command=lambda button=self.frame.button4:self.number_button_action(button))
        self.frame.button5.configure(command=lambda button=self.frame.button5:self.number_button_action(button))
        self.frame.button6.configure(command=lambda button=self.frame.button6:self.number_button_action(button))
        self.frame.button7.configure(command=lambda button=self.frame.button7:self.number_button_action(button))
        self.frame.button8.configure(command=lambda button=self.frame.button8:self.number_button_action(button))
        self.frame.button9.configure(command=lambda button=self.frame.button9:self.number_button_action(button))
        self.frame.button0.configure(command=lambda button=self.frame.button0:self.number_button_action(button))

        self.frame.back_button.configure(command=lambda: self.back())
        self.frame.homebutton.configure(command=lambda: self.back())
        self.frame.undobutton.configure(command=lambda: self.model.logginmodel.undo())

    def number_button_action(self, button):
        self.timer.clicked()
        if len(self.model.logginmodel.current_password) == 0:
            self.frame.digit1.configure(text="*")
        if len(self.model.logginmodel.current_password) == 1:
            self.frame.digit2.configure(text="*")
        if len(self.model.logginmodel.current_password) == 2:
            self.frame.digit3.configure(text="*")
        if len(self.model.logginmodel.current_password) == 3:
            self.frame.digit4.configure(text="*")
        self.change_color(button)
        #print("changed color")
        self.model.logginmodel.add_number(button.cget("text"))
        self.lastButtonPressed = button.cget("text")
        self.view.app.after(200,self.change_color_back)
        #print("changing color back")

    def undo(self):
        self.timer.clicked()
        if len(self.model.logginmodel.current_password) == 0:
            self.frame.digit1.configure(text="")
        if len(self.model.logginmodel.current_password) == 1:
            self.frame.digit2.configure(text="")
        if len(self.model.logginmodel.current_password) == 2:
            self.frame.digit3.configure(text="")
        if len(self.model.logginmodel.current_password) == 3:
            self.frame.digit4.configure(text="")


    
    def change_color_back(self):
        if(self.lastButtonPressed == "1"):
            self.frame.button1.configure(fg_color=ColorTheme.button_color,hover_color=ColorTheme.button_color)
        elif(self.lastButtonPressed == "2"):
            self.frame.button2.configure(fg_color=ColorTheme.button_color,hover_color=ColorTheme.button_color)
        elif(self.lastButtonPressed == "3"):
            self.frame.button3.configure(fg_color=ColorTheme.button_color,hover_color=ColorTheme.button_color)
        elif(self.lastButtonPressed == "4"):
            self.frame.button4.configure(fg_color=ColorTheme.button_color,hover_color=ColorTheme.button_color)
        elif(self.lastButtonPressed == "5"):
            self.frame.button5.configure(fg_color=ColorTheme.button_color,hover_color=ColorTheme.button_color)
        elif(self.lastButtonPressed == "6"):
            self.frame.button6.configure(fg_color=ColorTheme.button_color,hover_color=ColorTheme.button_color)
        elif(self.lastButtonPressed == "7"):
            self.frame.button7.configure(fg_color=ColorTheme.button_color,hover_color=ColorTheme.button_color)
        elif(self.lastButtonPressed == "8"):
            self.frame.button8.configure(fg_color=ColorTheme.button_color,hover_color=ColorTheme.button_color)
        elif(self.lastButtonPressed == "9"):
            self.frame.button9.configure(fg_color=ColorTheme.button_color,hover_color=ColorTheme.button_color)
        elif(self.lastButtonPressed == "0"):
            self.frame.button0.configure(fg_color=ColorTheme.button_color,hover_color=ColorTheme.button_color)
                
        
    
    def change_color(self, button):
        button.configure(fg_color=ColorTheme.highlight_color,hover_color=ColorTheme.highlight_color)

    def back(self):
        self.timer.clicked()
        self.Authreq()
        self.model.logginmodel.current_password = []
        self.view.switchFrame("modeselector")

    def enter_mode_selector(self):
        self.timer.clicked()
        self.view.switchFrame("modeselector")  
        self.Authreq()

    def enter_settings(self):
        self.timer.clicked()
        self.view.switchFrame("settings")
        self.Authreq()
    
    def successfullLogin(self):
        #self.frame.label.configure(text="Successfull")
        self.uncheck()

    def unsucessfullLogin(self): 
        self.frame.label.configure(text="Wrong password. Try again")
        self.frame.label.configure(text_color=ColorTheme.error_color)
        self.uncheck()   

    def Authreq(self):
        self.frame.label.configure(text_color=ColorTheme.text_color)
        self.frame.label.configure(text="Authentication Required")
        self.uncheck()

    def uncheck(self):
        self.frame.digit1.configure(text = " ")
        self.frame.digit2.configure(text = " ")
        self.frame.digit3.configure(text = " ")
        self.frame.digit4.configure(text = " ")