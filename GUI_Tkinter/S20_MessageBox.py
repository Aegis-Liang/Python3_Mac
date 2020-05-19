"""
Tkinter messagebox

The messagebox module is used to display the message boxes in the python applications.
There are the various functions which are used to display the relevant messages depending upon
the application requirements.

The syntax to use the messagebox is given below.

Syntax

messagebox.function_name(title, message [, options])
Parameters

function_name: It represents an appropriate message box function.
title: It is a string which is shown as a title of a message box.
message: It is the string to be displayed as a message on the message box.
options: There are various options which can be used to configure the message dialog box.
The two options that can be used are default and parent.

1. default

The default option is used to mention the types of the default button, i.e. ABORT, RETRY, or IGNORE in the message box.

2. parent

The parent option specifies the parent window on top of which, the message box is to be displayed.

There is one of the following functions used to show the appropriate message boxes.
All the functions are used with the same syntax but have the specific functionalities.

1. showinfo()

The showinfo() messagebox is used where we need to show some relevant information to the user.
"""

# !/usr/bin/python3

from tkinter import *
from tkinter import messagebox

top = Tk()
top.geometry("100x100")

messagebox.showinfo("information", "Information")

top.mainloop()



"""
2. showwarning()

This method is used to display the warning to the user. Consider the following example.

Example

# !/usr/bin/python3  
from tkinter import *  
  
from tkinter import messagebox  
  
top = Tk()  
top.geometry("100x100")  
messagebox.showwarning("warning","Warning")  
  
top.mainloop()  
Output:

Python Tkinter messagebox
3. showerror()

This method is used to display the error message to the user. Consider the following example.

Example

# !/usr/bin/python3  
from tkinter import *  
from tkinter import messagebox  
  
top = Tk()  
top.geometry("100x100")  
messagebox.showerror("error","Error")  
top.mainloop()  
Output:

Python Tkinter messagebox
4. askquestion()

This method is used to ask some question to the user which can be answered in yes or no. Consider the following example.

Example

# !/usr/bin/python3  
from tkinter import *  
from tkinter import messagebox  
  
top = Tk()  
top.geometry("100x100")  
messagebox.askquestion("Confirm","Are you sure?")  
top.mainloop()  
Output:

Python Tkinter messagebox
5. askokcancel()

This method is used to confirm the user's action regarding some application activity. Consider the following example.

Example

# !/usr/bin/python3  
from tkinter import *  
from tkinter import messagebox  
  
top = Tk()  
top.geometry("100x100")  
messagebox.askokcancel("Redirect","Redirecting you to www.javatpoint.com")  
top.mainloop()  
Output:

Python Tkinter messagebox
6. askyesno()

This method is used to ask the user about some action to which, the user can answer in yes or no. 
Consider the following example.

Example

# !/usr/bin/python3  
from tkinter import *  
from tkinter import messagebox  
  
top = Tk()  
top.geometry("100x100")  
messagebox.askyesno("Application","Got It?")  
top.mainloop()  
Output:

Python Tkinter messagebox
7. askretrycancel()

This method is used to ask the user about doing a particular task again or not. Consider the following example.

Example

# !/usr/bin/python3  
from tkinter import *  
from tkinter import messagebox  
  
top = Tk()  
top.geometry("100x100")  
messagebox.askretrycancel("Application","try again?")  
  
top.mainloop()  
"""
