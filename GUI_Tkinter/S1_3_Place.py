"""
Python Tkinter place() method
The place() geometry manager organizes the widgets to the specific x and y coordinates.

Syntax
widget.place(options)
A list of possible options is given below.

Anchor: It represents the exact position of the widget within the container. The default value (direction) is NW
 (the upper left corner)
bordermode: The default value of the border type is INSIDE that refers to ignore the parent's inside the border.
 The other option is OUTSIDE.
height, width: It refers to the height and width in pixels.
relheight, relwidth: It is represented as the float between 0.0 and 1.0 indicating the fraction of the parent's
 height and width.
relx, rely: It is represented as the float between 0.0 and 1.0 that is the offset in the horizontal and vertical
 direction.
x, y: It refers to the horizontal and vertical offset in the pixels.
"""

# !/usr/bin/python3
from tkinter import *

top = Tk()
top.geometry("400x250")

name = Label(top, text="Name").place(x=30, y=50)
email = Label(top, text="Email").place(x=30, y=90)
password = Label(top, text="Password").place(x=30, y=130)

e1 = Entry(top).place(x=80, y=50)
e2 = Entry(top).place(x=80, y=90)
e3 = Entry(top).place(x=95, y=130)

top.mainloop()