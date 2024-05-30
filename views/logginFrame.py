import customtkinter
from PIL import Image, ImageTk
import tkinter
from .ColorTheme import ColorTheme

class LogginFrame(customtkinter.CTkFrame):
    
    def __init__(self, master):
        super().__init__(master)
        self.configure(fg_color=ColorTheme.background_color)
        
        font = customtkinter.CTkFont(family="Helvetica",size=45,weight="bold")
        height= 130
        width = 200

        labelfont = customtkinter.CTkFont(family="Helvetica",size=35,weight="bold")
        self.label = customtkinter.CTkLabel(self, text="Authentication Required",font=labelfont,text_color=(ColorTheme.text_color) ,height=50, width=200)
        self.label.place(relx = 0.5, rely=0.05,anchor=tkinter.CENTER)
        

        self.digit1 = customtkinter.CTkButton(self,fg_color="#d0d2d6",hover_color="#d0d2d6",text = " ", height=90,width=90,border_width=3,border_color=ColorTheme.border_color,font=font, text_color="black")
        self.digit1.place(relx=0.15,rely=0.1,anchor=tkinter.NW)
        
        self.digit2 = customtkinter.CTkButton(self,fg_color="#d0d2d6",hover_color="#d0d2d6",text = " ", height=90,width=90,border_width=3,border_color=ColorTheme.border_color,font=font, text_color="black")
        self.digit2.place(relx=0.29,rely=0.1,anchor=tkinter.NW)

        self.digit3 = customtkinter.CTkButton(self,fg_color="#d0d2d6",hover_color="#d0d2d6",text = " ", height=90,width=90,border_width=3,border_color=ColorTheme.border_color,font=font, text_color="black")
        self.digit3.place(relx=0.43,rely=0.1,anchor=tkinter.NW)

        self.digit4 = customtkinter.CTkButton(self,fg_color="#d0d2d6",hover_color="#d0d2d6",text = " ", height=90,width=90,border_width=3,border_color=ColorTheme.border_color,font=font, text_color="black")
        self.digit4.place(relx=0.57,rely=0.1,anchor=tkinter.NW)

        backarrow = Image.open("./images/ArrowLeft.png")
        backarrow = customtkinter.CTkImage(backarrow, size=backarrow.size)
        self.undobutton = customtkinter.CTkButton(self,fg_color=(ColorTheme.button_color),hover_color=(ColorTheme.button_color),text = "",image = backarrow, height=90,width=90,border_width=3,border_color=ColorTheme.border_color,font=font,text_color=(ColorTheme.text_color))
        self.undobutton.place(relx=0.71,rely=0.1,anchor=tkinter.NW)
        
        self.button1 = customtkinter.CTkButton(self,fg_color=(ColorTheme.button_color),hover_color=(ColorTheme.button_color),text = "1", height=height,width=width,border_width=3,border_color=ColorTheme.border_color,font=font, text_color=(ColorTheme.text_color))
        self.button1.place(relx=0.04166,rely=0.24,anchor=tkinter.NW)

        self.button2 = customtkinter.CTkButton(self,fg_color=(ColorTheme.button_color),hover_color=(ColorTheme.button_color),text = "2", height=height,width=width,border_width=3,border_color=ColorTheme.border_color,font=font, text_color=(ColorTheme.text_color))
        self.button2.place(relx=0.36111,rely=0.24,anchor=tkinter.NW)

        self.button3 = customtkinter.CTkButton(self,fg_color=(ColorTheme.button_color),hover_color=(ColorTheme.button_color),text = "3", height=height,width=width,border_width=3,border_color=ColorTheme.border_color,font=font, text_color=(ColorTheme.text_color))
        self.button3.place(relx=0.68055,rely=0.24,anchor=tkinter.NW)

        self.button4 = customtkinter.CTkButton(self,fg_color=(ColorTheme.button_color),hover_color=(ColorTheme.button_color),text = "4", height=height,width=width,border_width=3,border_color=ColorTheme.border_color,font=font, text_color=(ColorTheme.text_color))
        self.button4.place(relx=0.04166,rely=0.43,anchor=tkinter.NW)

        self.button5 = customtkinter.CTkButton(self,fg_color=(ColorTheme.button_color),hover_color=(ColorTheme.button_color),text = "5", height=height,width=width,border_width=3,border_color=ColorTheme.border_color,font=font, text_color=(ColorTheme.text_color))
        self.button5.place(relx=0.36111,rely=0.43,anchor=tkinter.NW)

        self.button6 = customtkinter.CTkButton(self,fg_color=(ColorTheme.button_color),hover_color=(ColorTheme.button_color),text = "6", height=height,width=width,border_width=3,border_color=ColorTheme.border_color,font=font, text_color=(ColorTheme.text_color))
        self.button6.place(relx=0.68055,rely=0.43,anchor=tkinter.NW)

        self.button7 = customtkinter.CTkButton(self,fg_color=(ColorTheme.button_color),hover_color=(ColorTheme.button_color),text = "7", height=height,width=width,border_width=3,border_color=ColorTheme.border_color,font=font, text_color=(ColorTheme.text_color))
        self.button7.place(relx=0.04166,rely=0.62,anchor=tkinter.NW)

        self.button8 = customtkinter.CTkButton(self,fg_color=(ColorTheme.button_color),hover_color=(ColorTheme.button_color),text = "8", height=height,width=width,border_width=3,border_color=ColorTheme.border_color,font=font, text_color=(ColorTheme.text_color))
        self.button8.place(relx=0.36111,rely=0.62,anchor=tkinter.NW)

        self.button9 = customtkinter.CTkButton(self,fg_color=(ColorTheme.button_color),hover_color=(ColorTheme.button_color),text = "9", height=height,width=width,border_width=3,border_color=ColorTheme.border_color,font=font, text_color=(ColorTheme.text_color))
        self.button9.place(relx=0.68055,rely=0.62,anchor=tkinter.NW)

        self.button0 = customtkinter.CTkButton(self,fg_color=(ColorTheme.button_color),hover_color=(ColorTheme.button_color),text = "0", height=height,width=width,border_width=3,border_color=ColorTheme.border_color,font=font, text_color=(ColorTheme.text_color))
        self.button0.place(relx=0.36111,rely=0.81,anchor=tkinter.NW)

        homeimage = Image.open("./images/home.png")
        homeimage = customtkinter.CTkImage(homeimage, size=homeimage.size)
        self.homebutton = customtkinter.CTkButton(self,fg_color=(ColorTheme.button_color),hover_color=(ColorTheme.button_color),text = "", image=homeimage,height=height,width=width,border_width=3,border_color=ColorTheme.border_color,font=font, text_color=(ColorTheme.text_color))
        self.homebutton.place(relx=0.68055,rely=0.81,anchor=tkinter.NW)

        backarrow = Image.open("./images/back.png")
        backarrow = customtkinter.CTkImage(backarrow, size=backarrow.size)
        self.back_button = customtkinter.CTkButton(self,fg_color=(ColorTheme.button_color),hover_color=(ColorTheme.button_color),text = "",image=backarrow, height=height,width=width,border_width=3,border_color=ColorTheme.border_color,font=font, text_color=(ColorTheme.text_color))
        self.back_button.place(relx=0.04166,rely=0.81,anchor=tkinter.NW)

       

        
        
        




   