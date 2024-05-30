from .observablemodel import ObservableModel


class ModeSelectorModel(ObservableModel):
    currentMode = ' '
    def __init__(self) -> None: #model: Model, view: View
        super().__init__()
        file = open('settings.txt', 'r')
        self.currentMode = file.read()
        file.close()

    def modeHasChanged(self):
        with open('settings.txt', 'r') as file: 
            self.currentMode= file.read()

        print(self.currentMode)

    def getMode(self): 
        return self.currentMode
        