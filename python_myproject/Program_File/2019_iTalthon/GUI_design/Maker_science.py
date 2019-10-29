from tkinter import *

top = Tk()
top._root().title("Title here")
window_scale = Canvas(top, color=None, height="100", width="450")


def clicker():
    check1_in.set(0)
    check2_in.set(0)


lister = Menubutton(top, text="Sample", relief=SUNKEN)
lister.grid()
lister.menu = Menu(lister, tearoff=0)
lister["menu"] = lister.menu

lister_opt1 = IntVar()
lister_opt2 = IntVar()

lister.menu.add_checkbutton(label="option 1", variable = lister_opt1)
lister.menu.add_checkbutton(label="option 2", variable = lister_opt2)

lister.pack()

check1_in = IntVar()
check2_in = IntVar()

check1 = Checkbutton(top, text="Was this a test?", variable=check1_in, \
                     onvalue=1, offvalue=0, height=5, width=20)
check2 = Checkbutton(top, text="Say hello to python_myproject", variable=check2_in, \
                     onvalue=1, offvalue=0, height=5, width=20)
check1.pack()
check2.pack()
button1 = Button(top, text="Try me", command=clicker)
button1.pack(side = BOTTOM)

window_scale.pack()
top.mainloop()


