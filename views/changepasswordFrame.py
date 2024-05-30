import customtkinter
from PIL import Image, ImageTk
import tkinter
from .ColorTheme import ColorTheme

class ChangepasswordFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(fg_color=ColorTheme.background_color)

        
        font = customtkinter.CTkFont(family="Helvetica",size=45,weight="bold")
        height = 130
        width  = 200
        labelfont = customtkinter.CTkFont(family="Helvetica",size=35,weight="bold")
        self.label1 = customtkinter.CTkLabel(self, text="Enter new password",font=labelfont,text_color=(ColorTheme.text_color) ,height=50, width=200)
        self.label1.place(relx = 0.5, rely=0.05,anchor=tkinter.CENTER)

        self.digit11 = customtkinter.CTkButton(self,fg_color="#d0d2d6",hover_color="#d0d2d6",text = " ", height=90,width=90,border_width=3,border_color=ColorTheme.border_color,font=font, text_color="black")
        self.digit11.place(relx=0.15,rely=0.1,anchor=tkinter.NW)
        
        self.digit22 = customtkinter.CTkButton(self,fg_color="#d0d2d6",hover_color="#d0d2d6",text = " ", height=90,width=90,border_width=3,border_color=ColorTheme.border_color,font=font, text_color="black")
        self.digit22.place(relx=0.29,rely=0.1,anchor=tkinter.NW)

        self.digit33 = customtkinter.CTkButton(self,fg_color="#d0d2d6",hover_color="#d0d2d6",text = " ", height=90,width=90,border_width=3,border_color=ColorTheme.border_color,font=font, text_color="black")
        self.digit33.place(relx=0.43,rely=0.1,anchor=tkinter.NW)

        self.digit44 = customtkinter.CTkButton(self,fg_color="#d0d2d6",hover_color="#d0d2d6",text = " ", height=90,width=90,border_width=3,border_color=ColorTheme.border_color,font=font, text_color="black")
        self.digit44.place(relx=0.57,rely=0.1,anchor=tkinter.NW)

        leftarrow = Image.open("./images/ArrowLeft.png")
        ctkimage = customtkinter.CTkImage(leftarrow, size=leftarrow.size)
        self.undobutton1 = customtkinter.CTkButton(self,fg_color=(ColorTheme.button_color),hover_color=(ColorTheme.button_color),text = "",image = ctkimage, height=90,width=90,border_width=3,border_color=ColorTheme.border_color,font=font,text_color=(ColorTheme.text_color))
        self.undobutton1.place(relx=0.71,rely=0.1,anchor=tkinter.NW)

        self.button11 = customtkinter.CTkButton(self,fg_color=(ColorTheme.button_color),hover_color=(ColorTheme.button_color),text = "1", height=height,width=width,border_width=3,border_color=ColorTheme.border_color,font=font, text_color=(ColorTheme.text_color))
        self.button11.place(relx=0.04166,rely=0.24,anchor=tkinter.NW)

        self.button22 = customtkinter.CTkButton(self,fg_color=(ColorTheme.button_color),hover_color=(ColorTheme.button_color),text = "2", height=height,width=width,border_width=3,border_color=ColorTheme.border_color,font=font, text_color=(ColorTheme.text_color))
        self.button22.place(relx=0.36111,rely=0.24,anchor=tkinter.NW)

        self.button33 = customtkinter.CTkButton(self,fg_color=(ColorTheme.button_color),hover_color=(ColorTheme.button_color),text = "3", height=height,width=width,border_width=3,border_color=ColorTheme.border_color,font=font, text_color=(ColorTheme.text_color))
        self.button33.place(relx=0.68055,rely=0.24,anchor=tkinter.NW)

        self.button44 = customtkinter.CTkButton(self,fg_color=(ColorTheme.button_color),hover_color=(ColorTheme.button_color),text = "4", height=height,width=width,border_width=3,border_color=ColorTheme.border_color,font=font, text_color=(ColorTheme.text_color))
        self.button44.place(relx=0.04166,rely=0.43,anchor=tkinter.NW)

        self.button55 = customtkinter.CTkButton(self,fg_color=(ColorTheme.button_color),hover_color=(ColorTheme.button_color),text = "5", height=height,width=width,border_width=3,border_color=ColorTheme.border_color,font=font, text_color=(ColorTheme.text_color))
        self.button55.place(relx=0.36111,rely=0.43,anchor=tkinter.NW)

        self.button66 = customtkinter.CTkButton(self,fg_color=(ColorTheme.button_color),hover_color=(ColorTheme.button_color),text = "6", height=height,width=width,border_width=3,border_color=ColorTheme.border_color,font=font, text_color=(ColorTheme.text_color))
        self.button66.place(relx=0.68055,rely=0.43,anchor=tkinter.NW)

        self.button77 = customtkinter.CTkButton(self,fg_color=(ColorTheme.button_color),hover_color=(ColorTheme.button_color),text = "7", height=height,width=width,border_width=3,border_color=ColorTheme.border_color,font=font, text_color=(ColorTheme.text_color))
        self.button77.place(relx=0.04166,rely=0.62,anchor=tkinter.NW)

        self.button88 = customtkinter.CTkButton(self,fg_color=(ColorTheme.button_color),hover_color=(ColorTheme.button_color),text = "8", height=height,width=width,border_width=3,border_color=ColorTheme.border_color,font=font, text_color=(ColorTheme.text_color))
        self.button88.place(relx=0.36111,rely=0.62,anchor=tkinter.NW)

        self.button99 = customtkinter.CTkButton(self,fg_color=(ColorTheme.button_color),hover_color=(ColorTheme.button_color),text = "9", height=height,width=width,border_width=3,border_color=ColorTheme.border_color,font=font, text_color=(ColorTheme.text_color))
        self.button99.place(relx=0.68055,rely=0.62,anchor=tkinter.NW)

        self.button00 = customtkinter.CTkButton(self,fg_color=(ColorTheme.button_color),hover_color=(ColorTheme.button_color),text = "0", height=height,width=width,border_width=3,border_color=ColorTheme.border_color,font=font, text_color=(ColorTheme.text_color))
        self.button00.place(relx=0.36111,rely=0.81,anchor=tkinter.NW)

        homeimage = Image.open("./images/home.png")
        homeimage = customtkinter.CTkImage(homeimage, size=homeimage.size)
        self.home_button = customtkinter.CTkButton(self,fg_color=(ColorTheme.button_color),hover_color=(ColorTheme.button_color),text = "", image=homeimage, height=height,width=width,border_width=3,border_color=ColorTheme.border_color,font=font, text_color=(ColorTheme.text_color))
        self.home_button.place(relx=0.68055,rely=0.81,anchor=tkinter.NW)

        backarrow = Image.open("./images/back.png")
        backarrow = customtkinter.CTkImage(backarrow, size=backarrow.size)
        self.back_button = customtkinter.CTkButton(self,fg_color=(ColorTheme.button_color),hover_color=(ColorTheme.button_color),text = "",image=backarrow, height=height,width=width,border_width=3,border_color=ColorTheme.border_color,font=font, text_color=(ColorTheme.text_color))
        self.back_button.place(relx=0.04166,rely=0.81,anchor=tkinter.NW)

           


    