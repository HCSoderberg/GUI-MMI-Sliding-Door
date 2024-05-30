import signal 
import time
from tkinter import* 

class TimeCounter():
    global done
    done = False

    def alarm_handler( signum, frame): 
        done = True
        signal.alarm(0)
    
    signal.signal(signal.SIGALRM, alarm_handler)

    def increaseAlarm(self):
        signal.alarm(100)

    def clicked(self):
        signal.alarm(10)
        
    if __name__ == "__main__":
        signal.alarm(5)
        root = Tk()
        btn = Button(root, text = "Click me" ,
            fg = "red", command=clicked)
        btn.grid(column=1, row=0)
        while not done: 
            root.mainloop()
        

