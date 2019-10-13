from tkinter import *
from tkinter import messagebox
top = Tk()
top.title("Main sample")


def pop_up():
    messagebox.showinfo("Pop up", "Hello, "+ent1.get())


lbl1 = Label(top, text="Enter your name:")
lbl1.pack(side=LEFT)
ent1 = Entry(top, bd=5)
ent1.pack(side=LEFT)

button_pop = Button(top, text="Try me plz", command=pop_up)
button_pop.pack(side=RIGHT)
top.mainloop()
