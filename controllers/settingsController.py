from models.mainModel import Model
from views.mainView import View
from .timeController import TimeCounter

class SettingsController:
    my_next_frame = "mainmenu"
    def __init__(self, model: Model, view: View, timer: TimeCounter) -> None:
        self.model = model
        self.view = view
        self.timer = timer 
        self.frame = self.view.frames["settings"]
        self.bind_buttons()

    def bind_buttons(self):
        self.frame.home_button.configure(command=lambda: self.home_button_action())
        self.frame.change_speed_button.configure(command=lambda: self.change_speed_button_action())
        self.frame.change_hold_open_time_button.configure(command=lambda: self.hold_open_time_button_action())
        self.frame.change_password_button.configure(command= lambda: self.change_password_button_action())
        self.frame.error.configure(command=lambda:self.enter_error_menu())

    def home_button_action(self):
        self.timer.clicked()
        self.view.switchFrame("modeselector")

    def change_speed_button_action(self):
        self.timer.clicked()
        self.view.switchFrame("changespeed")
        self.model.settingmodel.trigger_event("updatespeed")

    def hold_open_time_button_action(self):
        self.timer.clicked()
        self.view.switchFrame("changeholdopentime")
        self.model.settingmodel.trigger_event("updatehot")

    def change_password_button_action(self):
        self.timer.clicked()
        self.view.switchFrame("changepassword")

    def enter_error_menu(self):
        self.timer.increaseAlarm()
        self.view.switchFrame("errormenu")  
        self.model.errormessagemodel.lastFrame = "settings"  
    
    def get_next_frame(self):
        return self.my_next_frame

    

