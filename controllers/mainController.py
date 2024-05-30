from models.mainModel import Model
from views.mainView import View
import signal
from .startController import StartController
from .modeselectorController import ModeselectorController
from .logginController import LogginController
from .timeController import TimeCounter
from .changeholdopentimeController import ChangeholdopentimeController
from .changespeedController import ChangespeedController
from .settingsController import SettingsController
from .changepasswordController import ChangePasswordController
from .errormenuController import ErrorMenuController

import threading

class Controller:

    def alarm_handler(self, signum, frame):
        self.view.switchFrame("start")
        self.model.logginmodel.logg_out()
        signal.alarm(0)


    def clicked():
        #signal.alarm(0)
        signal.alarm(10)
        #print("click registered")
    

    def __init__(self, model: Model, view: View) -> None:
        self.view = view
        self.model = model
        timer = TimeCounter()
        self.startcontroller = StartController(model,view,timer)
        self.modeselectorController = ModeselectorController(model,view,timer)
        self.logginController = LogginController(model, view,timer)
        self.changespeedController = ChangespeedController(model,view,timer)
        self.changeholdopentimeController = ChangeholdopentimeController(model,view,timer)
        self.settingsController = SettingsController(model,view,timer)
        self.changePasswordController = ChangePasswordController(model, view,timer)
        self.errormenuController = ErrorMenuController(model,view,timer)
        
        self.model.logginmodel.add_event_listener("successfull_loggin",self.logginController.enter_mode_selector)
        self.model.logginmodel.add_event_listener("Unsuccessfull_loggin", self.logginController.unsucessfullLogin)
        self.model.settingmodel.add_event_listener("settingchanged", self.settingChanged)
        self.model.logginmodel.add_event_listener("password_changed", self.changePasswordController.successfullChange)
        self.model.logginmodel.add_event_listener("Authenticated", self.logginController.enter_settings)
        self.model.logginmodel.add_event_listener("change mode", self.modeselectorController.changeMode)
        self.model.logginmodel.add_event_listener("Enter second password", self.changePasswordController.ReenterPassword)
        self.model.errormessagemodel.add_event_listener("errorsChanged", self.errormenuController.updateErrors)
        self.model.logginmodel.add_event_listener("undo", self.logginController.undo)
        self.model.logginmodel.add_event_listener("undo2", self.changePasswordController.undo2)
        self.model.logginmodel.add_event_listener("alarm", self.clicked)
        self.model.logginmodel.add_event_listener("changefailed", self.changePasswordController.changefailed)
        self.model.settingmodel.add_event_listener("updatehot", self.changeholdopentimeController.update_view)
        self.model.settingmodel.add_event_listener("updatespeed", self.changespeedController.update_view)
        self.model.errormessagemodel.add_event_listener("alertmodechanged", self.modeselectorController.alertModeHasChanged)



        signal.signal(signal.SIGALRM, self.alarm_handler)
        signal.alarm(10)

    def settingChanged(self):
        self.changespeedController.update_view()
    
    def start(self) -> None:
        self.view.switchFrame("start")
        self.view.start_mainloop()


        
