from time import strftime

from tkinter import *

root = Tk()
root.title("digital")



def time():
    string = strftime("%H:%M:%S %p")
    lbl.config(text = string)
    lbl.after(1000, time)

lbl = Label(root, font= ("arial", 160, "bold"), bg="black",fg="white")
lbl.pack(anchor="center" ,fill="both",expand=1)


time()
mainloop()