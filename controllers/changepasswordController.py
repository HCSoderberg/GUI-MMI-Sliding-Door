from models.mainModel import Model
from views.mainView import View
from models.logginModel import LogginModel
from views.ColorTheme import ColorTheme
from .timeController import TimeCounter

class ChangePasswordController():
    lastButtonPressed = None
    def __init__(self, model: Model, view: View, timer : TimeCounter) -> None:
        self.model = model
        self.view = view
        self.timer = timer
        self.frame = self.view.frames["changepassword"]
        self.bind_buttons()

    def bind_buttons(self):
        self.frame.button11.configure(command=lambda button=self.frame.button11:self.number_button_action(button))
        self.frame.button22.configure(command=lambda button=self.frame.button22:self.number_button_action(button))
        self.frame.button33.configure(command=lambda button=self.frame.button33:self.number_button_action(button))
        self.frame.button44.configure(command=lambda button=self.frame.button44:self.number_button_action(button))
        self.frame.button55.configure(command=lambda button=self.frame.button55:self.number_button_action(button))
        self.frame.button66.configure(command=lambda button=self.frame.button66:self.number_button_action(button))
        self.frame.button77.configure(command=lambda button=self.frame.button77:self.number_button_action(button))
        self.frame.button88.configure(command=lambda button=self.frame.button88:self.number_button_action(button))
        self.frame.button99.configure(command=lambda button=self.frame.button99:self.number_button_action(button))
        self.frame.button00.configure(command=lambda button=self.frame.button00:self.number_button_action(button))
        self.frame.back_button.configure(command=lambda: self.back())
        self.frame.home_button.configure(command=lambda: self.enter_main_menu())
        self.frame.undobutton1.configure(command=lambda: self.model.logginmodel.undo2())


    def number_button_action(self, button):
        self.timer.clicked()
        if len(self.model.logginmodel.new_password) == 0:
            self.frame.digit11.configure(text="*")
        if len(self.model.logginmodel.new_password) == 1:
            self.frame.digit22.configure(text="*")
        if len(self.model.logginmodel.new_password) == 2:
            self.frame.digit33.configure(text="*")
        if len(self.model.logginmodel.new_password) == 3:
            self.frame.digit44.configure(text="*")
        self.change_color(button)
        #print("changed color")
        self.model.logginmodel.add_number_change(button.cget("text"))
        self.lastButtonPressed = button.cget("text")
        self.view.app.after(200,self.change_color_back)
        #print("changing color back")

    def enter_main_menu(self):
        self.timer.clicked()
        self.frame.label1.configure(text_color=ColorTheme.text_color)
        self.frame.label1.configure(text="Enter new password")
        self.view.switchFrame("modeselector")
        self.model.logginmodel.firstPassword = ""
        self.model.logginmodel.secondPassword = ""
        self.model.logginmodel.changepassworditeration = 0
        self.uncheck()  


    def undo2(self):
        self.timer.clicked()
        if len(self.model.logginmodel.new_password) == 0:
            self.frame.digit11.configure(text="")
        if len(self.model.logginmodel.new_password) == 1:
            self.frame.digit22.configure(text="")
        if len(self.model.logginmodel.new_password) == 2:
            self.frame.digit33.configure(text="")
        if len(self.model.logginmodel.new_password) == 3:
            self.frame.digit44.configure(text="")

    def change_color_back(self):
        if(self.lastButtonPressed == "1"):
            self.frame.button11.configure(fg_color=ColorTheme.button_color,hover_color=ColorTheme.button_color)
        elif(self.lastButtonPressed == "2"):
            self.frame.button22.configure(fg_color=ColorTheme.button_color,hover_color=ColorTheme.button_color)
        elif(self.lastButtonPressed == "3"):
            self.frame.button33.configure(fg_color=ColorTheme.button_color,hover_color=ColorTheme.button_color)
        elif(self.lastButtonPressed == "4"):
            self.frame.button44.configure(fg_color=ColorTheme.button_color,hover_color=ColorTheme.button_color)
        elif(self.lastButtonPressed == "5"):
            self.frame.button55.configure(fg_color=ColorTheme.button_color,hover_color=ColorTheme.button_color)
        elif(self.lastButtonPressed == "6"):
            self.frame.button66.configure(fg_color=ColorTheme.button_color,hover_color=ColorTheme.button_color)
        elif(self.lastButtonPressed == "7"):
            self.frame.button77.configure(fg_color=ColorTheme.button_color,hover_color=ColorTheme.button_color)
        elif(self.lastButtonPressed == "8"):
            self.frame.button88.configure(fg_color=ColorTheme.button_color,hover_color=ColorTheme.button_color)
        elif(self.lastButtonPressed == "9"):
            self.frame.button99.configure(fg_color=ColorTheme.button_color,hover_color=ColorTheme.button_color)
        elif(self.lastButtonPressed == "9"):
            self.frame.button00.configure(fg_color=ColorTheme.button_color,hover_color=ColorTheme.button_color)

        
    
    def change_color(self, button):
        button.configure(fg_color=ColorTheme.highlight_color,hover_color=ColorTheme.highlight_color)


    def back(self):
        self.timer.clicked()
        self.view.switchFrame("settings")
        self.frame.label1.configure(text_color=ColorTheme.text_color)
        self.frame.label1.configure(text="Enter new password")
        self.model.logginmodel.firstPassword = ""
        self.model.logginmodel.secondPassword = ""
        self.model.logginmodel.changepassworditeration = 0
        self.uncheck()
    
    def successfullChange(self):
        self.frame.label1.configure(text_color=ColorTheme.text_color)
        self.frame.label1.configure(text="Enter new password")
        self.view.switchFrame("settings")
        self.model.logginmodel.firstPassword = ""
        self.model.logginmodel.secondPassword = ""
        self.model.logginmodel.changepassworditeration = 0
        self.uncheck() 

    def ReenterPassword(self):
        self.frame.label1.configure(text_color=ColorTheme.text_color)
        self.frame.label1.configure(text="Reenter Password")
        self.uncheck()
    
    def changefailed(self): 
        self.frame.label1.configure(text_color=ColorTheme.error_color)
        self.frame.label1.configure(text="Passwords did not match. Try again")
        self.uncheck()
    
        

    def uncheck(self):
        self.frame.digit11.configure(text = " ")
        self.frame.digit22.configure(text = " ")
        self.frame.digit33.configure(text = " ")
        self.frame.digit44.configure(text = " ")
