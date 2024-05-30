from typing import TypedDict

from .changepasswordFrame import ChangepasswordFrame
from .logginFrame import LogginFrame
from .modeselectorFrame import ModeselectorFrame
from .startFrame import StartFrame
from .mainWindow import App 
from .changeholdopentimeFrame import ChangeholdopentimeFrame
from .changespeedFrame import ChangespeedFrame
from .settingsFrame import SettingsFrame
from .errorMenuFrame import ErrorMenuFrame


class Frames(TypedDict):
    modeselector: ModeselectorFrame
    start: StartFrame
    loggin: LogginFrame
    changepassword: ChangepasswordFrame
    settings: SettingsFrame
    changeholdopentime: ChangeholdopentimeFrame
    changespeed: ChangespeedFrame
    error : ErrorMenuFrame

class View:
    def __init__(self):
        self.app = App()
        self.frames: Frames = {}

        self.add_frame(ModeselectorFrame,"modeselector")
        self.add_frame(StartFrame,"start")
        self.add_frame(LogginFrame,"loggin")
        self.add_frame(ChangepasswordFrame,"changepassword")
        self.add_frame(ChangeholdopentimeFrame, "changeholdopentime")
        self.add_frame(ChangespeedFrame, "changespeed")
        self.add_frame(SettingsFrame, "settings")
        self.add_frame(ErrorMenuFrame, "errormenu")



    def add_frame(self, Frame, name: str) -> None: 
        self.frames[name] = Frame(self.app)
        self.frames[name].grid(row=0, column=0, sticky="nsew")

    def switchFrame(self, name: str) -> None:
        frame = self.frames[name]
        frame.tkraise()

    def start_mainloop(self) -> None:
        self.app.mainloop()
