from tkinter import *
from tkinter import messagebox

main_win = Tk()
main_win.title("EZ Calculator")

# Definitions for functions below


class Returner:
    result = 0


def alerter_empty():
    messagebox.showwarning("Warning", "It can't be empty value for blanks!")


def alerter_format():
    messagebox.showwarning("Warning", "Wrong format, please check your input!")


def the_plus():
    if ent_front.get() is "" or ent_back.get() is "":
        alerter_empty()
    else:
        fronter = ent_front.get()
        backer = ent_back.get()
        if fronter.isdigit() is False or backer.isdigit() is False:
            alerter_format()
        else:
            Returner.result = float(fronter) + float(backer)


def the_minus():
    if ent_front.get() is "" or ent_back.get() is "":
        alerter_empty()
    else:
        fronter = ent_front.get()
        backer = ent_back.get()
        if fronter.isdigit() is False or backer.isdigit() is False:
            alerter_format()
        else:
            Returner.result = float(fronter) - float(backer)


def the_multi():
    if ent_front.get() is "" or ent_back.get() is "":
        alerter_empty()
    else:
        fronter = ent_front.get()
        backer = ent_back.get()
        if fronter.isdigit() is False or backer.isdigit() is False:
            alerter_format()
        else:
            Returner.result = float(fronter) * float(backer)


def the_divis():
    if ent_front.get() is "" or ent_back.get() is "":
        alerter_empty()
    else:
        fronter = ent_front.get()
        backer = ent_back.get()
        if fronter.isdigit() is False or backer.isdigit() is False:
            alerter_format()
        elif str(ent_back.get()) is "0":
            messagebox.showwarning("Warning", "The result is not exist!")
        else:
            Returner.result = float(fronter) / float(backer)


def resulting():
    messagebox.showinfo("Result", "The result is " + str(Returner.result))


def cleaning():
    ent_front.delete(first=0, last=len(ent_front.get()))
    ent_back.delete(first=0, last=len(ent_back.get()))
    Returner.result = 0

#End of function coding


top_frame = Frame(main_win)
top_frame.pack(side=TOP)

t_lft_frame = Frame(top_frame)
t_lft_frame.pack(side=LEFT)

t_rht_frame = Frame(top_frame)
t_rht_frame.pack(side=RIGHT)

btm_frame = Frame(main_win)
btm_frame.pack(side=BOTTOM)

b_top_frame = Frame(btm_frame)
b_top_frame.pack(side=TOP)

#Programs for top frame below

pane1 = PanedWindow(t_lft_frame, orient=VERTICAL)
pane1.pack(fill=X, expand=1)

pane2 = PanedWindow(t_lft_frame, orient=VERTICAL)
pane2.pack(fill=X, expand=1)

mainer = Label(pane1, text="Front number", width=15)
pane1.add(mainer)

sub_mainer = Label(pane2, text="Back number", width=15)
pane2.add(sub_mainer)

ent_front = Entry(t_rht_frame, bd=4)
ent_front.pack()

ent_back = Entry(t_rht_frame, bd=4)
ent_back.pack()

#End coding for top frame
#Programs for bottom frame below

btn_plus = Button(b_top_frame, text="  +  ", command=the_plus)
btn_plus.pack(side=LEFT)

btn_minus = Button(b_top_frame, text="  -  ", command=the_minus)
btn_minus.pack(side=LEFT)

btn_multi = Button(b_top_frame, text="  *  ", command=the_multi)
btn_multi.pack(side=LEFT)

btn_divis = Button(b_top_frame, text="  /  ", command=the_divis)
btn_divis.pack(side=LEFT)

btn_clean = Button(btm_frame, text="Clean", command=cleaning)
btn_clean.pack(side=LEFT)

btn_getter = Button(btm_frame, text="Result", command=resulting)
btn_getter.pack(side=LEFT)

btn_exit = Button(btm_frame, text="Close app", command=main_win.destroy)
btn_exit.pack(side=RIGHT)
#End coding for bottom frame

main_win.mainloop()

