from .observablemodel import ObservableModel

class SettingsModel(ObservableModel):
    current_mode = 0
    hold_open_time = 0
    opening_speed = 0
    closing_speed = 0

    def __init__(self):
        super().__init__()

        settingsFile = open('settings.txt', 'r')
        #print("setting up settings")
        self.current_mode = settingsFile.readline().strip()
        #print(self.current_mode)
        settingsFile.close

        hotFile = open('settingshot.txt')
        try: 
            self.hold_open_time = float(hotFile.readline().strip())
        except ValueError:
            print("Failed to load hold open time, could not convert into float")
        hotFile.close

        osFile = open('settingsos.txt')
        try:
            self.opening_speed = float(osFile.readline().strip())
        except ValueError:
            print("Failed to load opening speed, could not convert into float")
        osFile.close

        csFile = open('settingscs.txt')
        try:
            self.closing_speed = float(csFile.readline().strip())
        except ValueError:
            print("Failed to load closing speed, could not convert into float")
        csFile.close
        
        

        
        
    


    def change_setting(self, setting, value)-> None:
        if setting == "hold_open_time":
            self.hold_open_time = value
            settingsFile = open('settingshot.txt', 'w')
            settingsFile.write(str(self.hold_open_time))
            settingsFile.close()
            self.trigger_event("settingchanged")
        elif setting == "opening_speed":
            self.opening_speed = value
            settingsFile = open('settingsos.txt', 'w')
            settingsFile.write(str(self.opening_speed))
            settingsFile.close()
            #self.trigger_event("settingchanged")
        elif setting == "closing_speed":
            self.closing_speed = value
            settingsFile = open('settingscs.txt', 'w')
            settingsFile.write(str(self.closing_speed))
            settingsFile.close()
            self.trigger_event("settingchanged")
        
    def get_setting(self, setting)-> None:
        if setting == "hold_open_time":
            return self.hold_open_time
        elif setting == "opening_speed":
            return self.opening_speed
        elif setting == "closing_speed":
            return self.closing_speed
        
    def change_current_mode(self, newmode):
        self.current_mode = newmode
        settingsFile = open('settings.txt', 'w')
        settingsFile.write(self.current_mode)
        settingsFile.close()




    







