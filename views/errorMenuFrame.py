
import customtkinter
from PIL import Image, ImageTk
import tkinter
from .ColorTheme import ColorTheme

class ErrorMenuFrame(customtkinter.CTkFrame):
    
    def __init__(self, master):
        super().__init__(master)
        
        self.configure(fg_color=ColorTheme.background_color)
        
        font = customtkinter.CTkFont(family="Helvetica",size=45,weight="bold")
        self.scrollableFrame = ScrollableFrame(self)
        self.scrollableFrame.grid(row=0, column=0, padx = 10)

        image = Image.open("./images/home.png")
        image = customtkinter.CTkImage(image, size=image.size)
        self.home_button= customtkinter.CTkButton(self,fg_color=(ColorTheme.button_color),hover_color=(ColorTheme.button_color),image = image, text="",height=142,width=200,border_width=3,border_color=ColorTheme.border_color,font=font)
        self.home_button.place(relx=0.65,y=568)

        self.reset_button = customtkinter.CTkButton(self,fg_color=(ColorTheme.button_color),hover_color=(ColorTheme.button_color),text = "Reset", height=142,width=200,border_width=3,border_color=ColorTheme.border_color,font=font, text_color=(ColorTheme.text_color))
        self.reset_button.place(relx = 0.35, y=568)
         
        backarrow = Image.open("./images/back.png")
        backarrow = customtkinter.CTkImage(backarrow, size=backarrow.size)
        self.back_button = customtkinter.CTkButton(self,fg_color=(ColorTheme.button_color),hover_color=(ColorTheme.button_color),text = "",image=backarrow, height=142,width=200,border_width=3,border_color=ColorTheme.border_color,font=font, text_color=(ColorTheme.text_color))
        self.back_button.place(relx=0.05, y=568)


class ScrollableFrame(customtkinter.CTkScrollableFrame):
    errorMessages = []
    def __init__(self, master):
        super().__init__(master)
        self.configure(fg_color=ColorTheme.background_color)
        self.configure(width=680, height = 558)
        

class ErrorMessageFrame(customtkinter.CTkFrame):
    expanded = False
    def __init__(self,errorNr, errorName, errorDescription,errorSolution,master):
        font = customtkinter.CTkFont(family="Helvetica",size=25,weight="bold")
        super().__init__(master)
        self.configure(fg_color=ColorTheme.button_color)
        self.configure(width=660, height = 100)
        self.label = customtkinter.CTkLabel(self, text= errorNr, text_color=ColorTheme.text_color, font=font)
        self.label.place(x = 5, y = 5)
        self.title = customtkinter.CTkLabel(self, text= errorName, text_color=ColorTheme.text_color, font=font)
        self.title.place(x= 5, y =30)
        arrowLeft = Image.open("./images/ArrowLeft.png")
        arrowLeft = customtkinter.CTkImage(arrowLeft, size=arrowLeft.size)
        self.expand_button = customtkinter.CTkButton(self,fg_color=(ColorTheme.button_color),hover_color=(ColorTheme.button_color),text = "", image=arrowLeft, height=70,width=70,border_width=3,border_color=ColorTheme.text_color,font=font, text_color=(ColorTheme.text_color))
        self.expand_button.place(x=550, y=15)
       
        smallfont = customtkinter.CTkFont(family="Helvetica",size=18,weight="bold")
        self.description = customtkinter.CTkLabel(self, justify= "left", text=errorDescription, text_color=ColorTheme.text_color, font=smallfont)
        self.solution = customtkinter.CTkLabel(self, justify= "left", text=errorSolution, text_color=ColorTheme.text_color, font=smallfont)
        

    



   