from tkinter import *
from math import *
from sympy import *

yolo = Tk()
yolo.configure(background="#0FB6A3")

button = Button(yolo,relief=FLAT, borderwidth=0.8,bg="#0FB6CF" ,text="Calculate the Area", command= lambda : get_area(float(entry1.get()), float(entry2.get()), float(entry3.get())))
button.grid(row=4, column=0, columnspan=2)

def get_area(x,y,z):
    s = (x + y + z)/2
    area = sqrt(s*(s-x)*(s-y)*(s-z))
    areatext = Label(text=(area), bg="#0FB6A3")
    areatext.grid(column=0, row=3)
    print(area)

entry1 = Entry()
entry2 = Entry()
entry3 = Entry()

label1 = Label(text="A", bg="#0FB6A3")
label2 = Label(text="B", bg="#0FB6A3")
label3 = Label(text="C", bg="#0FB6A3")

label1.grid(column=0, row=0)
label2.grid(column=0, row=1)
label3.grid(column=0, row=2)
entry1.grid(column=1, row=0)
entry2.grid(column=1, row=1)
entry3.grid(column=1, row=2)

yolo.mainloop()