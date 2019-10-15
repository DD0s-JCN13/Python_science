from tkinter import *
from tkinter import messagebox

main_logger = Tk()
main_logger.title("Calculator")
"""
Before update program code, please READ THE INDEX BELOW!!
If you don't understand what meaning of some value code, check here for more info.
top_number_box/number_label/number_blank are for the blank to
record the input data.

"""
top_number_box = Frame(main_logger)
number_label = Label(top_number_box,text="")
number_blank = Text(number_label)
number_blank.insert(INSERT, "Testing code")
number_blank.pack()
number_label.config(anchor=CENTER)
number_label.pack()
top_number_box.pack(side=TOP)

btn_box = Frame(main_logger)
btn_line1 = Frame(btn_box)
btn_line1.pack()
btn_line2 = Frame(btn_box)
btn_line2.pack()

main_logger.mainloop()