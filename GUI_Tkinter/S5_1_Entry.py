"""
Python Tkinter Entry

The Entry widget is used to provde the single line text-box to the user to accept a value from the user.
We can use the Entry widget to accept the text strings from the user.
It can only be used for one line of text from the user. For multiple lines of text, we must use the text widget.

The syntax to use the Entry widget is given below.

Syntax

w = Entry (parent, options)
A list of possible options is given below.

SN	Option	Description
1	bg	The background color of the widget.
2	bd	The border width of the widget in pixels.
3	cursor	The mouse pointer will be changed to the cursor type set to the arrow, dot, etc.
4	exportselection	The text written inside the entry box will be automatically copied to the clipboard by default. We can set the exportselection to 0 to not copy this.
5	fg	It represents the color of the text.
6	font	It represents the font type of the text.
7	highlightbackground	It represents the color to display in the traversal highlight region when the widget does not have the input focus.
8	highlightcolor	It represents the color to use for the traversal highlight rectangle that is drawn around the widget when it has the input focus.
9	highlightthickness	It represents a non-negative value indicating the width of the highlight rectangle to draw around the outside of the widget when it has the input focus.
10	insertbackground	It represents the color to use as background in the area covered by the insertion cursor. This color will normally override either the normal background for the widget.
11	insertborderwidth	It represents a non-negative value indicating the width of the 3-D border to draw around the insertion cursor. The value may have any of the forms acceptable to Tk_GetPixels.
12	insertofftime	It represents a non-negative integer value indicating the number of milliseconds the insertion cursor should remain "off" in each blink cycle. If this option is zero, then the cursor doesn't blink: it is on all the time.
13	insertontime	Specifies a non-negative integer value indicating the number of milliseconds the insertion cursor should remain "on" in each blink cycle.
14	insertwidth	It represents the value indicating the total width of the insertion cursor. The value may have any of the forms acceptable to Tk_GetPixels.
15	justify	It specifies how the text is organized if the text contains multiple lines.
16	relief	It specifies the type of the border. Its default value is FLAT.
17	selectbackground	The background color of the selected text.
18	selectborderwidth	The width of the border to display around the selected task.
19	selectforeground	The font color of the selected task.
20	show	It is used to show the entry text of some other type instead of the string. For example, the password is typed using stars (*).
21	textvariable	It is set to the instance of the StringVar to retrieve the text from the entry.
22	width	The width of the displayed text or image.
23	xscrollcommand	The entry widget can be linked to the horizontal scrollbar if we want the user to enter more text then the actual width of the widget.
"""

# !/usr/bin/python3

from tkinter import *

top = Tk()
top.geometry("400x250")

name = Label(top, text="Name").place(x=30, y=50)
email = Label(top, text="Email").place(x=30, y=90)
password = Label(top, text="Password").place(x=30, y=130)
sbmitbtn = Button(top, text="Submit", activebackground="pink", activeforeground="blue").place(x=30, y=170)

e1 = Entry(top).place(x=80, y=50)
e2 = Entry(top).place(x=80, y=90)
e3 = Entry(top).place(x=95, y=130)

top.mainloop()
