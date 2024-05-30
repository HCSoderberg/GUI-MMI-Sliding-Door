import customtkinter
from tkinter import PhotoImage
from PIL import Image, ImageTk
import tkinter
from .ColorTheme import ColorTheme

class ModeselectorFrame(customtkinter.CTkFrame):
    buttons = []
    def __init__(self, master):
        super().__init__(master)
        self.configure(fg_color=ColorTheme.background_color)

        height = 180
        width = 300
        font = customtkinter.CTkFont(family="Helvetica",size=35,weight="bold")
        errorfont = customtkinter.CTkFont(family="Helvetica",size=25,weight="bold")

        errorimage = Image.open("./images/Error_red.png")
        ctkimage = customtkinter.CTkImage(errorimage, size=errorimage.size)
        self.error= customtkinter.CTkButton(self,fg_color=(ColorTheme.background_color),hover_color=(ColorTheme.background_color),text = "Active error",image=ctkimage, height=20,width=20,border_width=3,font=errorfont, border_color=ColorTheme.background_color, text_color=("#e8847c"))

        # Mode selector buttons

        self.auto_button= customtkinter.CTkButton(self,fg_color=(ColorTheme.button_color),hover_color=(ColorTheme.button_color),text = "Automatic", height=height,width=width,border_width=3,border_color=ColorTheme.border_color,font=font, text_color=(ColorTheme.text_color))
        self.auto_button.place(relx=0.05,rely=0.15,anchor=tkinter.NW)

        self.off_closed_button= customtkinter.CTkButton(self,fg_color=(ColorTheme.button_color),hover_color=(ColorTheme.button_color),text="Closed",height=height,width=width,border_width=3,border_color=ColorTheme.border_color,font=font, text_color=(ColorTheme.text_color))
        self.off_closed_button.place(relx=0.5,rely=0.15,anchor=tkinter.NW)

        self.auto_partial_button = customtkinter.CTkButton(self,fg_color=(ColorTheme.button_color),hover_color=(ColorTheme.button_color),text = "Auto\n partial", height=height,width=200,border_width=3,border_color=ColorTheme.border_color,font=font, text_color=(ColorTheme.text_color))
        self.auto_partial_button.place(relx=0.05,rely=0.43,anchor=tkinter.NW)

        self.hold_open_button= customtkinter.CTkButton(self,fg_color=(ColorTheme.button_color),hover_color=(ColorTheme.button_color),text = "Hold\n open", height=height,width=200,border_width=3,font=font, border_color=ColorTheme.border_color, text_color=(ColorTheme.text_color))
        self.hold_open_button.place(relx=0.35,rely=0.43,anchor=tkinter.NW)
        
        self.exit_only_button= customtkinter.CTkButton(self,fg_color=(ColorTheme.button_color),hover_color=(ColorTheme.button_color),text = "Exit\n only", height=height,width=200,border_width=3,border_color=ColorTheme.border_color,font=font, text_color=(ColorTheme.text_color))
        self.exit_only_button.place(relx=0.65,rely=0.43,anchor=tkinter.NW)
        
        settingsimage = Image.open("./images/settings.png")
        settingsimage = customtkinter.CTkImage(settingsimage, size=settingsimage.size)
        self.settings_button = customtkinter.CTkButton(self,fg_color=(ColorTheme.background_color),hover_color=(ColorTheme.background_color),text = "", image=settingsimage, height=200,width=200,border_width=3,border_color=ColorTheme.background_color,font=font, text_color=(ColorTheme.text_color))
        self.settings_button.place(relx=0.7, rely = 0.75, anchor=tkinter.NW)


        self.buttons = [self.hold_open_button, self.auto_partial_button, self.auto_button, 
                        self.exit_only_button, self.off_closed_button, self.settings_button]
    

