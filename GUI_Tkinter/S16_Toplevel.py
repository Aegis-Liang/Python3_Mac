"""
Tkinter Toplevel

The Toplevel widget is used to create and display the toplevel windows which are directly managed by the window manager.
The toplevel widget may or may not have the parent window on the top of them.

The toplevel widget is used when a python application needs to represent some extra information, pop-up, or the group of
widgets on the new window.

The toplevel windows have the title bars, borders, and other window decorations.

The syntax to use the Toplevel widget is given below.

Syntax

w = Toplevel(options)
A List of possible options is given below.

SN	Options	Description
1	bg	It represents the background color of the window.
2	bd	It represents the border size of the window.
3	cursor	The mouse pointer is changed to the cursor type set to the arrow, dot, etc. when the mouse is in the window.
4	class_	The text selected in the text widget is exported to be selected to the window manager.
We can set this to 0 to make this behavior false.
5	font	The font type of the text inserted into the widget.
6	fg	The foreground color of the widget.
7	height	It represents the height of the window.
8	relief	It represents the type of the window.
9	width	It represents the width of the window,
Methods

The methods associated with the Toplevel widget is given in the following list.

SN	Method	Description
1	deiconify()	This method is used to display the window.
2	frame()	It is used to show a system dependent window identifier.
3	group(window)	It is used to add this window to the specified window group.
4	iconify()	It is used to convert the toplevel window into an icon.
5	protocol(name, function)	It is used to mention a function which will be called for the specific protocol.
6	state()	It is used to get the current state of the window. Possible values are normal, iconic, withdrawn, and icon.
7	transient([master])	It is used to convert this window to a transient window (temporary).
8	withdraw()	It is used to delete the window but doesn't destroy it.
9	maxsize(width, height)	It is used to declare the maximum size for the window.
10	minsize(width, height)	It is used to declare the minimum size for the window.
11	positionfrom(who)	It is used to define the position controller.
12	resizable(width, height)	It is used to control whether the window can be resizable or not.
13	sizefrom(who)	It is used to define the size controller.
14	title(string)	It is used to define the title for the window.
"""

from tkinter import *

root = Tk()

root.geometry("200x200")


def open():
    top = Toplevel(root)
    top.mainloop()


btn = Button(root, text="open", command=open)

btn.place(x=75, y=50)

root.mainloop()
