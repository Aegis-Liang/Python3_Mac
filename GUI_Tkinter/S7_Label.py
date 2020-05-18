"""
Python Tkinter Label

The Label is used to specify the container box where we can place the text or images.
This widget is used to provide the message to the user about other widgets used in the python application.

There are the various options which can be specified to configure the text or the part of the text shown in the Label.

The syntax to use the Label is given below.

Syntax

w = Label (master, options)
A list of possible options is given below.

SN	Option	Description
1	anchor	It specifies the exact position of the text within the size provided to the widget.
The default value is CENTER, which is used to center the text within the specified space.
2	bg	The background color displayed behind the widget.
3	bitmap	It is used to set the bitmap to the graphical object specified so that,
the label can represent the graphics instead of text.
4	bd	It represents the width of the border. The default is 2 pixels.
5	cursor	The mouse pointer will be changed to the type of the cursor specified, i.e., arrow, dot, etc.
6	font	The font type of the text written inside the widget.
7	fg	The foreground color of the text written inside the widget.
8	height	The height of the widget.
9	image	The image that is to be shown as the label.
10	justify	It is used to represent the orientation of the text if the text contains multiple lines.
It can be set to LEFT for left justification, RIGHT for right justification, and CENTER for center justification.
11	padx	The horizontal padding of the text. The default value is 1.
12	pady	The vertical padding of the text. The default value is 1.
13	relief	The type of the border. The default value is FLAT.
14	text	This is set to the string variable which may contain one or more line of text.
15	textvariable	The text written inside the widget is set to the control variable StringVar
so that it can be accessed and changed accordingly.
16	underline	We can display a line under the specified letter of the text.
Set this option to the number of the letter under which the line will be displayed.
17	width	The width of the widget. It is specified as the number of characters.
18	wraplength	Instead of having only one line as the label text,
we can break it to the number of lines where each line has the number of characters specified to this option.
"""

# !/usr/bin/python3

from tkinter import *

top = Tk()
top.geometry("400x250")

# creating label
uname = Label(top, text="Username").place(x=30, y=50)

# creating label
password = Label(top, text="Password").place(x=30, y=90)
sbmitbtn = Button(top, text="Submit", activebackground="pink", activeforeground="blue").place(x=30, y=120)

e1 = Entry(top, width=20).place(x=100, y=50)
e2 = Entry(top, width=20).place(x=100, y=90)

top.mainloop()
