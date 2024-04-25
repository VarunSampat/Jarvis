from tkinter import *
from Libraries import friday 

def buttonClick(self):
    friday.main()
    root.destroy()

root = Tk()
c = Canvas(root,height = 600,width = 1200)
file1 = PhotoImage(file="background.gif")
id = c.create_image(600,275,anchor = CENTER,image = file1)
c.pack()
id = c.create_oval(357,67,815,530,width = 0)
c.tag_bind(id,"<Button-1>", buttonClick)
root.title("Friday")


root.mainloop()