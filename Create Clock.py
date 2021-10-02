from tkinter import *
from tkinter import ttk
root = Tk()
import time
root.title("Create Clock")
root.geometry("400x400")
root.iconbitmap("image/2.ico")
root.resizable(width= True, height=False)

def clock(): # 1st choice (do by myself)
    #hour=time.strftime("%H :%M :%S") # 1st choice (do by myself)
    hour = time.strftime("%H") # this line is follow tutorial
    minute = time.strftime("%M") # this line is follow tutorial
    second = time.strftime("%S") # this line is follow tutorial
    AmPm = time.strftime ("%p")
    # mylabel.config(text=hour) # 1st choice (do by myself)
    mylabel.config(text= hour + ":" + minute + ":" + second + AmPm) # this line is follow tutorial
    mylabel.after(1000,clock)
mylabel= Label(root, text="Test", font=("Khmer OS",40), fg= "green", bg="Silver")
mylabel.pack(pady=20)
clock()


## self-practies

root.mainloop()