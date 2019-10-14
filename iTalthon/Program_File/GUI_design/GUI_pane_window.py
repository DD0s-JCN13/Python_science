from tkinter import *
main_win = Tk();
main_win.title("Sample")

pane1 = PanedWindow()
pane1.pack(fill=BOTH, expand=1)

mainer = Label(pane1, text="Main pane")
pane1.add(mainer)

pane2 = PanedWindow(pane1, orient=VERTICAL)
pane1.add(pane2)

pane2_label = Label(pane2, text="Sub pane(for pane2)")
pane2.add(pane2_label)

pane3 = PanedWindow(pane2)
pane2.add(pane3)

pane3_label = Label(pane3, text="Sub pane(for pane3)")
pane3.add(pane3_label)


main_win.mainloop()

