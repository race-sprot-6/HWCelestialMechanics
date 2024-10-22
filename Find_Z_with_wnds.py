import astropy.io.fits as pyfits
from astropy.wcs import WCS
import astropy
import matplotlib.pyplot as plt
import numpy as np
from astropy.io import fits
from statistics import mean
import configparser
import os
from tkinter import *
from tkinter.ttk import Combobox

def clickedOk1():
    if str(combo.get()) == "Red Shift":
        for i in range(len(ListWLineName)):
            Lin = 0
            if str(combo1.get()) == ListWLineName[i]:
                R = (float(txt.get()) - ListWLineVal[i])/ListWLineVal[i]
                labelO.config(text=f"Result: Z = {R}")
            # elif str(combo1.get()) == "Another...":
            #     txt1.grid(column=0, row=6)
                #btn2.grid(column=1, row=6)

            # else:
            #     Lin = float(combo1.get())
            #     R = (float(txt.get()) - Lin) / Lin)
            #     labelO.config(text=f"Result: Z = {R}")
            #     break
                #window.update()
    elif str(combo.get()) == "Wavelenght":
        for i in range(len(ListWLineName)):
            if ListWLineName[i] == str(combo1.get()):
                R = float(txt.get())*ListWLineVal[i] + ListWLineVal[i]
                labelO.config(text=f"Result: Lambda = {R}")
def clickedOk():
    global combo1
    if combo.get() == "Red Shift":
        label1.config(text="Specify line", state="normal")
        label.config(text="Specify the offset wavelenght")
        btn1.grid(column=4, row=4)
        txt.config(state="normal")
        txt.grid(column=3, row=4)
        combo1.config(state="normal")
        combo1.grid(column=0, row=4)
        btn1.config(state="normal")
        window.update()
    elif combo.get() == "Wavelenght":
        label1.config(text="Specify line")
        label.config(text="Specify the Red Shift")
        btn1.grid(column=4, row=4)
        txt.config(state="normal")
        txt.grid(column=3, row=4)
        btn1.config(state="normal")
        combo1.config(state="normal")
        combo1.grid(column=0, row=4)
        window.update()
    else:
        btn1.config(state="disabled")
        txt.config(state="disabled")
        label1.config(text="Specify line", state="disabled")
        combo1.config(state="disabled")
        label.config(text="Ahahah")
        window.update()

ListWLineName = ["HA", "HB", "SI", "ARIII", "OII", "SIIB", "SIIR", "NII"]
ListWLineVal = [6562.85, 4861.33, 6716.40, 7751.12, 3726.19, 6716.40, 6730.80, 6583.45]
Line = 0
window = Tk()
label = Label(text='')
label1 = Label(text='')
labelO = Label(text='')
window.title("Hier We are looking for a Red Shift or Wavelenght")
lbl = Label(window, text="What you find: Z or lambda?")
lbl.grid(column=0, row=0)
window.geometry('400x250')
combo = Combobox(window)
combo['values'] = ("...", "Red Shift", "Wavelenght")
combo.current(0)
combo.grid(column=0, row=2)
btn1 = Button(window, text="Ok", bg="white", fg="gray", command=clickedOk1)
combo1 = Combobox(window)
combo1['values'] = ("HA", "HB", "SI", "ARIII", "OII", "SIIB", "SIIR", "NII")
combo1.current(0)
txt = Entry(window,width=10)
btn = Button(window, text="Ok", bg="white", fg="gray", command=clickedOk)
btn.grid(column=1, row=2)
txt1 = Entry(window, width=10)

label.grid(column=3, row=3)
label1.grid(column=0, row=3)
labelO.grid(column=0, row=10)
window.mainloop()
