"""
Python Tkinter Frame

Python Tkinter Frame widget is used to organize the group of widgets.
It acts like a container which can be used to hold the other widgets.
The rectangular areas of the screen are used to organize the widgets to the python application.

The syntax to use the Frame widget is given below.

Syntax

w = Frame(parent,  options)
A list of possible options is given below.

SN	Option	Description
1	bd	It represents the border width.
2	bg	The background color of the widget.
3	cursor	The mouse pointer is changed to the cursor type set to different values like an arrow, dot, etc.
4	height	The height of the frame.
5	highlightbackground	The color of the background color when it is under focus.
6	highlightcolor	The text color when the widget is under focus.
7	highlightthickness	It specifies the thickness around the border when the widget is under the focus.
8	relief	It specifies the type of the border. The default value if FLAT.
9	width	It represents the width of the widget.
"""

from tkinter import *

top = Tk()
top.geometry("140x100")
frame = Frame(top)
frame.pack()

leftframe = Frame(top)
leftframe.pack(side=LEFT)

rightframe = Frame(top)
rightframe.pack(side=RIGHT)

btn1 = Button(frame, text="Submit", fg="red", activebackground="red")
btn1.pack(side=LEFT)

btn2 = Button(frame, text="Remove", fg="brown", activebackground="brown")
btn2.pack(side=RIGHT)

btn3 = Button(rightframe, text="Add", fg="blue", activebackground="blue")
btn3.pack(side=LEFT)

btn4 = Button(leftframe, text="Modify", fg="black", activebackground="white")
btn4.pack(side=RIGHT)

top.mainloop()
