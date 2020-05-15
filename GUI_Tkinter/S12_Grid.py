"""
Python Tkinter grid() method

The grid() geometry manager organizes the widgets in the tabular form. We can specify the rows and columns as the
options in the method call. We can also specify the column span (width) or rowspan(height) of a widget.
This is a more organized way to place the widgets to the python application. The syntax to use the grid()
is given below.

Syntax
widget.grid(options)
A list of possible options that can be passed inside the grid() method is given below.

Column
The column number in which the widget is to be placed. The leftmost column is represented by 0.
Columnspan
The width of the widget. It represents the number of columns up to which, the column is expanded.
ipadx, ipady
It represents the number of pixels to pad the widget inside the widget's border.
padx, pady
It represents the number of pixels to pad the widget outside the widget's border.
row
The row number in which the widget is to be placed. The topmost row is represented by 0.
rowspan
The height of the widget, i.e. the number of the row up to which the widget is expanded.
Sticky
If the cell is larger than a widget, then sticky is used to specify the position of the widget inside the cell.
It may be the concatenation of the sticky letters representing the position of the widget.
It may be N, E, W, S, NE, NW, NS, EW, ES.
"""


# !/usr/bin/python3
from tkinter import *

parent = Tk()

name = Label(parent, text="Name").grid(row=0, column=0)
e1 = Entry(parent).grid(row=0, column=1)

password = Label(parent, text="Password").grid(row=1, column=0)
e2 = Entry(parent).grid(row=1, column=1)

submit = Button(parent, text="Submit").grid(row=4, column=0)

parent.mainloop()
