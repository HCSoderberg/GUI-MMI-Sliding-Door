from models.mainModel import Model
from views.mainView import View
from .timeController import TimeCounter

class ChangespeedController:

    def __init__(self, model: Model, view: View, timer: TimeCounter) -> None:
        self.model = model
        self.view = view
        self.timer = timer
        self.frame = self.view.frames["changespeed"]
        self.bind_buttons()
        self.update_view()

    def bind_buttons(self):
       self.frame.confirm_button.configure(command= lambda: self.confirm_button_action())
       self.frame.error.configure(command=lambda: self.enter_error_menu())
       self.frame.home_button.configure(command=lambda: self.home())
       self.frame.back_button.configure(command=lambda: self.back())

    def confirm_button_action(self):
        self.model.settingmodel.change_setting("opening_speed",self.frame.opening_speed_slider.get())
        self.model.settingmodel.change_setting("closing_speed", self.frame.closing_speed_slider.get())
        self.view.switchFrame("settings")

    def home(self):
        self.view.switchFrame("modeselector")

    def back(self):
        self.view.switchFrame("settings")
    
    def enter_error_menu(self):
        #self.timer.increaseAlarm()
        self.view.switchFrame("errormenu")
        self.model.errormessagemodel.lastFrame = "changespeed"

    def update_view(self):
        self.frame.opening_speed_slider.set(self.model.settingmodel.get_setting("opening_speed"))
        self.frame.closing_speed_slider.set(self.model.settingmodel.get_setting("closing_speed"))