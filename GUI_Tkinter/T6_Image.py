from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("This is my title")
#root.iconbitmap("xxx.ico")


my_img = ImageTk.PhotoImage(Image.open("/Users/aegis/Downloads/IMG_6382.JPG"))
my_label = Label(image=my_img)
my_label.pack()


button_quit = Button(root, text="quit", command=root.quit)
button_quit.pack()


root.mainloop()
