"""
Python Tkinter pack() method

The pack() widget is used to organize widget in the block. The positions widgets added to the python application using
the pack() method can be controlled by using the various options specified in the method call.
However, the controls are less and widgets are generally added in the less organized manner.

The syntax to use the pack() is given below.
syntax
widget.pack(options)

A list of possible options that can be passed in pack() is given below.

expand: If the expand is set to true, the widget expands to fill any space.
Fill: By default, the fill is set to NONE. However, we can set it to X or Y to determine whether the widget contains
any extra space.
size: it represents the side of the parent to which the widget is to be placed on the window.
"""

# !/usr/bin/python3
from tkinter import *

parent = Tk()

redbutton = Button(parent, text="Red", fg="red")
redbutton.pack(side=LEFT)

greenbutton = Button(parent, text="Black", fg="black")
greenbutton.pack(side=RIGHT)

bluebutton = Button(parent, text="Blue", fg="blue")
bluebutton.pack(side=TOP)

blackbutton = Button(parent, text="Green", fg="red")
blackbutton.pack(side=BOTTOM)
parent.mainloop()
