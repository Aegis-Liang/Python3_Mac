"""
Python Tkinter Text

The Text widget is used to show the text data on the Python application. However, Tkinter provides us the Entry widget
which is used to implement the single line text box.

The Text widget is used to display the multi-line formatted text with various styles and attributes.
The Text widget is mostly used to provide the text editor to the user.

The Text widget also facilitates us to use the marks and tabs to locate the specific sections of the Text.
We can also use the windows and images with the Text as it can also be used to display the formatted text.

The syntax to use the Text widget is given below.

Syntax

w = Text(top, options)
A list of possible options that can be used with the Text widget is given below.

SN	Option	Description
1	bg	The background color of the widget.
2	bd	It represents the border width of the widget.
3	cursor	The mouse pointer is changed to the specified cursor type, i.e. arrow, dot, etc.
4	exportselection	The selected text is exported to the selection in the window manager. We can set this to 0 if we don't want the text to be exported.
5	font	The font type of the text.
6	fg	The text color of the widget.
7	height	The vertical dimension of the widget in lines.
8	highlightbackground	The highlightcolor when the widget doesn't has the focus.
9	highlightthickness	The thickness of the focus highlight. The default value is 1.
10	highlighcolor	The color of the focus highlight when the widget has the focus.
11	insertbackground	It represents the color of the insertion cursor.
12	insertborderwidth	It represents the width of the border around the cursor. The default is 0.
13	insertofftime	The time amount in Milliseconds during which the insertion cursor is off in the blink cycle.
14	insertontime	The time amount in Milliseconds during which the insertion cursor is on in the blink cycle.
15	insertwidth	It represents the width of the insertion cursor.
16	padx	The horizontal padding of the widget.
17	pady	The vertical padding of the widget.
18	relief	The type of the border. The default is SUNKEN.
19	selectbackground	The background color of the selected text.
20	selectborderwidth	The width of the border around the selected text.
21	spacing1	It specifies the amount of vertical space given above each line of the text. The default is 0.
22	spacing2	This option specifies how much extra vertical space to add between displayed lines of text
when a logical line wraps. The default is 0.
23	spacing3	It specifies the amount of vertical space to insert below each line of the text.
24	state	It the state is set to DISABLED, the widget becomes unresponsive to the mouse and keyboard unresponsive.
25	tabs	This option controls how the tab character is used to position the text.
26	width	It represents the width of the widget in characters.
27	wrap	This option is used to wrap the wider lines into multiple lines.
Set this option to the WORD to wrap the lines after the word that fit into the available space.
The default value is CHAR which breaks the line which gets too wider at any character.
28	xscrollcommand	To make the Text widget horizontally scrollable, we can set this option to the set() method of
Scrollbar widget.
29	yscrollcommand	To make the Text widget vertically scrollable, we can set this option to the set() method of
Scrollbar widget.
Methods

We can use the following methods with the Text widget.

SN	Method	Description
1	delete(startindex, endindex)	This method is used to delete the characters of the specified range.
2	get(startindex, endindex)	It returns the characters present in the specified range.
3	index(index)	It is used to get the absolute index of the specified index.
4	insert(index, string)	It is used to insert the specified string at the given index.
5	see(index)	It returns a boolean value true or false depending upon
whether the text at the specified index is visible or not.
Mark handling methods

Marks are used to bookmark the specified position between the characters of the associated text.

SN	Method	Description
1	index(mark)	It is used to get the index of the specified mark.
2	mark_gravity(mark, gravity)	It is used to get the gravity of the given mark.
3	mark_names()	It is used to get all the marks present in the Text widget.
4	mark_set(mark, index)	It is used to inform a new position of the given mark.
5	mark_unset(mark)	It is used to remove the given mark from the text.
Tag handling methods

The tags are the names given to the separate areas of the text.
The tags are used to configure the different areas of the text separately.
The list of tag-handling methods along with the description is given below.

SN	Method	Description
1	tag_add(tagname, startindex, endindex)	This method is used to tag the string present in the specified range.
2	tag_config	This method is used to configure the tag properties.
3	tag_delete(tagname)	This method is used to delete a given tag.
4	tag_remove(tagname, startindex, endindex)	This method is used to remove a tag from the specified range.
"""

from tkinter import *

top = Tk()
text = Text(top)
text.insert(INSERT, "Name.....")
text.insert(END, "Salary.....")

text.pack()

text.tag_add("Write Here", "1.0", "1.4")
text.tag_add("Click Here", "1.8", "1.13")

text.tag_config("Write Here", background="yellow", foreground="black")
text.tag_config("Click Here", background="black", foreground="white")

top.mainloop()
