import customtkinter
from PIL import Image, ImageTk
import tkinter
from .ColorTheme import ColorTheme

class StartFrame(customtkinter.CTkFrame):
    

    def __init__(self, master):
        super().__init__(master)
        self.configure(fg_color=ColorTheme.background_color)
        file = open('settings.txt', 'r')
        self.mode = file.read()
        file.close()

        font = customtkinter.CTkFont(family="Helvetica",size=120)
        errorfont = customtkinter.CTkFont(family="Helvetica",size=25,weight="bold")
        errorimage = Image.open("./images/Error_red.png")
        errorimage = customtkinter.CTkImage(errorimage, size=errorimage.size)
        self.error= customtkinter.CTkButton(self,fg_color=(ColorTheme.background_color),hover_color=(ColorTheme.background_color),text = "Active error",image=errorimage, height=20,width=20,border_width=3,font=errorfont, border_color=ColorTheme.background_color, text_color=("#e8847c"))
        self.start_button= customtkinter.CTkButton(self,fg_color=(ColorTheme.background_color),hover_color=(ColorTheme.background_color), height=720,width=720,border_color=ColorTheme.background_color,text=self.mode, font = font, text_color=ColorTheme.text_color)
        self.start_button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)
        self.error.lift()

        

