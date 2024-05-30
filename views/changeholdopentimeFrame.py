import customtkinter
from PIL import Image, ImageTk
import tkinter
from .ColorTheme import ColorTheme

class ChangeholdopentimeFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(fg_color=ColorTheme.background_color)
        
        font = customtkinter.CTkFont(family="ADLaM Display",size=35,weight="bold")
        errorfont = customtkinter.CTkFont(family="Helvetica",size=25,weight="bold")
        smallfont =customtkinter.CTkFont(family="Helvetica",size=15,weight="bold")

        hold_open_time_text = tkinter.StringVar(value="HOLD OPEN TIME")
        self.hold_open_time_label = customtkinter.CTkLabel(self, textvariable= hold_open_time_text, width=160, height= 25, fg_color=ColorTheme.background_color,text_color=(ColorTheme.text_color), font=font)
        self.hold_open_time_label.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

        self.hold_open_time_slider = customtkinter.CTkSlider(self, from_=0, to=8, width=600, height=40, number_of_steps=8)
        self.hold_open_time_slider.place(relx=0.5, rely= 0.4, anchor=tkinter.CENTER)

        text_0 = tkinter.StringVar(value="0")
        self.value_0_label = customtkinter.CTkLabel(self,textvariable= text_0, width=40,height=20, fg_color=ColorTheme.background_color,text_color=(ColorTheme.text_color), font=smallfont)
        self.value_0_label.place(relx=0.1, rely=0.45, anchor=tkinter.CENTER)


        text_2 = tkinter.StringVar(value="2")
        self.value_2_label = customtkinter.CTkLabel(self,textvariable= text_2, width=40,height=20, fg_color=ColorTheme.background_color,text_color=(ColorTheme.text_color), font=smallfont)
        self.value_2_label.place(relx=0.3, rely=0.45, anchor=tkinter.CENTER)

        text_4 = tkinter.StringVar(value="4")
        self.value_4_label = customtkinter.CTkLabel(self,textvariable= text_4, width=40,height=20, fg_color=ColorTheme.background_color,text_color=(ColorTheme.text_color), font=smallfont)
        self.value_4_label.place(relx=0.5, rely=0.45, anchor=tkinter.CENTER)

        text_6 = tkinter.StringVar(value="6")
        self.value_6_label = customtkinter.CTkLabel(self,textvariable= text_6, width=40,height=20, fg_color=ColorTheme.background_color,text_color=(ColorTheme.text_color), font=smallfont)
        self.value_6_label.place(relx=0.7, rely=0.45, anchor=tkinter.CENTER)

        text_8 = tkinter.StringVar(value="8")
        self.value_8_label = customtkinter.CTkLabel(self,textvariable= text_8, width=40,height=20, fg_color=ColorTheme.background_color,text_color=(ColorTheme.text_color), font=smallfont)
        self.value_8_label.place(relx=0.9, rely=0.45, anchor=tkinter.CENTER)

        image = Image.open("./images/confirm.png")
        image = customtkinter.CTkImage(image, size=image.size)
        self.confirm_button= customtkinter.CTkButton(self,fg_color=(ColorTheme.button_color),hover_color=(ColorTheme.button_color),image = image, text="",height=120,width=200,border_width=3,border_color=ColorTheme.border_color,font=font)
        self.confirm_button.place(relx=0.35,rely=0.65,anchor=tkinter.NW)

        homeimage = Image.open("./images/home.png")
        homeimage = customtkinter.CTkImage(homeimage, size=homeimage.size)
        self.home_button= customtkinter.CTkButton(self,fg_color=(ColorTheme.button_color),hover_color=(ColorTheme.button_color),image = homeimage, text="",height=120,width=200,border_width=3,border_color=ColorTheme.border_color,font=font)
        self.home_button.place(relx=0.65,rely=0.65,anchor=tkinter.NW)

        backarrow = Image.open("./images/back.png")
        backarrow = customtkinter.CTkImage(backarrow, size=backarrow.size)
        self.back_button = customtkinter.CTkButton(self,fg_color=(ColorTheme.button_color),hover_color=(ColorTheme.button_color),text = "",image=backarrow, height=120,width=200,border_width=3,border_color=ColorTheme.border_color,font=font, text_color=(ColorTheme.text_color))
        self.back_button.place(relx=0.05, rely=0.65)

        errorimage = Image.open("./images/Error_red.png")
        errorimage = customtkinter.CTkImage(errorimage, size=errorimage.size)
        self.error= customtkinter.CTkButton(self,fg_color=(ColorTheme.background_color),hover_color=(ColorTheme.background_color),text = "Active error",image=errorimage, height=10,width=10,border_width=3,font=errorfont, border_color=ColorTheme.background_color, text_color=("#e8847c"))
        



   