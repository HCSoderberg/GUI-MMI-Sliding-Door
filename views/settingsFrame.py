import customtkinter
from PIL import Image, ImageTk
import tkinter
from .ColorTheme import ColorTheme

class SettingsFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(fg_color=ColorTheme.background_color)

        height = 200
        width = 300
        font = customtkinter.CTkFont(family="ADLaM Display",size=25,weight="bold")
        
        self.change_speed_button= customtkinter.CTkButton(self,fg_color=(ColorTheme.button_color),hover_color=(ColorTheme.button_color),text = "Door speed", height=height,width=width,border_width=3,font=font, border_color=ColorTheme.border_color, text_color=(ColorTheme.text_color))
        self.change_speed_button.place(relx=0.05,rely=0.15,anchor=tkinter.NW)

        self.change_hold_open_time_button= customtkinter.CTkButton(self,fg_color=(ColorTheme.button_color),hover_color=(ColorTheme.button_color),text = "Hold open time", height=height,width=width,border_width=3,font=font, border_color=ColorTheme.border_color, text_color=(ColorTheme.text_color))
        self.change_hold_open_time_button.place(relx=0.5,rely=0.15,anchor=tkinter.NW)
        
        self.change_password_button= customtkinter.CTkButton(self,fg_color=(ColorTheme.button_color),hover_color=(ColorTheme.button_color),text = "Change password", height=height,width=width,border_width=3,font=font, border_color=ColorTheme.border_color, text_color=(ColorTheme.text_color))
        self.change_password_button.place(relx=0.05,rely=0.45,anchor=tkinter.NW)

        image = Image.open("./images/home.png")
        image = customtkinter.CTkImage(image, size=image.size)
        self.home_button= customtkinter.CTkButton(self,fg_color=(ColorTheme.button_color),hover_color=(ColorTheme.button_color),image = image, text="",height=height,width=width,border_width=3,border_color=ColorTheme.border_color,font=font)
        self.home_button.place(relx=0.5,rely=0.45,anchor=tkinter.NW)

        errorimage = Image.open("./images/Error_red.png")
        errorimage = customtkinter.CTkImage(errorimage, size=errorimage.size)
        self.error= customtkinter.CTkButton(self,fg_color=(ColorTheme.background_color),hover_color=(ColorTheme.background_color),text = "Active error",image=errorimage, height=20,width=20,border_width=3,font=font, border_color=ColorTheme.background_color, text_color=("#e8847c"))
        

   