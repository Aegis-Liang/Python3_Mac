"""
Python Tkinter Scrollbar

The scrollbar widget is used to scroll down the content of the other widgets like listbox, text, and canvas. However, we can also create the horizontal scrollbars to the Entry widget.

The syntax to use the Scrollbar widget is given below.

Syntax

w = Scrollbar(top, options)
A list of possible options is given below.

SN	Option	Description
1	activebackground	The background color of the widget when it has the focus.
2	bg	The background color of the widget.
3	bd	The border width of the widget.
4	command	It can be set to the procedure associated with the list
which can be called each time when the scrollbar is moved.
5	cursor	The mouse pointer is changed to the cursor type set to this option which can be an arrow, dot, etc.
6	elementborderwidth	It represents the border width around the arrow heads and slider. The default value is -1.
7	Highlightbackground	The focus highlighcolor when the widget doesn't have the focus.
8	highlighcolor	The focus highlighcolor when the widget has the focus.
9	highlightthickness	It represents the thickness of the focus highlight.
10	jump	It is used to control the behavior of the scroll jump.
If it set to 1, then the callback is called when the user releases the mouse button.
11	orient	It can be set to HORIZONTAL or VERTICAL depending upon the orientation of the scrollbar.
12	repeatdelay	This option tells the duration up to which the button is to be pressed
before the slider starts moving in that direction repeatedly. The default is 300 ms.
13	repeatinterval	The default value of the repeat interval is 100.
14	takefocus	We can tab the focus through this widget by default. We can set this option to 0
if we don't want this behavior.
15	troughcolor	It represents the color of the trough.
16	width	It represents the width of the scrollbar.
Methods

The widget provides the following methods.

SN	Method	Description
1	get()	It returns the two numbers a and b which represents the current position of the scrollbar.
2	set(first, last)	It is used to connect the scrollbar to the other widget w.
The yscrollcommand or xscrollcommand of the other widget to this method.
"""

from tkinter import *

top = Tk()
sb = Scrollbar(top)
sb.pack(side=RIGHT, fill=Y)

mylist = Listbox(top, yscrollcommand=sb.set)

for line in range(30):
    mylist.insert(END, "Number " + str(line))

mylist.pack(side=LEFT)
sb.config(command=mylist.yview)

mainloop()
