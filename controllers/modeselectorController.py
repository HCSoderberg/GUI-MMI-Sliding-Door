from models.mainModel import Model
from views.mainView import View
import customtkinter
from views.modeselectorFrame import ModeselectorFrame
import time 
from views.ColorTheme import ColorTheme
from .timeController import TimeCounter

class ModeselectorController():
    prev_selected_button = None
    def __init__(self, model: Model, view: View, timer: TimeCounter) -> None:
        self.model = model
        self.view = view
        self.timer = timer
        self.frame = self.view.frames["modeselector"]
        self.bind_buttons()
        #print("setting mode")
        #print(model.settingmodel.current_mode)
        if(model.settingmodel.current_mode == "Automatic"):
            self.highlight(self.frame.auto_button)
        if(model.settingmodel.current_mode == "Hold open"):
            self.highlight(self.frame.hold_open_button)
        if(model.settingmodel.current_mode == "Exit only"):
            self.highlight(self.frame.exit_only_button)
        if(model.settingmodel.current_mode == "Auto partial"):
            self.highlight(self.frame.auto_partial_button)
        if(model.settingmodel.current_mode == "Closed"):
            self.highlight(self.frame.off_closed_button)

    def bind_buttons(self):
        self.frame.exit_only_button.configure(command=lambda: self.exit_only_button_action(self.frame.exit_only_button))
        self.frame.hold_open_button.configure(command=lambda: self.hold_open_button_action(self.frame.hold_open_button))
        self.frame.auto_button.configure(command= lambda: self.auto_button_action(self.frame.auto_button))
        self.frame.auto_partial_button.configure(command= lambda: self.auto_partial_button_action(self.frame.auto_partial_button))
        self.frame.off_closed_button.configure(command= lambda: self.check_access(self.frame.off_closed_button))
        self.frame.settings_button.configure(command= lambda: self.authentication())
        self.frame.error.configure(command =lambda: self.enter_error_menu())

    def auto_partial_button_action(self, button):
        self.model.publisher.publish('c/testdevice/slidingDoor/setOpMoPartial', '')
        self.highlight(button)

    def exit_only_button_action(self, button):
         self.model.publisher.publish('c/testdevice/slidingDoor/setOpMoExit', '')
         self.highlight(button)
    
    def auto_button_action(self, button):
        self.model.publisher.publish('c/testdevice/slidingDoor/setOpMoAuto', '')
        self.highlight(button)

    def hold_open_button_action(self, button):
        self.model.publisher.publish('c/testdevice/slidingDoor/setOpMoOpen', '')
        self.highlight(button)

    def check_access(self,button):
        if(self.model.logginmodel.is_logged_in):
            self.highlight(button)
            if button.cget("text") == "Exit\n only":
                self.model.publisher.publish('c/testdevice/slidingDoor/setOpMoExit', '')
            else:
                self.model.publisher.publish('c/testdevice/slidingDoor/setOpMoOff', '')    
        else:
            
            if self.prev_selected_button is button:
                return
            self.model.logginmodel.modeToEnter = button.cget("text")
            self.view.switchFrame("loggin") 
            self.model.logginmodel.changePrev("modeselector")
            
     
    def authentication(self):
        self.timer.clicked()
        if(self.model.logginmodel.is_logged_in):
            self.view.switchFrame("settings")
        else:
            self.view.switchFrame("loggin")
            self.model.logginmodel.main_menu()
            self.model.logginmodel.changePrev("mainmenu")

    def highlight(self, button):
        self.timer.clicked()
        if self.prev_selected_button is not None:
            self.prev_selected_button.configure(fg_color=ColorTheme.button_color,hover_color=ColorTheme.button_color)
        button.configure(fg_color=ColorTheme.highlight_color,hover_color=ColorTheme.highlight_color)
        self.prev_selected_button= button
        self.current_mode = button.cget("text")
        self.model.settingmodel.change_current_mode(self.current_mode)
        self.alertModeHasChanged()

    def changeMode(self):
        if self.model.logginmodel.modeToEnter == ("Exit\n only"):
            self.highlight(self.frame.exit_only_button)
            self.model.publisher.publish('c/testdevice/slidingDoor/setOpMoExit', '') 
            

        elif self.model.logginmodel.modeToEnter == ("Closed"):
            self.model.publisher.publish('c/testdevice/slidingDoor/setOpMoOff', '') 
            self.highlight(self.frame.off_closed_button)
            
    
    def alertModeHasChanged(self):
        self.model.modeselectormodel.modeHasChanged()
        currentmode = self.model.modeselectormodel.currentMode
        self.view.frames["start"].start_button.configure(text=currentmode)
        
    def enter_error_menu(self):
        self.timer.increaseAlarm()
        self.view.switchFrame("errormenu")
        self.model.errormessagemodel.lastFrame = "modeselector" 