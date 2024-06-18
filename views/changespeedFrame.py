import customtkinter
from PIL import Image, ImageTk
import tkinter
from .ColorTheme import ColorTheme

class ChangespeedFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(fg_color=ColorTheme.background_color)

        
        font = customtkinter.CTkFont(family="ADLaM Display",size=35,weight="bold")
        smallfont2 = customtkinter.CTkFont(family="ADLaM Display",size=20,weight="bold")
        smallfont =customtkinter.CTkFont(family="Helvetica",size=15,weight="bold")
        errorfont = customtkinter.CTkFont(family="Helvetica",size=25,weight="bold")

        # OPENING
        opening_speed_text = tkinter.StringVar(value="Opening speed")
        self.opening_speed_label = customtkinter.CTkLabel(self, textvariable= opening_speed_text, width=160, height= 25, fg_color=ColorTheme.background_color,text_color=(ColorTheme.text_color), font=font)
        self.opening_speed_label.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

        self.opening_speed_slider = customtkinter.CTkSlider(self, from_=20, to=60, width=600, height=40, number_of_steps=4)
        self.opening_speed_slider.place(relx=0.5, rely= 0.3, anchor=tkinter.CENTER)
        

        value_20_text = tkinter.StringVar(value="200")
        self.value_20_open_label = customtkinter.CTkLabel(self,textvariable= value_20_text, width=40,height=20, fg_color=ColorTheme.background_color,text_color=(ColorTheme.text_color), font=smallfont)
        self.value_20_open_label.place(relx=0.1, rely=0.35, anchor=tkinter.CENTER)

        value_30_text = tkinter.StringVar(value="300")
        self.value_30_open_label = customtkinter.CTkLabel(self,textvariable= value_30_text, width=40,height=20, fg_color=ColorTheme.background_color,text_color=(ColorTheme.text_color), font=smallfont)
        self.value_30_open_label.place(relx=0.3, rely=0.35, anchor=tkinter.CENTER)

        value_40_text = tkinter.StringVar(value="400")
        self.value_40_open_label = customtkinter.CTkLabel(self,textvariable= value_40_text, width=40,height=20, fg_color=ColorTheme.background_color,text_color=(ColorTheme.text_color), font=smallfont)
        self.value_40_open_label.place(relx=0.5, rely=0.35, anchor=tkinter.CENTER)

        value_50_text = tkinter.StringVar(value="500")
        self.value_50_open_label = customtkinter.CTkLabel(self,textvariable= value_50_text, width=40,height=20, fg_color=ColorTheme.background_color,text_color=(ColorTheme.text_color), font=smallfont)
        self.value_50_open_label.place(relx=0.7, rely=0.35, anchor=tkinter.CENTER)

        value_60_text = tkinter.StringVar(value="600")
        self.value_60_open_label = customtkinter.CTkLabel(self,textvariable= value_60_text, width=40,height=20, fg_color=ColorTheme.background_color,text_color=(ColorTheme.text_color), font=smallfont)
        self.value_60_open_label.place(relx=0.9, rely=0.35, anchor=tkinter.CENTER) 

        unit_text = tkinter.StringVar(value="mm/s") 
        self.unit_label = customtkinter.CTkLabel(self,textvariable=unit_text, width=40, height=20,fg_color=ColorTheme.background_color,text_color=(ColorTheme.text_color), font=smallfont2)
        self.unit_label.place(relx=0.5, rely=0.38, anchor=tkinter.CENTER)
        # CLOSING
        closing_speed_text = tkinter.StringVar(value="Closing speed")
        self.closing_speed_label = customtkinter.CTkLabel(self, textvariable= closing_speed_text, width=160, height= 25, fg_color=ColorTheme.background_color,text_color=(ColorTheme.text_color), font=font)
        self.closing_speed_label.place(relx=0.5, rely=0.45, anchor=tkinter.CENTER)

        self.closing_speed_slider = customtkinter.CTkSlider(self, from_=20, to=60, width=600, height=40, number_of_steps=4)
        self.closing_speed_slider.place(relx=0.5, rely= 0.55, anchor=tkinter.CENTER)
        

        self.value_20_close_label = customtkinter.CTkLabel(self,textvariable= value_20_text, width=40,height=20, fg_color=ColorTheme.background_color,text_color=(ColorTheme.text_color), font=smallfont)
        self.value_20_close_label.place(relx=0.1, rely=0.60, anchor=tkinter.CENTER)

        self.value_30_close_label = customtkinter.CTkLabel(self,textvariable= value_30_text, width=40,height=20, fg_color=ColorTheme.background_color,text_color=(ColorTheme.text_color), font=smallfont)
        self.value_30_close_label.place(relx=0.3, rely=0.60, anchor=tkinter.CENTER)

        self.value_40_close_label = customtkinter.CTkLabel(self,textvariable= value_40_text, width=40,height=20, fg_color=ColorTheme.background_color,text_color=(ColorTheme.text_color), font=smallfont)
        self.value_40_close_label.place(relx=0.5, rely=0.60, anchor=tkinter.CENTER)

        self.value_50_close_label = customtkinter.CTkLabel(self,textvariable= value_50_text, width=40,height=20, fg_color=ColorTheme.background_color,text_color=(ColorTheme.text_color), font=smallfont)
        self.value_50_close_label.place(relx=0.7, rely=0.60, anchor=tkinter.CENTER)

        self.value_60_close_label = customtkinter.CTkLabel(self,textvariable= value_60_text, width=40,height=20, fg_color=ColorTheme.background_color,text_color=(ColorTheme.text_color), font=smallfont)
        self.value_60_close_label.place(relx=0.9, rely=0.60, anchor=tkinter.CENTER)

        self.unit2_label = customtkinter.CTkLabel(self,textvariable=unit_text, width=40, height=20,fg_color=ColorTheme.background_color,text_color=(ColorTheme.text_color), font=smallfont2)
        self.unit2_label.place(relx=0.5, rely=0.63, anchor=tkinter.CENTER )

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
        self.error= customtkinter.CTkButton(self,fg_color=(ColorTheme.background_color),hover_color=(ColorTheme.background_color),text = "Active error",image=errorimage, height=20,width=20,border_width=3,font=errorfont, border_color=ColorTheme.background_color, text_color=("#e8847c"))

   