"""
Python Tkinter Button

The button widget is used to add various types of buttons to the python application.
Python allows us to configure the look of the button according to our requirements.
Various options can be set or reset depending upon the requirements.

We can also associate a method or function with a button which is called when the button is pressed.

The syntax to use the button widget is given below.


Syntax

W = Button(parent, options)
A list of possible options is given below.

SN	Option	Description
1	activebackground	It represents the background of the button when the mouse hover the button.
2	activeforeground	It represents the font color of the button when the mouse hover the button.
3	Bd	It represents the border width in pixels.
4	Bg	It represents the background color of the button.
5	Command	It is set to the function call which is scheduled when the function is called.
6	Fg	Foreground color of the button.
7	Font	The font of the button text.
8	Height	The height of the button. The height is represented in the number of text lines for the textual lines or the number of pixels for the images.
10	Highlightcolor	The color of the highlight when the button has the focus.
11	Image	It is set to the image displayed on the button.
12	justify	It illustrates the way by which the multiple text lines are represented. It is set to LEFT for left justification, RIGHT for the right justification, and CENTER for the center.
13	Padx	Additional padding to the button in the horizontal direction.
14	pady	Additional padding to the button in the vertical direction.
15	Relief	It represents the type of the border. It can be SUNKEN, RAISED, GROOVE, and RIDGE.
17	State	This option is set to DISABLED to make the button unresponsive. The ACTIVE represents the active state of the button.
18	Underline	Set this option to make the button text underlined.
19	Width	The width of the button. It exists as a number of letters for textual buttons or pixels for image buttons.
20	Wraplength	If the value is set to a positive number, the text lines will be wrapped to fit within this length.
"""

from tkinter import *

top = Tk()
top.geometry("200x100")


def fun():
    print("Hello", "Red Button clicked")


b1 = Button(top, text="Red", command=fun, activeforeground="red", activebackground="pink", pady=10)
b2 = Button(top, text="Blue", activeforeground="blue", activebackground="pink", pady=10)
b3 = Button(top, text="Green", activeforeground="green", activebackground="pink", pady=10)
b4 = Button(top, text="Yellow", activeforeground="yellow", activebackground="pink", pady=10)

b1.pack(side=LEFT)
b2.pack(side=RIGHT)
b3.pack(side=TOP)
b4.pack(side=BOTTOM)

top.mainloop()
