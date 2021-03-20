from tkinter import *
from tkinter import filedialog
import csv
import os

class Imgbutton(Canvas):

    def __init__(self, master=None, image=None, command=None, **kw):

        # Declared style to keep a reference to the original relief
        style = kw.get("relief", "groove")        

        if not kw.get('width') and image:
            kw['width'] = image.width()
        else: kw['width'] = 50

        if not kw.get('height') and image:
            kw['height'] = image.height()
        else: kw['height'] = 24

        kw['relief'] = style
        kw['borderwidth'] = kw.get('borderwidth', 2)
        kw['highlightthickness'] = kw.get('highlightthickness',0)

        super(Imgbutton, self).__init__(master=master, **kw)

        self.set_img = self.create_image(kw['borderwidth'], kw['borderwidth'], 
                anchor='nw', image=image)

        self.bind_class( self, '<Button-1>', 
                    lambda _: self.config(relief='sunken'), add="+")

        # Used the relief reference (style) to change back to original relief.
        self.bind_class( self, '<ButtonRelease-1>', 
                    lambda _: self.config(relief=style), add='+')

        self.bind_class( self, '<Button-1>', 
                    lambda _: command() if command else None, add="+")

filename = "apps.csv"
fields = []
with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
temp = fields

def input0(event=None):        
    if fields[0] == "":
        print("Add element")
    else: 
        command = "start cmd /c " + fields[0][:-4] + ".lnk"
        print(command)
        os.system(command)

def input1(event=None):        
    if fields[0] == "":
        print("Add element")
    else: 
        command = "start cmd /c " + fields[1][:-4] + ".lnk"
        os.system(command)

def input2(event=None):        
    if fields[0] == "":
        print("Add element")
    else: 
        command = "start cmd /c " + fields[2][:-4] + ".lnk"
        os.system(command)

def input3(event=None):        
    if fields[0] == "":
        print("Add element")
    else: 
        command = "start cmd /c " + fields[3][:-4] + ".lnk"
        os.system(command)

def input4(event=None):        
    if fields[0] == "":
        print("Add element")
    else: 
        command = "start cmd /c " + fields[4][:-4] + ".lnk"
        os.system(command)

def run():
    root = Tk()
    root.title(' MiniDock')
    attributes = root.attributes('-alpha', 0.9)
    background_color = '#1e1e1e'
    
    root['bg'] = background_color

    # attributes = root.attributes("-fullscreen", True)
    root.geometry("1920x480")
    # root.resizable(0, 0)

    icon = PhotoImage(file = 'plus_sign.png')

    images = []
    for i in range(len(temp)):
        if temp[i] == "+":
            images.append(icon)
        
        else:
            temp[i] += ".png"
            images.append(PhotoImage(file = temp[i]))
    
    button1 = Imgbutton(root, image = images[0], borderwidth = 0, command = input0, bg = background_color)
    button1.place(relx = 1/30, rely = 112/480, relwidth = 0.2, relheight = 1)

    button2 = Imgbutton(root, image = images[1], borderwidth = 0, command = input1, bg = background_color)
    button2.place(relx = 7/30, rely = 112/480, relwidth = 0.2, relheight = 1)

    button3 = Imgbutton(root, image = images[2], borderwidth = 0, command = input2, bg = background_color)
    button3.place(relx = 13/30, rely = 112/480, relwidth = 0.2, relheight = 1)

    button4 = Imgbutton(root, image = images[3], borderwidth = 0, command = input3, bg = background_color)
    button4.place(relx = 19/30, rely = 112/480, relwidth = 0.2, relheight = 1)

    button5 = Imgbutton(root, image = images[4], borderwidth = 0, command = input4, bg = background_color)
    button5.place(relx = 25/30, rely = 112/480, relwidth = 0.2, relheight = 1)

    root.iconbitmap(r"app_icon.ico")

    root.mainloop()

run()
