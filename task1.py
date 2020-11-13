#! python3
""" 
Create a num converter.
Recall that num is a system of counting based on powers of 2.
00000001 = 1
00000010 = 2
00001110 = 14
Create a converter that will convert num to dec or dec to
num using the interface shown in task1.png.  Use the shell that
has been started in task1.py
This is an incomplete program.  You will need to add onto it, 
but you should not change any of the commands that are already 
here
Use assignment_test.py to test your functions
"""
import tkinter as tk 
from tkinter import *

def num_to_dec(num):
    # num is a tuple of length 8
    # return value is an integer dec
    dec = num[0]*128+num[1]*64+num[2]*32+num[3]*16+num[4]*8+num[5]*4+num[6]*2+num[7]
    return dec

def dec_to_num(dec):
    # dec is an integer value
    # num is a tuple of length 8 that contains 1's and 0's
    num = []
    while dec >= 1:
        num.append(dec%2)
        dec = dec//2
    length = len(num)
    for i in range(0,(8-length)):
        num.append(0)
    for i in range(0,8):
        num.append(num[7-i])
    for i in range(0,8):
        num.pop(0)
    return num


def get_num():
    # function should read the entry widget and generate an integer
    # this integer will be used as an input parameter for dec to num and the result updated
    # in the 8 checkboxes
    dec = int(e1.get())
    num = dec_to_num(dec)
    num21.set(num[0])
    num22.set(num[1])
    num23.set(num[2])
    num24.set(num[3])
    num25.set(num[4])
    num26.set(num[5])
    num27.set(num[6])
    num28.set(num[7])



def get_dec():
    # function should read the checkboxes and generate a tuple called num of length 8 that has 1's and 0's
    # this tuple will be used as an input parameter for num_to_dec and the result updated
    # in the entry box
    num = []
    num.append(num21.get())
    num.append(num22.get())
    num.append(num23.get())
    num.append(num24.get())
    num.append(num25.get())
    num.append(num26.get())
    num.append(num27.get())
    num.append(num28.get())
    dec = num_to_dec(num)
    e1.delete(0,END)
    e1.insert(0,str(dec))

 


window = tk.Tk()
b1 = tk.Button(window, text="Convert to binary", command=get_num)
b2 = tk.Button(window, text="Convert to number", command=get_dec)

l1 = tk.Label(window, text="Binary to number or number to dec converter")
e1 = tk.Entry(window)

num21 = tk.IntVar()
cb1 = tk.Checkbutton(window, variable = num21)
num22 = tk.IntVar()
cb2 = tk.Checkbutton(window, variable = num22)
num23 = tk.IntVar()
cb3 = tk.Checkbutton(window, variable = num23)
num24 = tk.IntVar()
cb4 = tk.Checkbutton(window, variable = num24)
num25 = tk.IntVar()
cb5 = tk.Checkbutton(window, variable = num25)
num26 = tk.IntVar()
cb6 = tk.Checkbutton(window, variable = num26)
num27 = tk.IntVar()
cb7 = tk.Checkbutton(window, variable = num27)
num28 = tk.IntVar()
cb8 = tk.Checkbutton(window, variable = num28)

l1.grid(row = 1, column = 1, columnspan = 8)
cb1.grid(row = 2, column = 1)
cb2.grid(row = 2, column = 2)
cb3.grid(row = 2, column = 3)
cb4.grid(row = 2, column = 4)
cb5.grid(row = 2, column = 5)
cb6.grid(row = 2, column = 6)
cb7.grid(row = 2, column = 7)
cb8.grid(row = 2, column = 8)
b1.grid(row = 3, column = 1, columnspan = 4)
b2.grid(row = 3, column = 5, columnspan = 4)
e1.grid(row = 4, column = 1, columnspan = 8)

window.mainloop()