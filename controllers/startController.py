from models.mainModel import Model
from views.mainView import View
from .timeController import TimeCounter


class StartController:

    def __init__(self, model: Model, view: View, timer:TimeCounter) -> None:
        self.model = model
        self.view = view
        self.timer = timer
        self.frame = self.view.frames["start"]
        self.bind_buttons()

    def bind_buttons(self):
        self.frame.start_button.configure(command=lambda: self.enter_mode_selector_menu())
        self.frame.error.configure(command=lambda:self.enter_error_menu())

    def enter_mode_selector_menu(self):
        self.timer.clicked()
        self.view.switchFrame("modeselector")
    
    def enter_error_menu(self):
        self.timer.increaseAlarm()
        self.view.switchFrame("errormenu")
        self.model.errormessagemodel.lastFrame = "start"
    


