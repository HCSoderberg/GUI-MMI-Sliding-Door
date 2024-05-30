import customtkinter
import tkinter
from PIL import Image, ImageTk
import time
from .ColorTheme import ColorTheme



class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("720x720")
            # USED ON RPI to get full screen
        #self.after(1000, lambda: self.attributes("-fullscreen", "True"))
        self.grid_rowconfigure(0, weight=1)  
        self.grid_columnconfigure(0, weight=1)
        self.bind('<Escape>', lambda e, w = self: w.destroy())
        self.configure(fg_color=ColorTheme.background_color)
        
        
    




        




            

        

        
