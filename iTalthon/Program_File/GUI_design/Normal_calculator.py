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
number_label = Label(top_number_box, text="")
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
btn_line3 = Frame(btn_box)
btn_line3.pack()
btn_line4 = Frame(btn_box)
btn_line4.pack()
btn_box.pack()

#for line 1
num_btn_1 = Button(btn_line1, text="  1  ", command=None)
num_btn_1.pack(side=LEFT)
num_btn_2 = Button(btn_line1, text="  2  ", command=None)
num_btn_2.pack(side=LEFT)
num_btn_3 = Button(btn_line1, text="  3  ", command=None)
num_btn_3.pack(side=LEFT)
cal_btn_plu = Button(btn_line1, text="  +  ", command=None)
cal_btn_plu.pack(side=LEFT)

#for line 2
num_btn_4 = Button(btn_line2, text="  4  ", command=None)
num_btn_4.pack(side=LEFT)
num_btn_5 = Button(btn_line2, text="  5  ", command=None)
num_btn_5.pack(side=LEFT)
num_btn_6 = Button(btn_line2, text="  6  ", command=None)
num_btn_6.pack(side=LEFT)
cal_btn_minus = Button(btn_line2, text="   -  ", command=None)
cal_btn_minus.pack(side=LEFT)

#for line 3
num_btn_7 = Button(btn_line3, text="  7  ", command=None)
num_btn_7.pack(side=LEFT)
num_btn_8 = Button(btn_line3, text="  8  ", command=None)
num_btn_8.pack(side=LEFT)
num_btn_9 = Button(btn_line3, text="  9  ", command=None)
num_btn_9.pack(side=LEFT)
cal_btn_times = Button(btn_line3, text="  *   ", command=None)
cal_btn_times.pack(side=LEFT)

#for line 4
cal_btn_doter = Button(btn_line4, text="   .  ", command=None)
cal_btn_doter.pack(side=LEFT)
num_btn_0 = Button(btn_line4, text="  0  ", command=None)
num_btn_0.pack(side=LEFT)
cal_btn_equ = Button(btn_line4, text="  =   ", command=None)
cal_btn_equ.pack(side=LEFT)
cal_btn_dvs = Button(btn_line4, text="  /  ", command=None)
cal_btn_dvs.pack(side=LEFT)

main_logger.mainloop()
