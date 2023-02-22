from time import *
from tkinter import *


def update():
    time_string = strftime("%H:%M:%S")
    time_label.config(text=time_string)

    day_string = strftime("%d/%m/%Y - Today is %A")
    day_label.config(text=day_string)
    time_label.after(1000, update)


root = Tk()

day_label = Label(root, text="")
day_label.pack()

time_label = Label(root, text="")
time_label.pack()

update()

root.mainloop()
