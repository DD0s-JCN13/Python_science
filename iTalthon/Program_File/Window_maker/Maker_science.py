from tkinter import *
top = Tk()
top._root().title("Title here")
text1 = Text(top)
text1.insert(INSERT, "Text here.")
text1.insert(END, "Put text here.")
text1.pack()

top.mainloop()


